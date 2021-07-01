import os
import json
from jschon import Catalogue, JSON, JSONSchema


def get_config(path):
    data = {}

    try:
        data = json.loads(JSON.loadf(path).__str__())
    except Exception:
        pass

    return data


def scan_project(name, path=".", configs=[]):
    if has_config(name, path):
        configs.append(os.path.join(path, name))

    entries = os.scandir(path)

    for entry in entries:
        if entry.is_dir():
            scan_project(name, entry, configs)

    return configs


def has_config(name, path="."):
    return os.path.exists(os.path.join(path, name))


def validate_config_schema(config={}, path=""):
    if len(path) > 0:
        config = get_config(path)

    if len(config) <= 0: return {'valid': False}

    try:
        Catalogue.create_default_catalogue('2020-12')
    except Exception:
        pass

    schema = JSONSchema({
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "properties": {
            "repository": {"$ref": "#/$defs/repositoryDefinition"},
            "branch": {"$ref": "#/$defs/branchDefinition"}
        },
        "required": ["repository"],
        "$defs": {
            "repositoryDefinition": {
                "type": "string",
            },
            "branchDefinition": {
                "type": "string"
            }
        }
    })

    return schema.evaluate(JSON(config)).output('flag')
