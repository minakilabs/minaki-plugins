class HelloWorldPlugin:
    """A simple Hello World plugin for Minaki."""
    
    def before_command(self, command):
        print("🌍 Hello from the Hello World Plugin!")
        return command

    def after_command(self, command, output):
        return output  # No changes to the command output

    def register_commands(self, cli):
        """Register additional CLI commands."""
        @cli.command()
        def hello():
            """Prints Hello from Minaki."""
            print("👋 Hello from Minaki!")

plugin = HelloWorldPlugin()
