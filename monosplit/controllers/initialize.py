import os
from cement import Controller, ex
from ..core.app import init
from ..core.project import scan_project, validate_config_schema
from ..core.config import get_ms_config
from ..core.lock import create_lock_content
from tinydb import where


class Initialize(Controller):
    class Meta:
        label = 'initialize'

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
