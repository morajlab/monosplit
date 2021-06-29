import os
import yaml
import shutil
from tempfile import TemporaryDirectory
from git import Repo

CONFIG_FILE = 'monosplit.yml'


def init():
    try:
        os.mkdir('.monosplit')
    except FileExistsError:
        print('Directory already exist !')


def get_config():
    data = yaml.load(open(CONFIG_FILE), Loader=yaml.FullLoader)

    print(data)


def scan_project(path=".", configs=[]):
    if has_config(path):
        configs.append(os.path.join(path, CONFIG_FILE))

    entries = os.scandir(path)

    for entry in entries:
        if entry.is_dir():
            scan_project(entry, configs)

    return configs


def has_config(path="."):
    return os.path.exists(os.path.join(path, CONFIG_FILE))


def push_repository(repo_url, repo_path):
    with TemporaryDirectory() as tmpdir:
        print('Temporary directory is', tmpdir)

        cloned_repo = Repo.clone_from(repo_url, tmpdir)

        print(cloned_repo.is_dirty())

        shutil.copytree(repo_path, tmpdir, dirs_exist_ok=True)
        entries = os.scandir(tmpdir)

        for entry in entries:
            print(entry)

        print(cloned_repo.is_dirty())

def get_latest_commits(path="."):
    pass