import json

import click

from genie.commands import available_commands, unformat_command
from genie.commands import base64_decode_command
from genie.commands import base64_encode_command
from genie.commands import format_json_command
from genie.commands import minify_json_command


@click.group()
def cli():
    pass


@cli.command()
@click.argument("parameters", nargs=-1)
def commands(parameters):
    args = parameters[0].strip() if parameters else ""
    commands_metadata = [c.metadata(args) for c in available_commands]
    if args:
        commands_metadata = [
            c for c in commands_metadata if args in c.get("title").lower()
        ]
    commands_json = json.dumps(dict(items=commands_metadata))
    click.echo(commands_json, nl=False)


@cli.command()
def format_json():
    result = format_json_command.process()
    click.echo(result, nl=False)


@cli.command()
def minify_json():
    result = minify_json_command.process()
    click.echo(result, nl=False)


@cli.command()
def base64_decode():
    result = base64_decode_command.process()
    click.echo(result, nl=False)


@cli.command()
def base64_encode():
    result = base64_encode_command.process()
    click.echo(result, nl=False)


@cli.command()
def unformat():
    result = unformat_command.process()
    click.echo(result, nl=False)
