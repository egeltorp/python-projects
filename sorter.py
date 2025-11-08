'''
1. Run the script in the terminal (python sorter.py)
2. Ctrl + C to stop

The script will automatically move and sort the files in the Downloads folder to 
the /sorted folder and then relevant subfolder
'''

import os
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS = Path.home() / "Downloads"
SORTED_DIR = DOWNLOADS / "sorted"

FILE_CATEGORIES = {
	"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
	"Documents": [".pdf", ".docx", ".txt", ".md", ".pptx", ".xlsx"],
	"Audio": [".mp3", ".wav", ".flac", ".m4a"],
	"Video": [".mp4", ".mov", ".avi", ".mkv"],
	"Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def get_destination_folder(ext):
	for category, exts in FILE_CATEGORIES.items():
		if ext in exts:
			return SORTED_DIR / category
	return SORTED_DIR / "Other"

def create_category_folders():
	SORTED_DIR.mkdir(exist_ok=True)
	for category in FILE_CATEGORIES.keys():
		(SORTED_DIR / category).mkdir(parents=True, exist_ok=True)
	(SORTED_DIR / "Other").mkdir(parents=True, exist_ok=True)
	(SORTED_DIR / "Folders").mkdir(parents=True, exist_ok=True)

def move_item(src_path: Path):
	if src_path.is_dir():
		dest_dir = SORTED_DIR / "Folders"
	else:
		dest_dir = get_destination_folder(src_path.suffix.lower())
	dest_dir.mkdir(parents=True, exist_ok=True)
	dest_path = dest_dir / src_path.name

	# Avoid overwriting duplicates
	if dest_path.exists():
		base, ext = os.path.splitext(src_path.name)
		dest_path = dest_dir / f"{base}_copy{ext}"

	shutil.move(str(src_path), dest_path)
	print(f"Moved: {src_path.name} → {dest_dir.name}")

def sort_existing_items():
	for item in DOWNLOADS.iterdir():
		if item.name == "sorted":
			continue
		move_item(item)

class SortHandler(FileSystemEventHandler):
	def on_created(self, event):
		src_path = Path(event.src_path)
		if src_path.name == "sorted":
			return
		create_category_folders()
		move_item(src_path)

if __name__ == "__main__":
	create_category_folders()
	sort_existing_items()

	event_handler = SortHandler()
	observer = Observer()
	observer.schedule(event_handler, str(DOWNLOADS), recursive=False)
	observer.start()
	print("Watching Downloads folder... Press Ctrl+C to stop.")
	try:
		while True:
			pass
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

