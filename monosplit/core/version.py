from cement.utils.version import get_version as cement_get_version
from cement.utils.version import get_version_banner

VERSION = (0, 0, 1, 'alpha', 0)


def get_version(version=VERSION):
    return cement_get_version(version)


VERSION_BANNER = """
A Git plugin for monorepo management %s
%s
""" % (get_version(), get_version_banner())
