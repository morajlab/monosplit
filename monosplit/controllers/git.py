import os
from cement import Controller, ex
from ..core.project import scan_project
from ..core.config import get_ms_config
from ..core.app import is_inited


class Git(Controller):
    class Meta:
        label = 'git'

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help="Push repositories",
        arguments=[
            (['-p', '--path'],
             {'help': 'Root repository path',
              'action': 'store',
              'dest': 'path'}),
        ],
    )
    def push(self):
        ms_config = get_ms_config(self.app)

        data = {
            'path': '.'
        }

        if self.app.pargs.path is not None:
            data['path'] = self.app.pargs.path

        if is_inited(os.path.join(data['path'], ms_config['meta_directory'])) is not True:
            print('Repository is not initiated')
            return

        configs = scan_project(
            ms_config['config_file_name'] + ms_config['config_file_suffix'],
            data['path'])

        print(configs)
