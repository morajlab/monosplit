import os
from .lock import create_lock_object
from .config import get_ms_config


def init(app, path):
    ms_config = get_ms_config(app)
    meta_directory = os.path.join(path, ms_config['meta_directory'])

    try:
        create_lock_object(app, os.path.join(path, '{}-lock{}'.format(ms_config['config_file_name'], ms_config[
            'config_file_suffix'])))
        if is_inited(app, path) is not True: os.mkdir(meta_directory)
    except OSError:
        pass


def is_inited(app, path):
    return os.path.exists(os.path.join(path, get_ms_config(app)['meta_directory']))
