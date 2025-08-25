.. clumio-python-sdk documentation master file, created by
   sphinx-quickstart on Mon Mar 22 13:30:46 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Clumio Python SDK's documentation!
=============================================

.. toctree::
   :maxdepth: 10
   :caption: Contents:

Clumio Python SDK provides an object-oriented API which allows developers to write software using operations which Clumio provides for protecting data. This document provides information on how to build and use the SDK. 

How to Build
------------

You must have Python Python 3 >=3.6 installed on your system to install and run this SDK. This SDK package depends on other Python packages like requests, jsonpickle etc. 
These dependencies are defined in the *requirements.txt* file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at https://pip.pypa.io/en/stable/installing/.

Python and PIP executables should be defined in your PATH. Open command prompt and type ``pip --version``.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

::

pip install 'git+https://github.com/clumio/clumio-python-sdk.git@<version>#egg=clumio-python-sdk'

Quick Start
-----------
The following code block explains how to use the clumioapi SDK package.

.. code-block:: python

   #Start by importing the clumioapi_client and configuration modules from the clumioapi package.
   from clumioapi import configuration, clumioapi_client

   #Create the configuration object by passing in the API Token required for authentication.
   config = configuration.Configuration(api_token=<api_token>, hostname=<hostname>)

   #Create a client instance by passing in the configuration.
   client = clumioapi_client.ClumioAPIClient(config=config)

   #In the client, the available resources are defined as properties which can be accessed and the
   #required operation can be invoked on the resource.
   #For example, in order to list policy definitions use the following:
   policy_defn = client.policy_definitions_v1.list_policy_definitions()

API Reference
=============
* :doc:`Client<client>`
* :doc:`Configuration<configuration>`
* :doc:`Controllers<controllers>`
