import configparser

def read_config(config_file):
    """Reads the configuration file and returns a dictionary of values."""
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['ApplicationDetails']