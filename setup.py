from setuptools import find_packages, setup

def get_requirements(file_path):
    """
    Reads the requirements from a given file and returns them as a list.
    """
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kalpesh-Rajput',
    author_email='kr342803@gmail.com',
    packages=find_packages(),  # Automatically find packages
    install_requires=get_requirements('requirements.txt')
)
