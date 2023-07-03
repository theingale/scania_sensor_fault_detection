from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:    
    """
    Returns list of requiremets from requirements.txt file
    """
    requirements_list:List[str] = []
    # with open("requirements.txt", "r") as file:
    #     for item in file:
    #         requirements_list.append(str(item))

    return requirements_list


setup(

    name="sensor",
    version="0.1.0",
    author="saket_ingale",
    author_email="saketvingale4@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)
