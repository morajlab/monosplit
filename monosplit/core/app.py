import os


def init(meta_directory):
    if is_inited(meta_directory) is not True:
        try:
            os.mkdir(meta_directory)
        except FileExistsError:
            print('Directory already exist !')


def is_inited(meta_directory):
    return os.path.exists(meta_directory)
