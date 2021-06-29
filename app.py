import os
import yaml
import shutil
from git import Repo

CONFIG_FILE = "monosplit.yml"
CONFIG_DIRECTORY = ".monosplit"


def init():
    try:
        os.mkdir(CONFIG_DIRECTORY)
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


def push_repository(repo_url, repo_path, message):
    tmpdir = os.path.join(os.path.curdir, "temp")
    os.mkdir(tmpdir)
    print('Temporary directory is', tmpdir)
    clone_directory = os.path.join(tmpdir, "test-repo")
    repo = Repo.clone_from(repo_url, clone_directory)
    shutil.copytree(repo_path, clone_directory, dirs_exist_ok=True)

    if repo.is_dirty():
        print("Repository is dirty !")
        repo.git.add(A=True)
        repo.index.commit(message)
        origin = repo.remote(name="origin")
        origin.push()


push_repository("https://gitlab.com/morajlab/test-repo.git", "./test/mono-test", "This is a commit from monosplit")
