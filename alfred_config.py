from __future__ import print_function

import os

from alfred_file import AlfredFile, get_workflow_data_dir

config_file = AlfredFile(get_workflow_data_dir(), 'config.json')


# Returns config file in write mode
def get_config_file_in_write_mode():
    return open(config_file.get_file_name(), 'w+')


# Writes the config dictionary to config file.
def write_to_config_file(config_dict):
    config_file.write_to_file(config_dict)


# Returns the configuration for the workflow in dictionary format
def read_config():
    return config_file.read_json_file()


if __name__ == '__main__':
    os.environ[
        'alfred_workflow_data'] = '/Users/rhasija/Google Drive/Alfred/Alfred.alfredpreferences/workflows/user.workflow.B865A65B-5916-46CE-AE15-D413FFB64F64'
    read_config()
