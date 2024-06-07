from setuptools import setup, find_packages

setup(
    name='pycon_demo_library_python',
    description='Util functions for PyCon demo library',
    version='0.9.9',
    url='https://andresrestrepo.github.io/portfolio_team/',
    author='AFC',
    author_email='andresfelipe25@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['json-logging>=1.3.0']
)
