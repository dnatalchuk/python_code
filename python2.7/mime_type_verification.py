#!/usr/bin/env python

import os
import mimetypes
import boto3
import subprocess

# 1. Mime-type detection for directory with assets based on file extesnions:
dirName = os.environ['appDir']

def getListOfFiles(dirName): 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
listOfFiles = getListOfFiles(dirName)

def guess_mime():
    file_mime_type = {}
    for file in listOfFiles:
        mime_type = mimetypes.guess_type(file)[0]
        if mime_type == None:
            mime_type = "text/plain"
        if mime_type == "application/octet-stream":
            raise Exception("application/octet-stream content type is not allowed")
        if "healthcheck" in file:
            mime_type = "application/json"
        file_mime_type.update({file:mime_type})
    return file_mime_type
file_mime_type = guess_mime()
print file_mime_type

# 2. Create file sets based on mime-type detected:
cli = boto3.client('s3')
s3 = boto3.resource('s3', region_name = "eu-west-2")
max_age_files = {}
for (key, value) in file_mime_type.iteritems():
    # 3. Assign max-age=60 for healthcheck and stats.json
    if "healthcheck" in key:
        max_age_files.update({key:value})
    elif "stats.json" in key:
        max_age_files.update({key:value})
for (k,v) in max_age_files.iteritems():
    s3.meta.client.upload_file(
        k, "dn-bucket", k, ExtraArgs={'ContentType': v, 'CacheControl':'max-age=60'})
for (key, value) in max_age_files.iteritems():
    file_mime_type.pop(key, value)
for (key, value) in file_mime_type.iteritems():
    s3.meta.client.upload_file(
        key, "dn-bucket", key, ExtraArgs={'ContentType': value, 'CacheControl':'public,max-age=31536000'})
        
# 4. aws sync to remove deltas between source and target:
sync = subprocess.call("aws s3 sync --region ${region} --delete --no-guess-mime-type=True {appDir} s3://dn-bucket",shell=True))
