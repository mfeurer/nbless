import click

from src.nbless.nbconv import nbconv

from src.nbless.helpers.write_file import write_file

@click.command()
@click.argument('in_file')
@click.option('-e', '--exporter', 'exporter')
@click.option('-o', '--out_file', 'out_file')
def nbconv_click(in_file: str, exporter: str, out_file: str) -> None:
    nb_name, nb = nbconv(in_file, exporter)
    write_file(out_file, nb) if out_file else write_file(nb_name, nb)