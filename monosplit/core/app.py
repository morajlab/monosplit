import os
import yaml

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





push_repository("https://gitlab.com/morajlab/test-repo.git", "./test/mono-test", "This is a commit from monosplit")
