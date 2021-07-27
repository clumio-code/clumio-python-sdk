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
    version='0.1.0',
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
        'requests>=2.9.1',
        'jsonpickle>=0.7.1',
        'cachecontrol>=0.11.7',
        'python-dateutil>=2.5.3',
        'urllib3>=1.26.3',
        'rest3client>=0.3.3',
    ],
)