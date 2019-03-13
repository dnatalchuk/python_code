#!/usr/bin/env python

"""

 This script has the following purposes:
    aws s3 sync with --no-guess-mime-type is used to remove deltas
    between source and target. In case if upload action has been detected by
    `aws s3 sync --dryrun`: for object upload will be used functions for mime
    type verification and s3_upload from 'deployment_package/functions.py',
    ensuring verification logic and correct meta data applied.
    After object being uploaded - normal aws s3 sync with --no-guess-mime-type
    will be executed ensuring 1:1 match between source and target.
    If no upload has been detected by `aws s3 sync --dryrun` -
    just normal aws s3 sync with --no-guess-mime-type will be executed.

Example:

        $ python s3_sync_and_verification.py

Attributes:

    APP_DIR (str): directory name for static assets, set from env varibale;
    EXPIRE_DATE (str): expiration value for assets, set from env varibale;
    WORKER (str): Jenkins slave env name, set from env varibale;
    REGION (str): aws s3 region name, set from env varibale;
    S3_BUCKET (str): name of s3 bucket for objects upload;
    S3_SYNC_DRY (list): output of aws sync --dryrun command;

Exception:
    in case of identifying "application/octet-stream" content type.

"""
import os
import subprocess

from deployment_package.functions import guess_mime
from deployment_package.functions import s3_upload
from deployment_package.functions import sync_upload_list
from deployment_package.functions import sync_upload_and_delete

APP_DIR = os.environ['appDir']
EXPIRE_DATE = os.environ['expireDate']
WORKER = os.environ['worker']
REGION = os.environ['region']
S3_BUCKET = "bucket-{}-assets-{}".format(WORKER, REGION)

if __name__ == "__main__":
    S3_SYNC_DRY = list(subprocess.check_output(
        'aws s3 sync --dryrun --region {} --delete --no-guess-mime-type \
            "{}" "s3://{}/{}"'.
        format(REGION, APP_DIR, S3_BUCKET, APP_DIR), shell=True).split())
    UPLOAD_OBJECTS = sync_upload_list(S3_SYNC_DRY)
    SYNC_COMPLETION = sync_upload_and_delete(UPLOAD_OBJECTS, S3_BUCKET,
                                             REGION, EXPIRE_DATE, APP_DIR)
