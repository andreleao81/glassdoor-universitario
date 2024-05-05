import json
from collections import OrderedDict



def create_path_object(path, method, tags, description, schema_ref, response_description, response_code=201):
    path_object = {
        path: {
            method: {
                "tags": tags,
                "description": description,
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": schema_ref
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    str(response_code): {
                        "description": response_description,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": schema_ref
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return path_object

# Usage
path_object = create_path_object(
    "/user", 
    "post", 
    ["User"], 
    "Creates a new user", 
    "#/components/schemas/User", 
    "User created"
)

# Add to existing paths
with open('openapi.json', 'r+') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    data['paths'].update(path_object)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()