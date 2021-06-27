import argparse
from pathlib import Path
from sys import stderr

class CpError(Exception):
    pass

def copy_directory(src: Path, dest: Path):
    print("cp directory")

def copy_file(src: Path, dest: Path):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file():
        raise CpError(f"Cannot override {dest}")
    print("Ok.")

def copy(src: Path, dest: Path):
    if src.is_file():
        copy_file(src, dest)
    elif src.is_dir():
        copy_directory(src, dest)
    else:
        raise CpError("File type not supported.")

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cp",
        description="cp command implementation in Python.",
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Source directory or file."
    )
    parser.add_argument(
        "destination",
        type=Path,
        help="Destination directory or file."
    )
    return parser.parse_args()

def main():
    args = cli()
    try:
        copy(args.source, args.destination)
    except CpError as e:
        print(e, file=stderr)
        exit(1)
        
if __name__ == "__main__":
    main()
