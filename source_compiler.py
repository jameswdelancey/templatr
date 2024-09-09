import argparse
from typing import NamedTuple

import yaml
from jinja2 import Environment, FileSystemLoader

# Define the CLI arguments
parser = argparse.ArgumentParser(
    description="Generate source code from Jinja templates and YAML input."
)
parser.add_argument("template", help="Path to the Jinja template file.")
parser.add_argument("variables", help="Path to the YAML file containing variables.")
parser.add_argument("output", help="Path to the output source code file.")
args = parser.parse_args()

# Load variables from the YAML file
with open(args.variables, "r") as yaml_file:
    variables = yaml.safe_load(yaml_file)
# Load the Jinja template
env = Environment(loader=FileSystemLoader(searchpath="./"))
template = env.get_template(args.template)

# Generate the source code
source_code = template.render(variables)

# Write the source code to the output file
with open(args.output, "w") as output_file:
    output_file.write(source_code)
