class MinakiPlugin:
    """Base class for all Minaki plugins."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def before_command(self, command):
        """Modify or validate a command before execution."""
        return command  # Default: No changes

    def after_command(self, command, output):
        """Modify or log the output after execution."""
        return output  # Default: No changes
