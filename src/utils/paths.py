from pathlib import Path
import yaml

def get_base_dir(format='Path'):
    base_dir = Path(__file__).resolve().parents[2]
    if base_dir.name != 'MrktMove':
        raise RuntimeError('Please run from MrkMove root directory!')
    elif format == 'Path':
        return base_dir
    elif format == 'str':
        return str( base_dir )

def get_config_path(format='Path'):
    config_path = get_base_dir() / 'config.py'

    if format == 'Path':
        return config_path
    elif format == 'str':
        return str( config_path )