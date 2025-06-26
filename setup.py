import sys

from setuptools import find_packages
from setuptools import setup

if sys.version_info[0] < 3:
    with open('README.md') as fh:
        long_description = fh.read()
else:
    with open('README.md', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='clumioapi',
    version='SDK_VERSION',
    description='Python SDK for Clumio REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Clumio Inc.',
    author_email='support@clumio.com',
    url='https://clumio.com',
    classfiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(),
    install_requires=[
        'Jinja2>=3.1.4',
        'beautifulsoup4>=4.12.3',
        'html-table-extractor>=1.4.1',
        'texttable>=1.7.0',
        'black>=24.4.2',
        'pyupgrade>=3.16.0',
        'isort>=5.13.2',
        'unify>=0.5',
        'trim>=0.3',
        'Sphinx>=7.3.7',
        'sphinx-autodoc-typehints>=2.2.2',
        'sphinx-material>=0.0.36',
        'PyGithub>=2.6.1',
    ],
)
