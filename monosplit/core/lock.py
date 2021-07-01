from tinydb import TinyDB


def create_lock_object(app, path):
    app.extend('lock', TinyDB(path))
    print('Lock hook executed')
