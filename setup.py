try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Sample Python Programming Project',
    'author': 'Manuel A. Gama',
    'url': 'https://github.com/mgama/pythonProjects',
    'download_url': 'https://github.com/mgama/pythonProjects.git',
    'author_email': 'mgamamsc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['PythonProgramming'],
    'scripts': [],
    'name': 'pythonprogramming'
}

setup(**config)