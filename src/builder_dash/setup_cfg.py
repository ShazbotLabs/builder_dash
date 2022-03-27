def setup_cfg(config_data: dict, project_name: str):
    content = f"""[metadata]
name = {project_name}
version = {config_data['version']}
url = {config_data['url']}
author = {config_data['author']}
author_email = {config_data['author_email']}
license = {config_data['license']}
description = {config_data['description']}
long_description = {config_data['long_description']}
classifiers =
"""
    for item in config_data['classifiers']:
        content += f'    {item}\n'

    content += f"""
[options]
packages = {project_name}
"""
    return content
