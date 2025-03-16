from minaki.plugins.base import MinakiPlugin

class CommandBlockerPlugin(MinakiPlugin):
    """Prevents execution of dangerous commands."""
    
    def __init__(self):
        super().__init__("Command Blocker", "Prevents execution of dangerous commands")

    def before_command(self, command):
        blocked_commands = ["rm -rf /", "shutdown now", "dd if=/dev/zero"]
        for blocked in blocked_commands:
            if command.strip().startswith(blocked):
                print(f"🚨 BLOCKED: '{command}' is a dangerous command!")
                return None  # Prevent execution
        return command  # Allow execution
