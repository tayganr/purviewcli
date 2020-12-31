import setuptools

setuptools.setup(
      name='purviewcli',
      version='0.1',
      description='Azure Purview Command Line Interface (CLI).',
      url='https://github.com/tayganr/pypurview-cli',
      author='Taygan Rifat',
      author_email='contact@taygan.co',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires = ['docopt','requests','pandas'],
      entry_points={
        'console_scripts': [
            'purviewcli = purviewcli.cli:main'
        ],
    }
)