import math
import os

import yaml


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def get_config():
    with open("config.yml", 'r') as stream:
        return yaml.safe_load(stream)


def get_dst_dir(conf=None):
    if not conf:
        conf = get_config()
    return os.path.join(*conf['photo_dir_path'])


