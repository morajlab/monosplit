
from setuptools import setup, find_packages
from monosplit.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='monosplit',
    version=VERSION,
    description='A Git plugin for monorepo management',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Morteza Jamali',
    author_email='mortezajamali4241@gmail.com',
    url='https://github.com/morajlab/monosplit',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'monosplit': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        monosplit = monosplit.main:main
    """,
)
