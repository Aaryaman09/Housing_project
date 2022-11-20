from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.3'
AUTHOR = 'AARYAMAN_SHARMA'
DESCRIPTION = 'THIS IS THE FIRST PROJECT'
# PACKAGES =  ["housing"]
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement mention in requirements.txt file

    This function returns a list which contains name of libraries mentioned requirements.tt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author = AUTHOR,
    description=DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)
