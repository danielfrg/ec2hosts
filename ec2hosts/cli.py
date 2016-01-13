from __future__ import print_function, absolute_import, division

import sys
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


import ec2hosts


def main():
    try:
        cli(obj={})
    except Exception as e:
        import traceback
        click.echo(traceback.format_exc(), err=True)
        sys.exit(1)


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.version_option(prog_name='Anaconda Cluster', version=ec2hosts.__version__)
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    if ctx.invoked_subcommand is None:
        ctx.invoke(run)


@cli.command(short_help='Run')
@click.pass_context
def run(ctx):
    click.echo("New /etc/hosts file:")
    content = ec2hosts.gen_file()
    click.echo(content)
    if click.confirm('Do you want to continue?'):
        ec2hosts.write(content)
        ec2hosts.move()


@cli.command(short_help='Clean')
@click.pass_context
def clean(ctx):
    click.echo("New /etc/hosts file:")
    content = ec2hosts.read_file()
    content = ec2hosts.clean(ec2hosts.read_file())
    click.echo(content)
    if click.confirm('Do you want to continue?'):
        ec2hosts.write(content)
        ec2hosts.move()
