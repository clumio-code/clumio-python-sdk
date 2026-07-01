#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_gcs_assets_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_gcpgcs_asset_pitr_intervals_response
from clumioapi.models import list_gcpgcs_assets_response
from clumioapi.models import read_gcpgcs_asset_continuous_backup_stats_response
from clumioapi.models import read_gcpgcs_asset_response
import requests
import retrying


class GcpGcsAssetsV1Controller:
    """A Controller to access Endpoints for gcp-gcs-assets resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-gcs-assets=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_gcs_assets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_assets_types.ListGcpGcsAssetsV1FilterT
            | gcp_gcs_assets_types.ListGcpGcsAssetsV1FilterTypeDef
            | None
        ) = None,
        embed: str | None = None,
        **kwargs,
    ) -> list_gcpgcs_assets_response.ListGCPGCSAssetsResponse:
        """Returns a list of GCP GCS assets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +---------------------+---------------+----------------------------------------+
                |        Field        |   Condition   |              Description               |
                +=====================+===============+========================================+
                | id                  | $eq,$in       | The Clumio-assigned ID of the GCS      |
                |                     |               | asset.                                 |
                +---------------------+---------------+----------------------------------------+
                | protection_group_id | $eq,$in       | The Clumio-assigned ID of the          |
                |                     |               | protection group.                      |
                +---------------------+---------------+----------------------------------------+
                | bucket_id           | $eq,$in       | The Clumio-assigned ID of the GCS      |
                |                     |               | bucket.                                |
                +---------------------+---------------+----------------------------------------+
                | bucket_name         | $eq,$in       | The name of the GCS bucket.            |
                +---------------------+---------------+----------------------------------------+
                | is_deleted          | $eq           | Boolean flag indicating whether to     |
                |                     |               | return deleted (true) or active        |
                |                     |               | (false) GCS assets.                    |
                +---------------------+---------------+----------------------------------------+
                | name                | $eq,$contains | The display name of the GCS asset.     |
                +---------------------+---------------+----------------------------------------+
                | added_by            | $in           | The method by which the GCS asset was  |
                |                     |               | added. Possible values include user    |
                |                     |               | and bucket_rule.                       |
                +---------------------+---------------+----------------------------------------+
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources                |
                |                        | will not have an associated policy. For example,    |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcpgcs_assets_response.ListGCPGCSAssetsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-assets'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_gcs_assets_types.ListGcpGcsAssetsV1FilterT
            ),
            'embed': embed,
        }

        resp_instance: list_gcpgcs_assets_response.ListGCPGCSAssetsResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_gcp_gcs_assets for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_gcp_gcs_asset(
        self, gcs_asset_id: str | None = None, embed: str | None = None, **kwargs
    ) -> read_gcpgcs_asset_response.ReadGCPGCSAssetResponse:
        """Returns a representation of the specified GCP GCS asset.

        Args:
            gcs_asset_id:
                Performs the operation on the GCS asset with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources                |
                |                        | will not have an associated policy. For example,    |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_gcpgcs_asset_response.ReadGCPGCSAssetResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-assets/{gcs_asset_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'gcs_asset_id': gcs_asset_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: read_gcpgcs_asset_response.ReadGCPGCSAssetResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_gcp_gcs_asset for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_gcp_gcs_asset_continuous_backup_stats(
        self,
        gcs_asset_id: str | None = None,
        begin_timestamp: str | None = None,
        end_timestamp: str | None = None,
        interval: str | None = None,
        **kwargs,
    ) -> (
        read_gcpgcs_asset_continuous_backup_stats_response.ReadGCPGCSAssetContinuousBackupStatsResponse
    ):
        """Returns continuous backup statistics of the specified GCP GCS asset.

        Args:
            gcs_asset_id:
                Performs the operation on the GCS asset with the specified ID.
            begin_timestamp:
                The beginning time of start_time filter in RFC-3339 format.
            end_timestamp:
                The end time of start_time filter in RFC-3339 format. If a future
                timestamp is supplied, the server clamps it to the current server time
                before validating the range against `begin_timestamp`.
            interval:
                The interval for bins represented as time duration.
                'm', 'h' and 'd' refers to minutes, hours, and days respectively.
                A series of aggregated statistics for each interval will be returned as `bins`
                in the response.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_gcpgcs_asset_continuous_backup_stats_response.ReadGCPGCSAssetContinuousBackupStatsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-assets/{gcs_asset_id}/continuous-backup-stats'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'gcs_asset_id': gcs_asset_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'begin_timestamp': begin_timestamp,
            'end_timestamp': end_timestamp,
            'interval': interval,
        }

        resp_instance: (
            read_gcpgcs_asset_continuous_backup_stats_response.ReadGCPGCSAssetContinuousBackupStatsResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_gcp_gcs_asset_continuous_backup_stats for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_gcp_gcs_asset_pitr_intervals(
        self,
        gcs_asset_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_assets_types.ListGcpGcsAssetPitrIntervalsV1FilterT
            | gcp_gcs_assets_types.ListGcpGcsAssetPitrIntervalsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> list_gcpgcs_asset_pitr_intervals_response.ListGCPGCSAssetPitrIntervalsResponse:
        """Returns a list of time intervals (start timestamp and end timestamp) in which
        the GCS asset can be restored.

        Args:
            gcs_asset_id:
                Performs the operation on the GCS asset with the specified ID.
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_gcpgcs_asset_pitr_intervals_response.ListGCPGCSAssetPitrIntervalsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/gcs-assets/{gcs_asset_id}/pitr-intervals'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'gcs_asset_id': gcs_asset_id}
        )

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_gcs_assets_types.ListGcpGcsAssetPitrIntervalsV1FilterT
            ),
        }

        resp_instance: (
            list_gcpgcs_asset_pitr_intervals_response.ListGCPGCSAssetPitrIntervalsResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_gcp_gcs_asset_pitr_intervals for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpGcsAssetsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-gcs-assets resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_gcs_assets(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_assets_types.ListGcpGcsAssetsV1FilterT
            | gcp_gcs_assets_types.ListGcpGcsAssetsV1FilterTypeDef
            | None
        ) = None,
        embed: str | None = None,
        **kwargs,
    ) -> Iterator[list_gcpgcs_assets_response.ListGCPGCSAssetsResponse]:
        """Returns a list of GCP GCS assets.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +---------------------+---------------+----------------------------------------+
                |        Field        |   Condition   |              Description               |
                +=====================+===============+========================================+
                | id                  | $eq,$in       | The Clumio-assigned ID of the GCS      |
                |                     |               | asset.                                 |
                +---------------------+---------------+----------------------------------------+
                | protection_group_id | $eq,$in       | The Clumio-assigned ID of the          |
                |                     |               | protection group.                      |
                +---------------------+---------------+----------------------------------------+
                | bucket_id           | $eq,$in       | The Clumio-assigned ID of the GCS      |
                |                     |               | bucket.                                |
                +---------------------+---------------+----------------------------------------+
                | bucket_name         | $eq,$in       | The name of the GCS bucket.            |
                +---------------------+---------------+----------------------------------------+
                | is_deleted          | $eq           | Boolean flag indicating whether to     |
                |                     |               | return deleted (true) or active        |
                |                     |               | (false) GCS assets.                    |
                +---------------------+---------------+----------------------------------------+
                | name                | $eq,$contains | The display name of the GCS asset.     |
                +---------------------+---------------+----------------------------------------+
                | added_by            | $in           | The method by which the GCS asset was  |
                |                     |               | added. Possible values include user    |
                |                     |               | and bucket_rule.                       |
                +---------------------+---------------+----------------------------------------+
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources                |
                |                        | will not have an associated policy. For example,    |
                |                        | embed=read-policy-definition                        |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
        """
        controller = GcpGcsAssetsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_gcs_assets(
                limit=limit, start=start, filter=filter, embed=embed, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_gcs_asset_pitr_intervals(
        self,
        gcs_asset_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_gcs_assets_types.ListGcpGcsAssetPitrIntervalsV1FilterT
            | gcp_gcs_assets_types.ListGcpGcsAssetPitrIntervalsV1FilterTypeDef
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_gcpgcs_asset_pitr_intervals_response.ListGCPGCSAssetPitrIntervalsResponse]:
        """Returns a list of time intervals (start timestamp and end timestamp) in which
        the GCS asset can be restored.

        Args:
            gcs_asset_id:
                Performs the operation on the GCS asset with the specified ID.
            limit:
                Limits the size of the items returned in the response.
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

        """
        controller = GcpGcsAssetsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_gcs_asset_pitr_intervals(
                gcs_asset_id=gcs_asset_id, limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
