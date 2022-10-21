#
# Copyright 2021. Clumio, Inc.
#

import requests

from clumioapi import api_helper, configuration, sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import (
    list_protection_group_s3_assets_response,
    read_protection_group_s3_asset_response,
)


class ProtectionGroupsS3AssetsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for protection-groups-s3-assets resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.protection-groups-s3-assets=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_protection_group_s3_assets(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse:
        """Returns a list of protection group S3 assets.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | account_native_id         | $eq              | The AWS-assigned ID of the    |
                |                           |                  | AWS account. For example, fil |
                |                           |                  | ter={"account_native_id":{"$e |
                |                           |                  | q":"789901323485"}}           |
                +---------------------------+------------------+-------------------------------+
                | aws_region                | $eq              | The AWS region of a given     |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example, filter={"account_nat |
                |                           |                  | ive_id":{"$eq":"789901323485" |
                |                           |                  | }, "aws_region":{"$eq":"us-   |
                |                           |                  | east-1"}} retrieves DynamoDB  |
                |                           |                  | tables in region us-east-1 in |
                |                           |                  | account 789901323485.         |
                +---------------------------+------------------+-------------------------------+
                | bucket_id                 | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS S3 bucket. Retrieves the  |
                |                           |                  | protection group s3 assets    |
                |                           |                  | within this S3 bucket.        |
                +---------------------------+------------------+-------------------------------+
                | bucket_name               | $eq              | The AWS-assigned ID or name   |
                |                           |                  | of the bucket. Retrieves the  |
                |                           |                  | protection group s3 assets    |
                |                           |                  | within this S3 bucket.        |
                +---------------------------+------------------+-------------------------------+
                | compliance_status         | $eq, $in         | The compliance status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include compliant and         |
                |                           |                  | non_compliant.                |
                |                           |                  |                               |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq              | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active         |
                |                           |                  | protection group buckets.     |
                +---------------------------+------------------+-------------------------------+
                | protection_group_id       | $eq              | The Clumio-assigned ID of the |
                |                           |                  | protection group of this      |
                |                           |                  | resource. Retrieves the       |
                |                           |                  | protection group s3 assets    |
                |                           |                  | within this protection group. |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include protected,            |
                |                           |                  | unprotected, and unsupported. |
                |                           |                  | If the compliance_status      |
                |                           |                  | filter parameter is set, this |
                |                           |                  | parameter value cannot        |
                |                           |                  | include "unprotected".        |
                +---------------------------+------------------+-------------------------------+
                | organizational_unit_id    | $in              | Denotes the organizational    |
                |                           |                  | unit IDs that can own the     |
                |                           |                  | assets that are returned. For |
                |                           |                  | example, filter={"organizatio |
                |                           |                  | nal_unit_id":{"$in":["c764b15 |
                |                           |                  | 2-5819-11ea-bb9f-             |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                +---------------------------+------------------+-------------------------------+

        Returns:
            ListProtectionGroupS3AssetsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/protection-groups/s3-assets'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing list_protection_group_s3_assets.", errors
            )
        return list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse.from_dictionary(
            resp
        )

    def read_protection_group_s3_asset(
        self, protection_group_s3_asset_id: str
    ) -> read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse:
        """Returns a representation of the specified protection group S3 asset.

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the protection group S3 asset with the specified ID.
        Returns:
            ReadProtectionGroupS3AssetResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/protection-groups/s3-assets/{protection_group_s3_asset_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_s3_asset_id': protection_group_s3_asset_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                "Error occurred while executing read_protection_group_s3_asset.", errors
            )
        return read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse.from_dictionary(
            resp
        )
