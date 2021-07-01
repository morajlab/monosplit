def get_ms_config(app):
    return app._meta.__getattribute__('ms_config')
