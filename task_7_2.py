import yaml
import os

with open('config.yaml') as f:
    templates = yaml.safe_load(f)


def create_dir(value, prefix=""):
    for directory, paths in value.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_dir(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_dir(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f"{i}"), "w") as file:
                        file.write("")


create_dir(templates)
