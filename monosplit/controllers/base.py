from cement import Controller, ex
from ..core.version import VERSION_BANNER
from pyfiglet import figlet_format


class Base(Controller):
    class Meta:
        label = 'base'
        description = 'A Git plugin for monorepo management\n\n\n{}\n\n'.format(
            figlet_format('Monosplit', font='slant'))
        arguments = [
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()
