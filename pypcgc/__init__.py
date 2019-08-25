import sys
import os
import click
from . import pattern
from . import config
from . import __version__

cnf = config.Config()

@click.group()
@click.version_option(version=__version__.__version__)
@click.pass_context
def cli(some=None):
    pass

@cli.command('init', help='Download and initialize pattern')
@click.option('--name', '-n', help='Enter package name', required=True)
@click.option('--custom', '-c', help='Custom pattern')
@click.option('--email', '-e', help='Email')
@click.option('--author', '-a', help='Author name')
@click.option('--version', '-v', help='Version')
@click.option('--requires_python', '-rp', help='Python version required')
@click.option('--project_license', '-l', help='License')
def init(name, custom, email, author, version, requires_python, project_license):
    if custom:
        pattern.download(custom)

    else:
        pattern.download('https://github.com/pypcgc/pattern.git')

    if cnf.exist:
        config_params = cnf.read()

    if email:
        config_params['author']['email'] = email

    if author:
        config_params['author']['name'] = author

    if version:
        config_params['project']['version'] = version

    if requires_python:
        config_params['project']['requires_python'] = requires_python

    if project_license:
        config_params['project']['license'] = project_license

    os.rename('{{PROJECT}}', name)

    setup_lines = open('setup.py').read()

    for group in config_params.keys():
        for attribute in config_params[group]:
            setup_lines = setup_lines.replace('{{' + attribute.upper() + '}}',
                                              config_params[group].get(attribute))

    setup_lines = setup_lines.replace('{{PROJECT}}', name)

    open('setup.py', 'w').write(setup_lines)

@cli.command('set', help='Set default values to not write them repeatedly')
@click.option('--email', '-e', help='Set default email')
@click.option('--author', '-a', help='Set default author name')
@click.option('--version', '-v', help='Set default version')
@click.option('--requires_python', '-rp', help='Set default python version required')
@click.option('--project_license', '-l', help='Set default license')
def set_config(email, author, version, requires_python, project_license):
    if email:
        cnf.set_to_config('author', 'email', email)

    if author:
        cnf.set_to_config('author', 'name', author)

    if version:
        cnf.set_to_config('project', 'version', version)

    if requires_python:
        cnf.set_to_config('project', 'requires_python', requires_python)

    if project_license:
        cnf.set_to_config('project', 'license', project_license)

    cnf.write()

def main():
    try:
        cli()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        click.secho('Exited with {0}'.format(e), fg='red')
        sys.exit(1)
