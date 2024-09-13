import argparse
import subprocess
import sys
from pathlib import Path

from black import FileMode, WriteBack, format_file_in_place


def run_isort(file_path: Path):
    subprocess.run(["isort", str(file_path)])


def remove_first_last_char(file_path: Path):
    if file_path.is_file():
        with open(file_path, "r", encoding="utf-16-le") as file:
            content = file.read()
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content[1:-1])


def main():
    parser = argparse.ArgumentParser(
        description="Run black on a file and output to another file."
    )
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    remove_first_last_char(input_path)

    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        sys.exit(1)

    try:
        run_isort(input_path)
        format_file_in_place(
            src=input_path,
            mode=FileMode(),
            fast=False,
            write_back=WriteBack.YES,
        )
        output_path.unlink(missing_ok=True)
        input_path.rename(output_path)
        print(f"File formatted successfully and written to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
