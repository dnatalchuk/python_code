#!/usr/bin/env python

import os
import mimetypes

# 1. Mime-type detection for directory with assets based on file extesnions:
dirName = "/Users/denysnatalchuk/whc/platform_team/jenkins-jobs/assests_copy/"

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
    for file in listOfFiles:
        mime_type = mimetypes.guess_type(file)
        if mime_type == None:
            mime_type = "text/plain"
        if mime_type == "application/octet-stream":
            raise Exception("application/octet-stream content type is not allowed")
        return mime_type
        print file, mime_type

guess_mime()
