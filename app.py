import os
import yaml

CONFIG_FILE = 'monosplit.yml'


def init():
    try:
        os.mkdir('.monosplit')
    except FileExistsError:
        print('Directory already exist !')


def getConfig():
    data = yaml.load(open(CONFIG_FILE), Loader=yaml.FullLoader)

    print(data)


def scanProject(path=".", configs=[]):
    if hasConfig(path):
        configs.append(os.path.join(path, CONFIG_FILE))

    entries = os.scandir(path)

    for entry in entries:
        if entry.is_dir():
            scanProject(entry, configs)

    return configs


def hasConfig(path="."):
    return os.path.exists(os.path.join(path, CONFIG_FILE))


print(scanProject())
