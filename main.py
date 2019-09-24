import click
import re

from jinja2 import Template


def validate_var(ctx, param, value):
    for v in value:
        if not re.match(r'^(.+)=(.+)$', v):
            raise click.BadParameter(f'var needs to be of the form var=value (while processing {v})')
    return value


@click.command()
@click.option('--template', '-t', type=click.File('r'), required=True,
             help='Path to the template file')
@click.option('--output', '-o', type=click.File('w'), required=True,
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
