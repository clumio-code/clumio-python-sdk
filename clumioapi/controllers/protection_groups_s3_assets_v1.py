#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_protection_group_s3_asset_pitr_intervals_response
from clumioapi.models import list_protection_group_s3_assets_response
from clumioapi.models import read_protection_group_s3_asset_continuous_backup_stats_response
from clumioapi.models import read_protection_group_s3_asset_response
import requests


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
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Union[
        list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse,
        tuple[
            requests.Response,
            Optional[list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse],
        ],
    ]:
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
                | bucket_name               | $eq,$contains    | The AWS-assigned ID or name   |
                |                           |                  | of the bucket. Retrieves the  |
                |                           |                  | protection group s3 assets    |
                |                           |                  | within this S3 bucket.        |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active         |
                |                           |                  | protection group buckets. fil |
                |                           |                  | ter={"is_deleted":{"$in":["tr |
                |                           |                  | ue","false"]}}                |
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
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
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
                | added_by                  | $in              | The method of addition used   |
                |                           |                  | to create a protection group  |
                |                           |                  | s3 asset. Possible values     |
                |                           |                  | include user and bucket_rule. |
                +---------------------------+------------------+-------------------------------+
                | is_supported              | $eq              | The Clumio supported status   |
                |                           |                  | for the S3 bucket. For        |
                |                           |                  | example, filter={"is_supporte |
                |                           |                  | d":{"$eq":true}}              |
                +---------------------------+------------------+-------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/protection-groups/s3-assets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter,
            'lookback_days': lookback_days,
        }

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_protection_group_s3_assets.', errors
            )

        obj = list_protection_group_s3_assets_response.ListProtectionGroupS3AssetsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_protection_group_s3_asset(
        self,
        protection_group_s3_asset_id: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Union[
        read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse,
        tuple[
            requests.Response,
            Optional[read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse],
        ],
    ]:
        """Returns a representation of the specified protection group S3 asset.

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the protection group S3 asset with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/protection-groups/s3-assets/{protection_group_s3_asset_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_s3_asset_id': protection_group_s3_asset_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'lookback_days': lookback_days}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_protection_group_s3_asset.', errors
            )

        obj = read_protection_group_s3_asset_response.ReadProtectionGroupS3AssetResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_protection_group_s3_asset_continuous_backup_stats(
        self,
        protection_group_s3_asset_id: str | None = None,
        bucket_name: str | None = None,
        bucket_id: str | None = None,
        begin_timestamp: str | None = None,
        end_timestamp: str | None = None,
        interval: str | None = None,
        **kwargs,
    ) -> Union[
        read_protection_group_s3_asset_continuous_backup_stats_response.ReadProtectionGroupS3AssetContinuousBackupStatsResponse,
        tuple[
            requests.Response,
            Optional[
                read_protection_group_s3_asset_continuous_backup_stats_response.ReadProtectionGroupS3AssetContinuousBackupStatsResponse
            ],
        ],
    ]:
        """Returns continuous backup statistics of the specified protection group S3 asset.

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the protection group S3 asset with the specified ID.
            bucket_name:
                The name of the source bucket.
            bucket_id:
                The Clumio-assigned ID of the source bucket.
            begin_timestamp:
                The beginning time of start_time filter in RFC-3339 format.
            end_timestamp:
                The end time of start_time filter in RFC-3339 format.
            interval:
                The interval for bins represented as time duration.
                'm', 'h' and 'd' refers to minutes, hours, and days respectively.
                A series of aggregated statistics for each interval will be returned as `bins`
                in the response.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_protection_group_s3_asset_continuous_backup_stats_response.ReadProtectionGroupS3AssetContinuousBackupStatsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/protection-groups/s3-assets/{protection_group_s3_asset_id}/continuous-backup-stats'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_s3_asset_id': protection_group_s3_asset_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'bucket_name': bucket_name,
            'bucket_id': bucket_id,
            'begin_timestamp': begin_timestamp,
            'end_timestamp': end_timestamp,
            'interval': interval,
        }

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_protection_group_s3_asset_continuous_backup_stats.',
                errors,
            )

        obj = read_protection_group_s3_asset_continuous_backup_stats_response.ReadProtectionGroupS3AssetContinuousBackupStatsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def list_protection_group_s3_asset_pitr_intervals(
        self,
        protection_group_s3_asset_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_protection_group_s3_asset_pitr_intervals_response.ListProtectionGroupS3AssetPitrIntervalsResponse,
        tuple[
            requests.Response,
            Optional[
                list_protection_group_s3_asset_pitr_intervals_response.ListProtectionGroupS3AssetPitrIntervalsResponse
            ],
        ],
    ]:
        """Returns a list of time intervals (start timestamp and end timestamp) in which
        the protection group S3 asset can be restored.

        Args:
            protection_group_s3_asset_id:
                Performs the operation on the protection group S3 asset with the specified ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------+------------------+-----------------------------------------------+
                |   Field   | Filter Condition |                  Description                  |
                +===========+==================+===============================================+
                | timestamp | $lte, $gte       | Filter pitr intervals whose range is "less    |
                |           |                  | than or equal to" or                          |
                |           |                  | "greater than or equal to" a given timestamp. |
                +-----------+------------------+-----------------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_protection_group_s3_asset_pitr_intervals_response.ListProtectionGroupS3AssetPitrIntervalsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/datasources/protection-groups/s3-assets/{protection_group_s3_asset_id}/pitr-intervals'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_s3_asset_id': protection_group_s3_asset_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_protection_group_s3_asset_pitr_intervals.',
                errors,
            )

        obj = list_protection_group_s3_asset_pitr_intervals_response.ListProtectionGroupS3AssetPitrIntervalsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
