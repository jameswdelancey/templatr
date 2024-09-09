class PythonFileGenerator:
    def __init__(self, config):
        self.config = config
        self.class_name = config.get("class_name", "GeneratedClass")
        self.properties = config.get("properties", {})
        self.methods = config.get("methods", {})

    def generate_property_code(self, name, type_):
        return f"    {name}: {type_}\n"

    def generate_method_code(self, name, implementation):
        return f"    def {name}(self):\n" + f"{implementation}\n"

    def generate_class_code(self):
        class_header = f"class {self.class_name}:\n"
        class_body = ""

        # Generate properties
        for prop_name, prop_type in self.properties.items():
            class_body += self.generate_property_code(prop_name, prop_type)

        # Generate methods
        for method_name, method_impl in self.methods.items():
            class_body += self.generate_method_code(method_name, method_impl)

        # Add an __init__ method if not provided
        if "__init__" not in self.methods:
            class_body += "    def __init__(self):\n"
            for prop_name, _ in self.properties.items():
                class_body += f"        self.{prop_name} = None\n"

        # Ensure class has at least a pass statement
        if not class_body.strip():
            class_body = "    pass\n"

        return class_header + class_body

    def generate_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(self.generate_class_code())


# Example usage:
if __name__ == "__main__":
    config = {
        "class_name": "MyClass",
        "properties": {"name": "str", "age": "int"},
        "methods": {
            "__init__": "        self.name = 'Unknown'\n        self.age = 0\n",
            "greet": "        print(f'Hello, my name is {self.name} and I am {self.age} years old.')\n",
        },
    }

    generator = PythonFileGenerator(config)
    generator.generate_file("generated_class.py")
