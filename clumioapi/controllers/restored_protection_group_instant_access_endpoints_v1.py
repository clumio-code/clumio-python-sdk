#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.controllers.types import restored_protection_group_instant_access_endpoints_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import add_protection_group_instant_access_endpoint_role_v1_request
from clumioapi.models import add_s3_instant_access_endpoint_role_response
from clumioapi.models import cost_estimates_protection_group_instant_access_endpoint_v1_request
from clumioapi.models import create_protection_group_instant_access_endpoint_v1_request
from clumioapi.models import create_s3_instant_access_endpoint_response
from clumioapi.models import delete_s3_instant_access_endpoint_role_response
from clumioapi.models import estimate_cost_details_s3_instant_access_endpoint_response
from clumioapi.models import estimate_cost_s3_instant_access_endpoint_async_response
from clumioapi.models import estimate_cost_s3_instant_access_endpoint_sync_response
from clumioapi.models import list_s3_instant_access_endpoints_response
from clumioapi.models import read_s3_instant_access_endpoint_response
from clumioapi.models import read_s3_instant_access_endpoint_role_permission_response
from clumioapi.models import read_s3_instant_access_endpoint_uri_response
from clumioapi.models import update_protection_group_instant_access_endpoint_role_v1_request
from clumioapi.models import update_protection_group_instant_access_endpoint_v1_request
from clumioapi.models import update_s3_instant_access_endpoint_response
from clumioapi.models import update_s3_instant_access_endpoint_role_response
import requests
import retrying


