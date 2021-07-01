import os
import hashlib
from .project import get_config
from tinydb import TinyDB


def create_lock_object(app, path):
    app.extend('lock', TinyDB(path))


def create_lock_content(config_path):
    repo_path = os.path.dirname(config_path)
    config = get_config(config_path)
    config.update({'hash': hashlib.md5(repo_path.encode()).hexdigest(), 'path': repo_path})

    return config
