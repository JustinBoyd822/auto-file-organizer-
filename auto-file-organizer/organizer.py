import logging
import os
import shutil
import yaml
from pathlib import Path

# Set up log directory
LOG_DIR = Path(__file__).parent / "log"
LOG_DIR.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_DIR / "run.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Load configuration from YAML
CONFIG_PATH = Path(__file__).parent / "config.yaml"

try:
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print(f" config.yaml not found at {CONFIG_PATH}")
    exit(1)

SOURCE = Path(config.get("source_folder", ""))
FILE_MAP = config.get("file_types", {})

# Organize files
def organize():
    if not SOURCE.exists():
        print(f" Source folder does not exist: {SOURCE}")
        return

    moved = 0
    skipped = 0

    for item in SOURCE.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            folder = FILE_MAP.get(ext)
            if folder:
                target_folder = SOURCE / folder
                target_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(target_folder / item.name))
                logging.info(f"Moved {item.name} → {target_folder}")
                moved += 1
            else:
                logging.warning(f"No mapping for {item.name} ({ext})")
                skipped += 1

    print(f" Organizing complete.")
    print(f"✔ Files moved: {moved}")
    print(f"⚠ Files skipped (no mapping): {skipped}")
    print(f" Log saved to: {LOG_DIR / 'run.log'}")

# Entry point
if __name__ == "__main__":
    organize()

