#!/usr/bin/env python

"""

 This module has following purposes:
    to detect correct mime types for files in artifact,
    assign correct mime types for objects during upload to s3 bucket,
    block unwanted mime types assign respective meta data,
    aws s3 sync with --no-guess-mime-type is used
    to remove deltas between source and target.

Example:

        $ python mime_type_verification.py

Attributes:

    APP_DIR (str): name of directory, set from env varibale.
    EXPIRE_DATE (str): expiration value for assets, set from env varibale.
    WORKER (str): Jenkins slave env name, set from env varibale.
    REGION (str): aws s3 region name, set from env varibale.
    S3_BUCKET (str): name of s3 bucket for objects upload.

Exception:
    in case of identifying "application/octet-stream" content type.

"""
import mimetypes
import os

import boto3

APP_DIR = os.environ['appDir']
EXPIRE_DATE = os.environ['expireDate']
WORKER = os.environ['worker']
REGION = os.environ['region']
S3_BUCKET = "wh-sports-{}-static-assets-{}".format(WORKER, REGION)


def get_list_of_files(dir_name):
    """Get list of files under directory:

    Args:
        one parameter with directory name.

    Returns:
        list of files under specified dir path.

    """
    list_of_files = os.listdir(dir_name)
    all_files = list()
    for entry in list_of_files:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files


def guess_mime():
    """Assign correct mime types for objects during upload to s3 bucket:

    Args:
        one parameter with list of files to be checked.

    Returns:
        dictionary with mapping of filename and its mime type value.

    """
    file_mime_type = {}
    for file in list_of_files:
        mime_type = mimetypes.guess_type(file)[0]
        if mime_type == 'None':
            mime_type = "text/plain"
        if mime_type == "application/octet-stream":
            raise Exception("Error: application/octet-stream is not allowed")
        if "healthcheck" in file:
            mime_type = "application/json"
        file_mime_type.update({file: mime_type})
    return file_mime_type


def s3_upload(mime_types_list, s3_bucket, region_name, expire_date):
    '''Get mime types assocaited with files:

    Args:
        one parameter with list of files to be checked.

    Returns:
        dictionary with mapping of filename and its mime type value.s

    '''
    s3 = boto3.resource('s3', REGION)
    max_age_files = {}
    for (key, value) in mime_types_list.iteritems():
        if "healthcheck" in key:
            max_age_files.update({key: value})
        elif "stats.json" in key:
            max_age_files.update({key: value})
    for (k, v) in max_age_files.iteritems():
        s3.meta.client.upload_file(
            k, s3_bucket, k, ExtraArgs={'ContentType': v,
                                        'CacheControl': 'max-age=60'})
    for (key, value) in max_age_files.iteritems():
        file_mime_type.pop(key, value)
    for (key, value) in mime_types_list.iteritems():
        s3.meta.client.upload_file(
            key, s3_bucket, key, ExtraArgs={
                'ContentType': value, 'CacheControl':
                'public,max-age=31536000', 'Expires': expire_date})


list_of_files = get_list_of_files(APP_DIR)
file_mime_type = guess_mime()
print(file_mime_type)
s3_upload(file_mime_type, S3_BUCKET, REGION, EXPIRE_DATE)
