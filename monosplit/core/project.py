import os
import yaml


def get_config(path):
    data = yaml.load(open(path), Loader=yaml.FullLoader)

    print(data)


def scan_project(name, path=".", configs=[]):
    if has_config(name, path):
        configs.append(os.path.join(path, name))

    entries = os.scandir(path)

    for entry in entries:
        if entry.is_dir():
            scan_project(name, entry, configs)

    return configs


def has_config(name, path="."):
    return os.path.exists(os.path.join(path, name))
