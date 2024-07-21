from typer import run

from .src.facade import main


def cli():
    run(main)
