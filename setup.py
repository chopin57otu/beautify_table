import os

from setuptools import Extension, find_packages, setup

ROOT = os.path.dirname(__file__)

setup(
    name='beautify_table',
    packages=find_packages(exclude=["test*"]),
    version=open(os.path.join(ROOT, 'version.txt')).read().strip(),
    license='MIT',
    author='57_OTU_Chopin, romanzdk',
    author_email='stranma5@gmail.com, romanzdk@gmail.com',
    description='Cleaning data tables from parsed documents.'
)