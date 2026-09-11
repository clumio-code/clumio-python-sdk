# Clumio Python SDK

## Overview

The `clumio-python-sdk` Python package provides an object-oriented API which allows developers to
write software using operations which Clumio provides for protecting data. This document provides
information on how to build and use the SDK.

## Requirements

Python 3.9 or higher. Third-party dependencies are listed in `requirements.txt` and are
installed automatically by `pip`.

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

## Configuration
`api_token` falls back to the `API_TOKEN` environment variable when it is not passed
explicitly. Two optional arguments cover multi-tenant and proxy setups:
```
   config = configuration.Configuration(
       hostname='api.clumio.com',
       organizational_unit_context='<organizational_unit_id>',
       custom_headers={'x-my-header': 'value'},
   )
```
`organizational_unit_context` scopes every request to that organizational unit, and
`custom_headers` is merged into the headers the SDK already sends.

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

## Pagination
Every resource also exposes a `<resource>_paginator` property. It walks the `_links.next`
chain and yields one response per page, so `start` does not have to be tracked by hand:
```
   for page in client.protection_groups_s3_assets_v1_paginator.list_protection_group_s3_assets(
       filter={'aws_region': {'$eq': 'us-west-2'}},
   ):
       for asset in page.Embedded.Items:
           print(asset.name)
```
The non-paginated controller returns a single page and accepts `limit` and `start` for
callers that need to drive paging themselves.

The REST API documentation describes all the available APIs and can be accessed from the help section in the top right corner of the Clumio UI.
