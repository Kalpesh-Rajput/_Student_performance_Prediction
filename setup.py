from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of packages.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present in the requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Student_performance_pred',  # The name of your project
    version='0.0.1',  # Version of the project
    author='Kalpesh-Rajput',  # Your name or organization name
    author_email='kr342803@gmail.com',  # Your contact email
    description='A machine learning project to predict student performance',
    packages=find_packages(),  # Automatically find and include all packages (subdirectories with __init__.py)
    install_requires=get_requirements('requirements.txt'),  # Install dependencies from requirements.txt
)
