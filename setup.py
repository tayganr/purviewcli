import setuptools
from os import path
from purviewcli import __version__

# Read the contents of README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='purviewcli',
    version=__version__,
    description="This package provides a command line interface to Azure Purview's REST API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tayganr/purviewcli',
    author='Taygan Rifat',
    author_email='contact@taygan.co',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires = ['docopt','requests','azure-identity'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pv = purviewcli.cli.cli:main'
        ],
    }
)