import setuptools
from setuptools import find_namespace_packages, setup

def get_install_requirements():    

    with open("requirements.txt", "r", encoding="utf-8") as f:        
        reqs = [x.strip() for x in f.read().splitlines()]    
        reqs = [x for x in reqs if not x.startswith("#")]    
    return reqs


setup(
    name='qdnc',
    description='DQN-based cooling & heating system ',
    author='Ahmed Mabrouk',
    license='BSD-3',
    packages=setuptools.find_namespace_packages(include=['src_dqnc', 'src_dqnc.models','src_dqnc.features', 'src_dqnc.data'] ),
    install_requires= get_install_requirements()
)
