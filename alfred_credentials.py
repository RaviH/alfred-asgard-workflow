import os
import base64
from alfred_config import read_config, write_to_config_file


def create_password(password):
    try:
        config_dict = read_config()
        config_dict['password'] = base64.b64encode(password)
        write_to_config_file(config_dict)
        print "Created password config successfully"
    except Exception as e:
        print "Error occurred: ({0}): {1} {2}".format(e.errno, e.strerror, data_dir)


def create_username(username):
    try:
        config_dict = read_config()
        config_dict['username'] = username
        write_to_config_file(config_dict)
        print "Created username config successfully"
    except Exception as e:
        print "Error occurred: ({0}): {1} {2}".format(e.errno, e.strerror, data_dir)


if __name__ == '__main__':
    os.environ['alfred_workflow_data'] = '/tmp'
    create_username('foobar')
