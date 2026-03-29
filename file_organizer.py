from pathlib import Path
import json, datetime, shutil, logging, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

def handle_file(path):
    file = Path(path)

    if not file.exists() or not file.is_file():
        return

    for folder, extensions in file_types.items():
        if file.suffix.lower() in extensions:

            dest = dest_base / folder
            dest.mkdir(exist_ok=True)

            dest_file = dest / folder

            counter = 1
            while dest_file.exists():
                dest_file = dest / f"{file.stem}_{counter}{file.suffix}"
                counter+=1


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

class WatchHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)
            handle_file(event.src_path)

if __name__ == "__main__":
    observer = Observer()
    event_handler = WatchHandler()

    observer.schedule(event_handler, path=str(src), recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
