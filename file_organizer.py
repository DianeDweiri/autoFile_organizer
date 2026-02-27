import json
from pathlib import Path
import logging
import shutil
import datetime

config_path = Path(__file__).parent / "config.json"

with open(config_path, "r") as f:
    config = json.load(f)


log_file = Path.home() / "automation.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

home= Path.home()

src = home / config["source_folder"]
dest_base = home / config["destination_folder"]
dest_base.mkdir(exist_ok=True)

file_types = config["file_types"]

def organizer():
    logging.info("Organizer started")

    counters = {k: 0 for k in file_types}
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for folder, extensions in file_types.items():
        dest = dest_base / folder
        dest.mkdir(exist_ok=True)

        for ext in extensions:
            for file in src.glob(f"*{ext}"):
                try:
                    if file.is_file():
                        shutil.move(str(file), str(dest))
                        counters[folder] += 1
                        logging.info(f"Moved {file.name} → {dest} at {now}")

                except Exception as e:
                    logging.error(f"{file.name} : {e}")

    for k, v in counters.items():
        logging.info(f"{k}: {v} files moved")

    logging.info("Organizer finished\n")


if __name__ == "__main__":
    organizer()
    print("Files organized successfully")
