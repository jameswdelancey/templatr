import argparse
import json
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="A CLI tool with JSON config reader")
    parser.add_argument(
        "-c", "--config", type=str, required=False, help="Path to the JSON config file", default="config.json"
    )
    return parser.parse_args()


def read_config(config_path):
    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print(f"Error: The config file {config_path} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The config file {config_path} contains invalid JSON.")
        sys.exit(1)
    return config


def main():
    args = parse_args()
    config = read_config(args.config)

    from templatr import CodeGenerator
    CodeGenerator(config).generate_code()


if __name__ == "__main__":
    main()
