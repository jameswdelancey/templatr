import argparse
import os

import yaml
from jinja2 import Environment, FileSystemLoader


class TemplateConfig(NamedTuple):
    template: str
    variables: str
    output: str


def load_config(config_path):
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)


def generate_code(template_config):
    env = Environment(loader=FileSystemLoader(searchpath="./"))
    template = env.get_template(template_config.template)
    with open(template_config.variables, "r") as yaml_file:
        variables = yaml.safe_load(yaml_file)
    source_code = template.render(variables)
    os.makedirs(os.path.dirname(template_config.output), exist_ok=True)
    with open(template_config.output, "w") as output_file:
        output_file.write(source_code)


def main(config_path, project=None, file=None):
    config = load_config(config_path)
    for project_name, project_config in config.items():
        if project and project_name != project:
            continue
        for file_config in project_config:
            if file and file_config["output"] != file:
                continue
            template_config = TemplateConfig(**file_config)
            generate_code(template_config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate source code from Jinja templates and YAML input for multiple projects."
    )
    parser.add_argument("config", help="Path to the YAML configuration file.")
    parser.add_argument(
        "--project",
        help="Optional: Specify a single project to generate.",
        default=None,
    )
    parser.add_argument(
        "--file",
        help="Optional: Specify a single file/class to generate.",
        default=None,
    )
    args = parser.parse_args()
    main(args.config, args.project, args.file)
