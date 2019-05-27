#!/usr/bin/env python

"""
This script has the following purposes.
    to detect correct mime types for files in artifact,
    assign correct mime types for objects during upload to s3 bucket,
    block unwanted mime types and assign respective meta data,
    aws s3 sync with --no-guess-mime-type is used
    to remove deltas between source and target.

Example:

        $ python mime_type_verification_and_upload.py

Attributes:

    APP_DIR (str): name of directory, set from env variable;
    EXPIRE_DATE (str): expiration value for assets, set from env variable;
    WORKER (str): Jenkins slave env name, set from env variable;
    REGION (str): aws s3 region name, set from env variable;
    S3_BUCKET (str): name of s3 bucket for objects upload;

Exception:
    in case of identifying "application/octet-stream" content type.

"""
import os

from module.functions import get_list_of_files
from module.functions import guess_mime
from module.functions import s3_upload

APP_DIR = os.environ['appDir']
EXPIRE_DATE = os.environ['expireDate']
WORKER = os.environ['worker']
REGION = os.environ['region']
S3_BUCKET = "bucket-{}-{}".format(WORKER, REGION)

if __name__ == "__main__":
    FILE_SETS = get_list_of_files(APP_DIR)
    FILES_MIME_TYPE = guess_mime(FILE_SETS)
    print FILES_MIME_TYPE
    s3_upload(FILES_MIME_TYPE, S3_BUCKET, REGION, EXPIRE_DATE)
