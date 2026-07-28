from pathlib import Path
import yaml

CONFIG_DIR = Path.home() / ".config" / "rif"
CONFIG_FILE = CONFIG_DIR / "config.yaml"

DEFAULT_CONFIG = {
    "workspace": str(Path.home() / "Projects"),
    "runtime": "docker",
    "editor": "code",
}

def init_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(yaml.safe_dump(DEFAULT_CONFIG))

def load_config():
    return yaml.safe_load(CONFIG_FILE.read_text()) if CONFIG_FILE.exists() else {}
