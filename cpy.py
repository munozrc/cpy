import argparse

def cli():
    parser = argparse.ArgumentParser(
        prog="cp",
        description="cp command implementation in Python",
    )
    parser.add_argument(
        "source",
        help="Source directory or file"
    )
    parser.add_argument(
        "destination",
        help="Destination directory or file"
    )
    return parser.parse_args()

def main():
    args = cli()
    print(args)
    
if __name__ == "__main__":
    main()
