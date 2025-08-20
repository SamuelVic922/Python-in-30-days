# Today (20/08/2025) we are building a folder cleaner app
# What it does:
#  - Asks you for a folder path.
# - Creates subfolders like "Images", "Videos", "Docs", etc.
# - Moves files into those subfolders based on their file extension.
# - If a file with the same name already exists, it adds " (1)", " (2)", ... to the name.

from pathlib import Path
import shutil
import sys


GROUPS = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Music":  {".mp3", ".wav", ".flac", ".aac", ".m4a"},
    "Docs":   {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code":   {".py", ".js", ".ts", ".html", ".css", ".json", ".md"},
}


def unique_path(p: Path) -> Path:
    """
    If 'p' exists, add ' (1)', ' (2)', ... until we find a free name.
    Example: report.pdf -> report (1).pdf
    """
    if not p.exists():
        return p

    stem, suffix = p.stem, p.suffix
    counter = 1
    while True:
        candidate = p.with_name(f"{stem} ({counter}){suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def choose_category(ext: str) -> str:
    """
    Return the GROUPS key (like 'Images') that contains this extension.
    If no match is found, return 'Others'.
    """
    ext = ext.lower()
    for name, extensions in GROUPS.items():
        if ext in extensions:
            return name
    return "Others"


def main() -> None:
    # Allow passing the folder as a command-line argument:
    if len(sys.argv) > 1:
        folder_input = " ".join(sys.argv[1:])  # join pieces in case of spaces
    else:
        folder_input = input(
            "Enter the FULL path of the folder to clean: ").strip()

    folder_input = folder_input.strip('"').strip(
        "'")  # remove quotes if pasted

    target = Path(folder_input)

    if not target.exists():
        print("❌ That path does not exist. Please check and try again.")
        sys.exit(1)

    if not target.is_dir():
        print("❌ That path is not a folder. Please give a folder path.")
        sys.exit(1)

    # If the script is run *inside* the folder being cleaned, don't move the script itself.
    try:
        this_script = Path(__file__).resolve()
    except NameError:
        this_script = None

    moved = 0
    skipped = 0

    print(f"🔧 Cleaning: {target}")

    for item in target.iterdir():
        if not item.is_file():
            continue  # ignore subfolders for this beginner version

        if this_script is not None and item.resolve() == this_script:
            skipped += 1
            continue  # don't move me (this script)

        category = choose_category(item.suffix)
        dest_dir = target / category
        dest_dir.mkdir(exist_ok=True)

        destination = dest_dir / item.name
        destination = unique_path(destination)

        shutil.move(str(item), str(destination))
        print(f"➡️  {item.name}  ->  {category}/")
        moved += 1

        print(f"✅ Done! Moved {moved} file(s). Skipped {skipped} item(s).")
    print("Tip: Run again if you add more files. You can edit GROUPS to fit your needs.")


if __name__ == "__main__":
    main()
