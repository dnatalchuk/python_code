"""

 This module has the following purposes:
    provide collection of functions to be used/
    imported by deployment python scripts, executed
    within static content deployment pipeline.

Example of import in python script:

        from deployment_package.functions import guess_mimes

Attributes:

    dir_name (str): name of directory to get a list of files;
    set_of_files (list): list of files to guess mime types;
    mime_types_list (dict): mapping of files and mime types associated;
    s3_bucket (str): name of s3 bucket for objects to be uploaded;
    region_name (str): aws s3 region name, set from env varibale;
    expire_date (str): expiration value for assets, set from env varibale;
    app_dir (str): directory name for static assets, set from env varibale;
    sync_dry_output (list): output of aws sync --dryrun command;

Exception:
    in case of identifying "application/octet-stream" content type.

"""

import mimetypes
import os
import subprocess

import boto3


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
        if asset.split('/')[-1] == "asset_1":
            mime_type = "application/json"
        files_mime_type.update({asset: mime_type})
    return files_mime_type


def s3_upload(mime_types_list, s3_bucket, region_name, expire_date):
    '''Get mime types assocaited with files:

    Args:
        parameter with list of files to be checked, targeted s3 bucket,
        region name for bucket, expiration date for assets.

    Returns:
        dictionary with mapping of filename and its mime type value.s

    '''
    s3 = boto3.resource('s3', region_name)
    max_age_files = {}
    for (asset, mime) in mime_types_list.iteritems():
        if asset.split('/')[-1] == "asset_1":
            max_age_files.update({asset: mime})
        elif asset.split('/')[-1] == "asset_2":
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


def sync_upload_list(sync_dry_output):
    '''
    Extract, format objects to be uploaded from output of
    aws s3 sync --dryrun command.
    Objects indentified will have correct mime types and meta data assigned.

    Args:
        one parameter with output of aws s3 sync --dryrun command.

    Returns:
        dictionary with mapping of filename and its mime type
        value for objects be uploaded.
    '''
    formatted_object = ''
    prepared_object = ''
    upload_objects = []
    upload_objects_mime = []
    for entry in range(len(sync_dry_output)-1):
        if sync_dry_output[entry] == "upload:":
            formatted_object = sync_dry_output[entry+3].split('/')[3:]
            prepared_object = '/'.join(formatted_object)
            upload_objects.append(prepared_object)
            upload_objects_mime = guess_mime(upload_objects)
    return upload_objects_mime


def sync_upload_and_delete(upload_objects_list, s3_bucket, region_name, expire_date, app_dir):
    '''
    If input parameter is not empty, objects will be uploaded
    to s3 from input parameter.
    After upload completion - aws s3 sync --no-guess-mime-type command
    will be executed to remove deltas between source and target.

    If input parameter is empty -
    just aws s3 sync --no-guess-mime-type command will be executed.

    Args:
        output of aws s3 sync --dryrun command, targeted s3 bucket,
        region name for bucket, expiration date for assets, app directory
        set from env variable.

    Returns:
        dictionary with mapping of filename and its mime type
        value for objects be uploaded.
    '''
    if upload_objects_list:
        print "Upload has been detected during aws s3 sync:\n\n",  upload_objects_list, "\n"
        s3_upload(upload_objects_list, s3_bucket, region_name, expire_date)
        sync_after_upload = subprocess.check_output(
            'aws s3 sync --region {} --delete \
            --no-guess-mime-type "{}" \
            "s3://{}/{}"'.format(region_name, app_dir, s3_bucket, app_dir), shell=True)
        print sync_after_upload
    else:
        print "Upload has not been detected during aws s3 sync and just delete will be performed:\n"
        sync_with_no_upload = subprocess.check_output(
            'aws s3 sync --region {} --delete \
            --no-guess-mime-type "{}" \
            "s3://{}/{}"'.format(region_name, app_dir, s3_bucket, app_dir), shell=True)
        print sync_with_no_upload
