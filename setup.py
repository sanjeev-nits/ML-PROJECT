from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requrements(file_path:str)->list[str]:
    
    """
    this function will return the list of requirements
    """
    requirements=[]
    
    with open(file_path) as file_obj:  
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

    
    
    
setup(
    name='mlproject',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='Sanjeev',
    author_email="sanjeevkumar814155@gmail.com",
    install_requires=get_requrements('requirements.txt')
)