import yaml
import os

def load_config(config_path="config.yaml"):
    """
    Loads YAML config and overrides with environment variables if present.
    Useful for Docker deployments where secrets shouldn't be in the YAML.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Environment overrides
    config['network']['alert_endpoint'] = os.getenv('ALERT_ENDPOINT', config['network'].get('alert_endpoint'))
    config['camera']['source'] = os.getenv('CAMERA_SOURCE', config['camera'].get('source', 0))
    
    return config
