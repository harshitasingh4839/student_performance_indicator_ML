from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    Function to read the requirements.txt file and return the list of packages.
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements

setup(
    name="student_performance_prediction",
    version="0.0.1",
    author='Harshita',
    author_email='harshicodeforme@gmail.com',

    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    # ,
    # entry_points={
    #     "console_scripts": [
    #         "your_script_name = your_project.module:main_function",
    #     ],
    # },
)
