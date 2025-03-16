import json
import os

PLUGIN_CONFIG_FILE = os.path.expanduser("~/.minaki_plugins.json")

def load_plugin_config():
    """Load the user's enabled plugins from a config file."""
    if not os.path.exists(PLUGIN_CONFIG_FILE):
        return []  # No plugins enabled by default
    with open(PLUGIN_CONFIG_FILE, "r") as f:
        return json.load(f)

def save_plugin_config(plugins):
    """Save the user's enabled plugins to a config file."""
    with open(PLUGIN_CONFIG_FILE, "w") as f:
        json.dump(plugins, f, indent=4)

def enable_plugin(plugin_name):
    """Enable a plugin by adding it to the config."""
    plugins = load_plugin_config()
    if plugin_name not in plugins:
        plugins.append(plugin_name)
        save_plugin_config(plugins)
        print(f"✅ Plugin '{plugin_name}' enabled.")
    else:
        print(f"⚠️ Plugin '{plugin_name}' is already enabled.")

def disable_plugin(plugin_name):
    """Disable a plugin by removing it from the config."""
    plugins = load_plugin_config()
    if plugin_name in plugins:
        plugins.remove(plugin_name)
        save_plugin_config(plugins)
        print(f"❌ Plugin '{plugin_name}' disabled.")
    else:
        print(f"⚠️ Plugin '{plugin_name}' is not enabled.")

def list_enabled_plugins():
    """List currently enabled plugins."""
    plugins = load_plugin_config()
    if plugins:
        print("📦 Enabled Plugins:")
        for plugin in plugins:
            print(f" - {plugin}")
    else:
        print("⚠️ No plugins enabled.")
