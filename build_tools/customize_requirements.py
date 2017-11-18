import os
import tempfile

import requests


def add_requirements_to_base():
    if "EXTRA_REQUIREMENTS" in os.environ:
        file_path = os.environ["EXTRA_REQUIREMENTS"]
        # We have been passed a URL, not a local file path
        if file_path.startswith('http'):
            _, path = tempfile.mkstemp(suffix=".txt", text=True)
            with open(path, 'w') as f:
                r = requests.get(file_path)
                f.write(r.content)
            file_path = path
        with open(file_path, 'r') as f:
            requirements = [requirement.strip() for requirement in f.readlines() if requirement.strip()]
        if requirements:
            with open(os.path.join(os.path.dirname(__file__), '../requirements/base.txt'), 'a') as f:
                f.writelines(requirements)


if __name__ == "__main__":
    add_requirements_to_base()