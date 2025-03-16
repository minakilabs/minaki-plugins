import click

@click.command(name="example")  # Change command name to 'example'
def example():
    """Example plugin command"""
    click.echo("Hello from Minaki Plugin!")

def register_commands(cli):
    cli.add_command(example)  # Register it as 'example'x
