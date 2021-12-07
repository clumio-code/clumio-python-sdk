# Clumio Python SDK

## Overview

The `clumio-python-sdk` Python package provides an object-oriented API which allows developers to
write software using operations which Clumio provides for protecting data. This document provides
information on how to build and use the SDK.

## Requirements

The library requires Python 3.6 and higher. Third-party libraries are also required.

## Installation
```
pip install 'git+https://github.com/clumio-code/clumio-python-sdk.git@<version>#egg=clumioapi'
```

## Quick Start
The following code block explains how to use the clumioapi SDK package.
```
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

```
The REST API documentation describes all the available APIs and can be accessed from the help section in the top right corner of the Clumio UI.