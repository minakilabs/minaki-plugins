import click
import subprocess
import sys

@click.group()
def requirements():
    """Manage dependencies for Minaki plugins."""
    pass

@click.command()
@click.argument("packages", nargs=-1)
def install(packages):
    """Install dependencies using pip."""
    if not packages:
        click.echo("❌ No package specified. Use: minaki requirements install <package>")
        return
    try:
        subprocess.run([sys.executable, "-m", "pip", "install"] + list(packages), check=True)
        click.echo(f"✅ Installed: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to install: {e}")

@click.command()
@click.argument("packages", nargs=-1)
def uninstall(packages):
    """Uninstall dependencies using pip."""
    if not packages:
        click.echo("❌ No package specified. Use: minaki requirements uninstall <package>")
        return
    try:
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y"] + list(packages), check=True)
        click.echo(f"✅ Uninstalled: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to uninstall: {e}")

@click.command()
def list():
    """List installed Python packages."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "list"])
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to list packages: {e}")

# Register plugin
def register_commands(cli):
    cli.add_command(requirements)
    requirements.add_command(install)
    requirements.add_command(uninstall)
    requirements.add_command(list)x
