import os
import json
from jinja2 import Environment, FileSystemLoader

class CodeGenerator:
    def __init__(self, config):
        self.config = config
        self.env = Environment(loader=FileSystemLoader(config["globalSettings"]["baseTemplateDirectory"]))
    
    def generate_code(self):
        for program in self.config["programs"]:
            for file_config in program["files"]:
                template_name = self.config["templates"][file_config["template"]]['filePath']
                # todo: validate
                file_name = file_config["fileNameFormat"].replace("{{className}}", program["name"])
                output_path = os.path.join(self.config["globalSettings"]["baseOutputDirectory"], file_name)
                self.render_template(template_name, file_config["vars"], output_path)
    
    def render_template(self, template_name, vars, output_path):
        template = self.env.get_template(template_name)
        rendered_content = template.render(vars)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # with open(output_path, 'w') as f:
            # f.write(rendered_content)
        print(rendered_content)

if __name__ == "__main__":
    config = {
        # ... (The provided dictionary goes here)
    }
    generator = CodeGenerator(config)
    generator.generate_code()
