# setup.py
from setuptools import setup, find_packages

setup(
    name="your-project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Django==3.2',  # or your version
    ],
    python_requires='>=3.7',
)
