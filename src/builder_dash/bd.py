import os

from slim.file_tools import read_json_file

from .license_mit import license_mit
from .readme_rst import readme_rst
from .setup_cfg import setup_cfg
from .setup_py import setup_py

slim_folder: str = f'{os.path.expanduser("~")}/slim/projects'
root_folder: str = f'{os.path.expanduser("~")}/Project'
organisation: str = 'tsvenson'

project_data = read_json_file(f'{slim_folder}/scb_tools.json')


def machine_name(project_name: str) -> str:
    name_temp = project_name.lower()
    result = name_temp.replace(' ', '_')
    return result


def make_file(path: str, content: str = '') -> None:
    with open(path, 'w') as f:
        f.write(content)


def main() -> None:
    project_root = f'{root_folder}/{organisation}'
    project_name = machine_name(project_data["name"])
    project_path = f'{project_root}/{project_name}'

    if not os.path.exists(f'{project_path}'):
        os.makedirs(f'{project_path}')
        os.makedirs(f'{project_path}/src/{project_name}')
        make_file(f'{project_path}/src/{project_name}/__init__.py')
        os.makedirs(f'{project_path}/tests')
        make_file(f'{project_path}/tests/__init__.py')
        make_file(f'{project_path}/LICENSE',
                  license_mit(project_data['year_started'], project_data['author']))
        make_file(f'{project_path}/README.rst', readme_rst(project_data))
        make_file(f'{project_path}/setup.cfg', setup_cfg(project_data, project_name))
        make_file(f'{project_path}/setup.py', setup_py())
        print(f'Project {project_name} created.')
    else:
        print(f'Project "{project_path}" already exists!')


def main2() -> None:
    print(project_data)


if __name__ == '__main__':
    main()
