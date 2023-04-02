import setuptools
from setuptools import find_packages, setup


setup(
    name='qdnc',
    description='DQN-based cooling & heating system ',
    author='Ahmed Mabrouk',
    license='BSD-3',
    packages=setuptools.find_packages(include=['src', 'src.models','src.features', 'src.data'] ),
)
