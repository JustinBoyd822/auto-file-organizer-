import logging
import os
import shutil
import yaml
from pathlib import Path

os.makedirs("log", exist_ok=True)

logging.basicConfig(
    filename='log/run.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

try:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("config.yaml not found.")
    exit()

SOURCE = Path(config.get("source_folder", ""))
FILE_MAP = config.get("file_types", {})


def organize():
    if not SOURCE.exists():
        print(f"Source folder does not exist: {SOURCE}")
        return

    for item in SOURCE.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            folder = FILE_MAP.get(ext)
            if folder:
                target_folder = SOURCE / folder
                target_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(target_folder / item.name))
                logging.info(f"Moved {item.name} → {target_folder}")
            else:
                logging.warning(f"No mapping for {item.name} ({ext})")


if __name__ == "__main__":
    organize()
    print("Organizing complete. Check log/run.log for details.")
