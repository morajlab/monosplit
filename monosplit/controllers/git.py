from cement import Controller, ex


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
        data = {
            'path': '.'
        }

        if self.app.pargs.path is not None:
            data['path'] = self.app.pargs.path
