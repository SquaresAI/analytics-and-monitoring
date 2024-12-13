import os
import json
import yaml

class ConfigParser:
    def __init__(self, config_path):
        """
        Initialize ConfigParser with the given configuration file path.

        Args:
            config_path (str): Path to the configuration file.
        """
        self.config_path = config_path
        self.config = {}

    def load(self):
        """
        Load the configuration file into a dictionary.
        Supports both YAML and JSON formats.

        Raises:
            ValueError: If the file format is unsupported.
        """
        if self.config_path.endswith('.yaml') or self.config_path.endswith('.yml'):
            with open(self.config_path, 'r') as file:
                self.config = yaml.safe_load(file)
        elif self.config_path.endswith('.json'):
            with open(self.config_path, 'r') as file:
                self.config = json.load(file)
        else:
            raise ValueError("Unsupported configuration format. Please use YAML or JSON.")

    def get(self, key, default=None):
        """
        Retrieve a value from the configuration.

        Args:
            key (str): The key to retrieve.
            default (Any): The default value if the key is not found.

        Returns:
            Any: The value associated with the key, or default if not found.
        """
        return self.config.get(key, default)

    def __str__(self):
        return f"ConfigParser({self.config_path})"

# Example utility function
def load_config(path):
    """
    Load a configuration file.

    Args:
        path (str): Path to the configuration file.

    Returns:
        dict: The parsed configuration as a dictionary.
    """
    parser = ConfigParser(path)
    parser.load()
    return parser.config
