#!/usr/bin/env python

"""

 This module has following purposes:
    to detect correct mime types for files in artifact,
    assign correct mime types for objects during upload to s3 bucket,
    block unwanted mime types and assign respective meta data,
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


def guess_mime(set_of_files):
    """Assign correct mime types for objects during upload to s3 bucket:

    Args:
        one parameter with list of files to be checked.

    Returns:
        dictionary with mapping of filename and its mime type value.

    """
    files_mime_type = {}
    for asset in set_of_files:
        mime_type = mimetypes.guess_type(asset)[0]
        if mime_type is None:
            mime_type = "text/plain"
        if mime_type == "application/octet-stream":
            raise Exception("Error: application/octet-stream is not allowed", asset)
        if asset.split('/')[-1] == "healthcheck":
            mime_type = "application/json"
        files_mime_type.update({asset: mime_type})
    return files_mime_type


def s3_upload(mime_types_list, s3_bucket, region_name, expire_date):
    '''Get mime types assocaited with files:

    Args:
        one parameter with list of files to be checked.

    Returns:
        dictionary with mapping of filename and its mime type value.s

    '''
    s3 = boto3.resource('s3', region_name)
    max_age_files = {}
    for (asset, mime) in mime_types_list.iteritems():
        if asset.split('/')[-1] == "healthcheck":
            max_age_files.update({asset: mime})
        elif asset.split('/')[-1] == "stats.json":
            max_age_files.update({asset: mime})
    for (max_age_file, max_age_file_mime) in max_age_files.iteritems():
        s3.meta.client.upload_file(
            max_age_file, s3_bucket, max_age_file, ExtraArgs={
                'ContentType': max_age_file_mime,
                'CacheControl': 'max-age=60'})
    for (max_age_file, max_age_file_mime) in max_age_files.iteritems():
        mime_types_list.pop(max_age_file, max_age_file_mime)
    for (asset, mime) in mime_types_list.iteritems():
        s3.meta.client.upload_file(
            asset, s3_bucket, asset, ExtraArgs={
                'ContentType': mime, 'CacheControl':
                'public,max-age=31536000', 'Expires': expire_date})


FILE_SETS = get_list_of_files(APP_DIR)
FILES_MIME_TYPE = guess_mime(FILE_SETS)
print FILES_MIME_TYPE
s3_upload(FILES_MIME_TYPE, S3_BUCKET, REGION, EXPIRE_DATE)
