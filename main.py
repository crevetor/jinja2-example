import click
import re

from jinja2 import Template


def validate_var(ctx, param, value):
    if not re.match(r'^(.+)=(.+)$', str(value)):
        raise click.BadParameter('var needs to be of the form var=value')
    return value


@click.command()
@click.option('--template', '-t', type=click.File('r'),
             help='Path to the template file')
@click.option('--output', '-o', type=click.File('w'),
              help='Path to the output file')
@click.option('--var', '-v', multiple=True, type=str, callback=validate_var,
              help='Variable in the form var=value, can be specified multiple times')
def main(template, output, var):
    var_dict = {}
    for v in var:
        name, val = v.split('=')
        var_dict[name] = val

    tpl = Template(template.read())
    output.write(tpl.render(**var_dict))
    output.close()

if __name__ == "__main__":
    main()
