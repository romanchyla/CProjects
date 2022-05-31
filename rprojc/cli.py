import click

try:
    import rutils as utils

    config = utils.load_config()
    logger = utils.setup_logging("rprojc.cli")
except ImportError:
    import logging

    config = {}
    logger = logging.getLogger("rprojc.cli")


@click.group()
def cli():
    pass


@cli.command()
def hello():
    """Will greet"""
    print("Hello World!")


if __name__ == "__main__":
    cli()
