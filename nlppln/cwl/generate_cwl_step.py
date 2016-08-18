#!/usr/bin/env python
import click
import os
import codecs

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('nlppln', 'templates'))


@click.command()
@click.option('--cname', prompt='Command name', default='command')
@click.option('--oid', prompt='Output id', default='out_files')
@click.option('--ob', prompt='Output binding', default='*.json')
@click.option('--out_file', type=click.Path(), prompt='Output file',
              default='./cwl/steps/command.cwl')
def command(cname, oid, ob, out_file):
    """Generate a cwl file that specifies an nlppln processing step.
    """
    output_dir = os.path.dirname(out_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    template = env.get_template('inputs-to-outputs.cwl')
    r = template.render(command_name=cname, output_id=oid, output_binding=ob)

    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        f.write(r)
        f.write('\n')


if __name__ == '__main__':
    command()
