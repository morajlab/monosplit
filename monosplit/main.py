from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import MonosplitError
from .controllers import base, git, initialize


class Monosplit(App):
    """Monosplit primary application."""

    class Meta:
        label = 'monosplit'
        config_defaults = init_defaults('monosplit')
        exit_on_close = True
        extensions = [
            'json',
            'colorlog',
            'jinja2',
        ]
        config_handler = 'json'
        config_file_suffix = '.json'
        log_handler = 'colorlog'
        output_handler = 'jinja2'
        handlers = [
            base.Base,
            git.Git,
            initialize.Initialize
        ]
        ms_config = {
            'config_file_name': 'monosplit',
            'config_file_suffix': '.json',
            'meta_directory': '.monosplit',
        }


class MonosplitTest(TestApp, Monosplit):
    """A sub-class of Monosplit that is better suited for testing."""

    class Meta:
        label = 'monosplit'


def main():
    with Monosplit() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except MonosplitError as e:
            print('MonosplitError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
