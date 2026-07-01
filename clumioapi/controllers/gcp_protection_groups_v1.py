#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import gcp_protection_groups_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_gcp_protection_group_response
from clumioapi.models import create_gcp_protection_group_v1_request
from clumioapi.models import delete_gcp_protection_group_response
from clumioapi.models import list_gcp_protection_groups_response
from clumioapi.models import read_gcp_protection_group_response
from clumioapi.models import update_gcp_protection_group_response
from clumioapi.models import update_gcp_protection_group_v1_request
import requests
import retrying


class GcpProtectionGroupsV1Controller:
    """A Controller to access Endpoints for gcp-protection-groups resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.gcp-protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_gcp_protection_groups(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_protection_groups_types.ListGcpProtectionGroupsV1FilterT
            | gcp_protection_groups_types.ListGcpProtectionGroupsV1FilterTypeDef
            | None
        ) = None,
        bucket_uuid_detail: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_gcp_protection_groups_response.ListGCPProtectionGroupsResponse:
        """Returns a list of GCP protection groups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +---------------------------+---------------+----------------------------------+
                |           Field           |   Condition   |           Description            |
                +===========================+===============+==================================+
                | id                        | $eq,$in       | The Clumio-assigned ID of the    |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | native_id                 | $eq,$in       | The native GCP identifier of the |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | is_deleted                | $eq           | Boolean flag indicating whether  |
                |                           |               | to return deleted (true) or      |
                |                           |               | active (false) protection        |
                |                           |               | groups.                          |
                +---------------------------+---------------+----------------------------------+
                | name                      | $eq,$contains | The display name of the          |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | protection_info.policy_id | $eq           | The Clumio-assigned ID of the    |
                |                           |               | policy protecting this resource. |
                +---------------------------+---------------+----------------------------------+
                | protection_status         | $in           | The protection status of this    |
                |                           |               | resource. Possible values        |
                |                           |               | include protected and            |
                |                           |               | unprotected.                     |
                +---------------------------+---------------+----------------------------------+
                | deactivated               | $eq           | Filter assets protected by a     |
                |                           |               | deactivated policy.              |
                +---------------------------+---------------+----------------------------------+
            bucket_uuid_detail:
                Controls which bucket UUID arrays are included in each protection group item.
                When omitted, both `bucket_uuids` and `bucket_rule_matched_bucket_uuids` are
                excluded
                to reduce payload size. Counts (`bucket_count`, `manual_added_bucket_count`,
                `bucket_rule_matched_bucket_count`) are always returned regardless of this
                parameter.
                Valid values: `all`, `manual`, `bucket_rule`.
            lookback_days:
                Calculate backup status stats for the last `lookback_days` days. When
                omitted, every counter in `backup_status_stats` is reported as zero and
                no lookback-window classification is performed.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return (
                list_gcp_protection_groups_response.ListGCPProtectionGroupsResponse.from_response(
                    resp
                )
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/protection-groups'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, gcp_protection_groups_types.ListGcpProtectionGroupsV1FilterT
            ),
            'bucket_uuid_detail': bucket_uuid_detail,
            'lookback_days': lookback_days,
        }

        resp_instance: list_gcp_protection_groups_response.ListGCPProtectionGroupsResponse
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
            error_str = (
                f'list_gcp_protection_groups for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_gcp_protection_group(
        self,
        body: (
            create_gcp_protection_group_v1_request.CreateGcpProtectionGroupV1Request | None
        ) = None,
        **kwargs,
    ) -> create_gcp_protection_group_response.CreateGCPProtectionGroupResponse:
        """Creates a new GCP protection group.

        Args:
            body:
                The protection group to create
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return (
                create_gcp_protection_group_response.CreateGCPProtectionGroupResponse.from_response(
                    resp
                )
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/protection-groups'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_gcp_protection_group_response.CreateGCPProtectionGroupResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'create_gcp_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_gcp_protection_group(
        self, protection_group_id: str | None = None, lookback_days: int | None = None, **kwargs
    ) -> read_gcp_protection_group_response.ReadGCPProtectionGroupResponse:
        """Returns a representation of the specified GCP protection group.

        Args:
            protection_group_id:
                Performs the operation on the protection group with the specified ID.
            lookback_days:
                Calculate backup status stats for the last `lookback_days` days. When
                omitted, every counter in `backup_status_stats` is reported as zero and
                no lookback-window classification is performed.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_gcp_protection_group_response.ReadGCPProtectionGroupResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/protection-groups/{protection_group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'lookback_days': lookback_days,
        }

        resp_instance: read_gcp_protection_group_response.ReadGCPProtectionGroupResponse
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
            error_str = (
                f'read_gcp_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_gcp_protection_group(
        self, protection_group_id: str | None = None, **kwargs
    ) -> delete_gcp_protection_group_response.DeleteGCPProtectionGroupResponse:
        """Deletes the specified GCP protection group.

        Args:
            protection_group_id:
                Performs the operation on the protection group with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return (
                delete_gcp_protection_group_response.DeleteGCPProtectionGroupResponse.from_response(
                    resp
                )
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/protection-groups/{protection_group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: delete_gcp_protection_group_response.DeleteGCPProtectionGroupResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'delete_gcp_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_gcp_protection_group(
        self,
        protection_group_id: str | None = None,
        body: (
            update_gcp_protection_group_v1_request.UpdateGcpProtectionGroupV1Request | None
        ) = None,
        **kwargs,
    ) -> update_gcp_protection_group_response.UpdateGCPProtectionGroupResponse:
        """Updates an existing GCP protection group.

        Args:
            protection_group_id:
                Performs the operation on the protection group with the specified ID.
            body:
                The protection group update data
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return (
                update_gcp_protection_group_response.UpdateGCPProtectionGroupResponse.from_response(
                    resp
                )
            )

        # Prepare query URL
        _url_path = '/datasources/gcp/protection-groups/{protection_group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'protection_group_id': protection_group_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: update_gcp_protection_group_response.UpdateGCPProtectionGroupResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = (
                f'update_gcp_protection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class GcpProtectionGroupsV1ControllerPaginator:
    """A Controller to access Endpoints for gcp-protection-groups resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_gcp_protection_groups(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            gcp_protection_groups_types.ListGcpProtectionGroupsV1FilterT
            | gcp_protection_groups_types.ListGcpProtectionGroupsV1FilterTypeDef
            | None
        ) = None,
        bucket_uuid_detail: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_gcp_protection_groups_response.ListGCPProtectionGroupsResponse]:
        """Returns a list of GCP protection groups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                Supported filter fields:

                +---------------------------+---------------+----------------------------------+
                |           Field           |   Condition   |           Description            |
                +===========================+===============+==================================+
                | id                        | $eq,$in       | The Clumio-assigned ID of the    |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | native_id                 | $eq,$in       | The native GCP identifier of the |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | is_deleted                | $eq           | Boolean flag indicating whether  |
                |                           |               | to return deleted (true) or      |
                |                           |               | active (false) protection        |
                |                           |               | groups.                          |
                +---------------------------+---------------+----------------------------------+
                | name                      | $eq,$contains | The display name of the          |
                |                           |               | protection group.                |
                +---------------------------+---------------+----------------------------------+
                | protection_info.policy_id | $eq           | The Clumio-assigned ID of the    |
                |                           |               | policy protecting this resource. |
                +---------------------------+---------------+----------------------------------+
                | protection_status         | $in           | The protection status of this    |
                |                           |               | resource. Possible values        |
                |                           |               | include protected and            |
                |                           |               | unprotected.                     |
                +---------------------------+---------------+----------------------------------+
                | deactivated               | $eq           | Filter assets protected by a     |
                |                           |               | deactivated policy.              |
                +---------------------------+---------------+----------------------------------+
            bucket_uuid_detail:
                Controls which bucket UUID arrays are included in each protection group item.
                When omitted, both `bucket_uuids` and `bucket_rule_matched_bucket_uuids` are
                excluded
                to reduce payload size. Counts (`bucket_count`, `manual_added_bucket_count`,
                `bucket_rule_matched_bucket_count`) are always returned regardless of this
                parameter.
                Valid values: `all`, `manual`, `bucket_rule`.
            lookback_days:
                Calculate backup status stats for the last `lookback_days` days. When
                omitted, every counter in `backup_status_stats` is reported as zero and
                no lookback-window classification is performed.
        """
        controller = GcpProtectionGroupsV1Controller(self.controller)
        while True:
            response = controller.list_gcp_protection_groups(
                limit=limit,
                start=start,
                filter=filter,
                bucket_uuid_detail=bucket_uuid_detail,
                lookback_days=lookback_days,
                **kwargs,
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
