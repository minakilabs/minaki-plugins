# 🚀 Minaki Plugins

**Minaki Plugins** is a collection of modular plugins for the **Minaki CLI**, allowing users to extend functionality with **authentication, logging, security**, and more. This repository serves as the **official plugin hub** for Minaki CLI.

🔌 **Features**:
- **Extend Minaki CLI** dynamically with plugins
- **Easy installation**: Install new plugins with `minaki plugin install <plugin>`
- **Authentication Ready** (Coming soon)
- **Modular & Lightweight**

---

## 📦 Installation

First, install the **Minaki CLI**:

```sh
pip install minaki-cli

Then, install a plugin:

minaki plugin install hello

Check installed plugins:

minaki plugin list

Run a plugin:

minaki app hello

🔧 Plugin Development

Want to build your own plugin? Create a new .py file inside the plugins/ directory.

Example plugin (hello.py):

import click

@click.command()
def hello():
    """Example plugin command"""
    click.echo("Hello from Minaki Plugin!")

def register_commands(cli):
    cli.add_command(hello)

📢 Contributing

🔹 Want to add your own plugins? Fork this repo and submit a PR!
🔹 Found a bug? Open an issue!

📜 License

MIT License – You are free to use, modify, and distribute Minaki Plugins.

📢 Stay updated: Follow Minaki Labs for future releases!
