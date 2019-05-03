import sys
import os
import click
from . import pattern
from . import config


VARIABLES = ["NAME", "DESCRIPTION", "URL", "EMAIL", "AUTHOR", "REQUIRES_PYTHON", "VERSION", "PROJECT_LICENSE", "CLASSIFIERS"]


@click.group()
@click.pass_context
def cli(some=None):
    pass

@cli.command("init", help="Download and initialize pattern")
@click.option("--name", "-n", help="Enter package name", required=True)
@click.option("--custom", "-c", help="Custom pattern")
@click.option("--email", "-e", help="Email")
@click.option("--author", "-a", help="Author name")
@click.option("--version", "-v", help="Version")
@click.option("--required_python", "-rp", help="Python version required")
@click.option("--project_license", "-l", help="License")
def init(name, custom, email, author, version, required_python, project_license):
    if custom:
        pattern.download(custom)

    else:
        pattern.download("https://github.com/pypcgc/pattern.git")

    config_params = {}

    if config.exists():
        config_params = config.read()

    config_params["name"] = name

    if email:
        config_params["email"] = email

    if author:
        config_params["author"] = author

    if version:
        config_params["version"] = version

    if required_python:
        config_params["required_python"] = required_python

    if project_license:
        config_params["config_params"] = project_license

    os.rename("{{NAME}}", name)

    setup_lines = open("setup.py").read()

    for param in config_params.keys():
        setup_lines = setup_lines.replace("{{" + param.upper() + "}}", config_params.get(param))

    open("setup.py", "w").write(setup_lines)




@cli.command("set", help="Set default values to not write them repeatedly")
@click.option("--email", "-e", help="Set default email")
@click.option("--author", "-a", help="Set default author name")
@click.option("--version", "-v", help="Set default version")
@click.option("--required_python", "-rp", help="Set default python version required")
@click.option("--project_license", "-l", help="Set default license")
@click.option("--default_pattern", "-p", help="Set default pattern git repository")
def set(email, author, version, required_python, project_license, default_pattern):
    if email:
        config.write("email={0}".format(email))

    if author:
        config.write("author={0}".format(author))

    if version:
        config.write("version={0}".format(version))

    if required_python:
        config.write("required_python={0}".format(required_python))

    if project_license:
        config.write("project_license={0}".format(default_pattern))

def main():
    try:
        cli()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        click.echo("Exited with {0}".format(e))
        sys.exit(1)
