import click

@click.command()
def hello():
    """Example plugin command"""
    click.echo("Hello from Minaki Plugin!")

def register_commands(cli):
    cli.add_command(hello)

