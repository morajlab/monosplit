import os
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from ..core.app import init
from ..core.project import scan_project, validate_config_schema
from ..core.config import get_ms_config
from ..core.lock import create_lock_content
from tinydb import where

VERSION_BANNER = """
A Git plugin for monorepo management %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'A Git plugin for monorepo management'

        # text displayed at the bottom of --help output
        epilog = 'Usage: monosplit command1 --foo bar'

        # controller level arguments. ex: 'monosplit --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help="Initialize monorepo",
        arguments=[
            (['-p', '--path'],
             {'help': 'Root repository path',
              'action': 'store',
              'dest': 'path'}),
        ],
    )
    def init(self):
        ms_config = get_ms_config(self.app)

        data = {
            'path': '.'
        }

        if self.app.pargs.path is not None:
            data['path'] = self.app.pargs.path

        init(self.app, data['path'])

        configs = scan_project(
            '{}{}'.format(ms_config['config_file_name'], ms_config['config_file_suffix']),
            data['path'])

        for config_path in configs:
            if validate_config_schema(path=config_path)['valid']:
                lock_content = create_lock_content(config_path)

                self.app.lock.upsert(lock_content, where('hash') == lock_content['hash'])
            else:
                self.app.log.warning(
                    '"{}" repository is not configured properly !'.format(os.path.dirname(config_path)))

        self.app.log.info('Repository initialized successfully !')
