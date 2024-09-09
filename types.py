import yaml
from dataclasses import dataclass
from typing import List

@dataclass
class GlobalSettings:
    outputLanguages: List[str]
    baseOutputDirectory: str
    baseTemplateDirectory: str

@dataclass
class Template:
    name: str
    language: str
    filePath: str
    requiredVars: List[str]

@dataclass
class File:
    name: str
    template: str
    fileNameFormat: str
    vars: dict

@dataclass
class Program:
    name: str
    language: str
    files: List[File]

@dataclass
class Configuration:
    globalSettings: GlobalSettings
    templates: List[Template]
    programs: List[Program]

def deserialize_yaml(yaml_content: str) -> Configuration:
    data = yaml.safe_load(yaml_content)
    return Configuration(**data)
