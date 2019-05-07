from setuptools import setup, find_packages
import pypcgc.__version__


NAME = 'pypcgc'
DESCRIPTION = 'Python package creater tool'
URL = 'https://github.com/pypcgc/cli-tool'
EMAIL = '0radimkozak0@gmail.com'
AUTHOR = 'worepix'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = pypcgc.__version__.__version__
LICENSE = 'MIT'
CLASSIFIERS = [
        'Programming Language :: Python'
    ]
CONSOLE_SCRIPTS = ['pypcgc=pypcgc:main']


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    }
)
