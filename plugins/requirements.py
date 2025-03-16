import click
import subprocess
import sys

@click.group()
def requirements():
    """Manage dependencies for Minaki plugins."""
    pass

@click.command(name="install")
@click.argument("packages", nargs=-1, required=True)
def install_packages(packages):
    """Install dependencies using pip."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install"] + list(packages), check=True)
        click.echo(f"✅ Installed: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to install: {e}")

@click.command(name="uninstall")
@click.argument("packages", nargs=-1, required=True)
def uninstall_packages(packages):
    """Uninstall dependencies using pip."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y"] + list(packages), check=True)
        click.echo(f"✅ Uninstalled: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to uninstall: {e}")

@click.command(name="list")
def list_packages():
    """List installed Python packages."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "list"], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"⚠️ Failed to list packages: {e}")

# ✅ Register the commands properly
requirements.add_command(install_packages)
requirements.add_command(uninstall_packages)
requirements.add_command(list_packages)

# ✅ Register the plugin inside Minaki CLI
def register_commands(app):
    """Register the requirements plugin into Minaki CLI"""
    app.add_command(requirements)  # Ensures it is correctly loaded
