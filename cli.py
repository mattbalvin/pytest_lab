#!/usr/bin/env python

import click
from libpoc.poc import simple_function

@click.command()
@click.option('--name', prompt='Your name',
              help='A test parameter.')
def poc(name):
    click.echo(simple_function( name ))

if __name__ == '__main__':
    poc() # pylint: disable=no-value-for-parameter