class RestoredProtectionGroupInstantAccessEndpointsV1Controller:
    """A Controller to access Endpoints for restored-protection-group-instant-access-endpoints resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-protection-group-instant-access-endpoints=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_protection_group_instant_access_endpoints(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            restored_protection_group_instant_access_endpoints_types.ListProtectionGroupInstantAccessEndpointsV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse:
        """Lists S3 instant access endpoints depending on the filters present in the body.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | protection_group_id         | $eq              | The Clumio-assigned ID of   |
                |                             |                  | the protection group        |
                |                             |                  | associated with the desired |
                |                             |                  | endpoints.                  |
                +-----------------------------+------------------+-----------------------------+
                | protection_group_s3_asset_i | $eq              | The Clumio-assigned ID of   |
                | d                           |                  | the Protection Group S3     |
                |                             |                  | asset associated with the   |
                |                             |                  | desired endpoints. The      |
                |                             |                  | field must be used with     |
                |                             |                  | protection_group_id.        |
                +-----------------------------+------------------+-----------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: (
            list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse
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
            error_str = f'list_protection_group_instant_access_endpoints for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_protection_group_instant_access_endpoint(
        self,
        body: (
            create_protection_group_instant_access_endpoint_v1_request.CreateProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse:
        """Creates an endpoint that provides instant access to a protection group backup at
        a specific
        backup point or arbitrary point-in-time if the S3 continuous backup is enabled.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints'

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse
        )
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
            error_str = f'create_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def cost_estimates_protection_group_instant_access_endpoint(
        self,
        body: (
            cost_estimates_protection_group_instant_access_endpoint_v1_request.CostEstimatesProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse,
        estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse,
    ]:
        """Estimates cost for creating and maintaining a S3 instant access endpoint with
        given parameters.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:

            obj: Any

            if resp.status_code == 200:
                obj = estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse.from_response(
                    resp
                )
                return obj

            if resp.status_code == 202:
                obj = estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse.from_response(
                    resp
                )
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for cost_estimates_protection_group_instant_access_endpoint.',
                resp=resp,
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/cost-estimates'

        _query_parameters: dict[str, Any] = {}

        resp_instance: Union[
            estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse,
            estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse,
        ]
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
            error_str = f'cost_estimates_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def cost_estimates_details_protection_group_instant_access_endpoint(
        self, estimate_id: str | None = None, **kwargs
    ) -> (
        estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse
    ):
        """Details of the cost estimate for an S3 instant access endpoint from a given
        estimate ID.

        Args:
            estimate_id:
                Performs the operation on the estimate with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/cost-estimates/{estimate_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'estimate_id': estimate_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse
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
            error_str = f'cost_estimates_details_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_protection_group_instant_access_endpoint(
        self, endpoint_id: str | None = None, **kwargs
    ) -> read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse:
        """Return detailed information for a specified S3 instant access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to read
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse
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
            error_str = f'read_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_protection_group_instant_access_endpoint(
        self,
        endpoint_id: str | None = None,
        body: (
            update_protection_group_instant_access_endpoint_v1_request.UpdateProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse:
        """Updates an endpoint for S3 Instant Access.

        Args:
            endpoint_id:
                ID of the endpoint to update
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
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
            error_str = f'update_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_protection_group_instant_access_endpoint(
        self, endpoint_id: str | None = None, **kwargs
    ) -> object:
        """Deletes a S3 instant access endpoint and all its details.

        Args:
            endpoint_id:
                ID of the endpoint to delete
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return resp

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: object
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
            error_str = f'delete_protection_group_instant_access_endpoint for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_protection_group_instant_access_endpoint_uri(
        self, endpoint_id: str | None = None, **kwargs
    ) -> read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse:
        """Reads the URI of S3 instant access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to read
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/_get_uri'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse
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
            error_str = f'read_protection_group_instant_access_endpoint_uri for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def add_protection_group_instant_access_endpoint_role(
        self,
        endpoint_id: str | None = None,
        body: (
            add_protection_group_instant_access_endpoint_role_v1_request.AddProtectionGroupInstantAccessEndpointRoleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse:
        """Adds a user-defined IAM role to allow access to an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to add a role
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse
        )
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
            error_str = f'add_protection_group_instant_access_endpoint_role for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_protection_group_instant_access_endpoint_role_permission(
        self, endpoint_id: str | None = None, **kwargs
    ) -> (
        read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse
    ):
        """Reads the permissions JSON string to be attached to the user-defined IAM role
        that can access
        an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to update a role
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/permissions'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse
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
            error_str = f'read_protection_group_instant_access_endpoint_role_permission for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_protection_group_instant_access_endpoint_role(
        self,
        endpoint_id: str | None = None,
        role_id: str | None = None,
        body: (
            update_protection_group_instant_access_endpoint_role_v1_request.UpdateProtectionGroupInstantAccessEndpointRoleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse:
        """Updates a user-defined IAM role that is attached to an S3 Instant Access
        endpoint if any
        changes are made to that role.

        Args:
            endpoint_id:
                ID of the endpoint to update a role
            role_id:
                ID of the currently enrolled role to be access the endpoint.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/{role_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id, 'role_id': role_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse
        )
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.put(
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
            error_str = f'update_protection_group_instant_access_endpoint_role for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def delete_protection_group_instant_access_endpoint_role(
        self, endpoint_id: str | None = None, role_id: str | None = None, **kwargs
    ) -> delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse:
        """Deletes a user-defined IAM role attached to an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint from which to delete a role.
            role_id:
                ID of the currently attached role to which access to the endpoint will be
                blocked.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/{role_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id, 'role_id': role_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: (
            delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse
        )
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
            error_str = f'delete_protection_group_instant_access_endpoint_role for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredProtectionGroupInstantAccessEndpointsV1ControllerPaginator:
    """A Controller to access Endpoints for restored-protection-group-instant-access-endpoints resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_protection_group_instant_access_endpoints(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            restored_protection_group_instant_access_endpoints_types.ListProtectionGroupInstantAccessEndpointsV1FilterT
            | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse]:
        """Lists S3 instant access endpoints depending on the filters present in the body.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | protection_group_id         | $eq              | The Clumio-assigned ID of   |
                |                             |                  | the protection group        |
                |                             |                  | associated with the desired |
                |                             |                  | endpoints.                  |
                +-----------------------------+------------------+-----------------------------+
                | protection_group_s3_asset_i | $eq              | The Clumio-assigned ID of   |
                | d                           |                  | the Protection Group S3     |
                |                             |                  | asset associated with the   |
                |                             |                  | desired endpoints. The      |
                |                             |                  | field must be used with     |
                |                             |                  | protection_group_id.        |
                +-----------------------------+------------------+-----------------------------+

        """
        controller = RestoredProtectionGroupInstantAccessEndpointsV1Controller(self.controller)
        while True:
            response = controller.list_protection_group_instant_access_endpoints(
                limit=limit, start=start, filter=filter, **kwargs
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
