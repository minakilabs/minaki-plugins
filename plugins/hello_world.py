import click

@click.command(name="hello_world")
def hello_world():
    """Prints Hello from Minaki."""
    click.echo("👋 Hello from Minaki!")

def register_commands(cli):
    """Register the 'hello_world' command inside Minaki CLI."""
    cli.add_command(hello_world)
