from setuptools import setup
from typing import List


#Declaring variables for setup functions 
PROJECT_NAME="productivity-predictor"
VERSION="0.0.1"
AUTHOR="Praveen Tomar"
DESCRIPTION="Garments Workers Productivity Project"
PACKAGES=["garments"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mention in requirements.txt
    
    Return: This function is going to return a list which will contain name of libraries mentioned
    in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

    
setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)