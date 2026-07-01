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

## Filtering
List operations accept a `filter` argument. Pass a plain `dict` exactly as the
filter appears in the REST API reference — snake_case field names and
`$`-prefixed operators — so a filter can be copied straight from the docs:
```
   #List S3 protection-group assets, copied 1:1 from the API reference.
   assets = client.protection_groups_s3_assets_v1.list_protection_group_s3_assets(
       filter={'aws_region': {'$eq': 'us-west-2'}, 'bucket_name': {'$contains': 'logs'}},
   )
```
Each operation also generates a `...FilterTypeDef` TypedDict (for example
`ListProtectionGroupS3AssetsV1FilterTypeDef`) so type checkers validate the field
names and operators against the API.

> **Note:** the older `...FilterT` filter classes are deprecated and will be
> removed in a future major release. Prefer the dict form shown above.

The REST API documentation describes all the available APIs and can be accessed from the help section in the top right corner of the Clumio UI.