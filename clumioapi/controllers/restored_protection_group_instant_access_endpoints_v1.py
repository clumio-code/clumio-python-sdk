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


class RestoredProtectionGroupInstantAccessEndpointsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-protection-group-instant-access-endpoints resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-protection-group-instant-access-endpoints=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_protection_group_instant_access_endpoints(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse,
        tuple[
            requests.Response,
            Optional[
                list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse
            ],
        ],
    ]:
        """Lists S3 instant access endpoints depending on the filters present in the body.

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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints'

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
                'Error occurred while executing list_protection_group_instant_access_endpoints.',
                errors,
            )

        obj = list_s3_instant_access_endpoints_response.ListS3InstantAccessEndpointsResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def create_protection_group_instant_access_endpoint(
        self,
        body: (
            create_protection_group_instant_access_endpoint_v1_request.CreateProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse,
        tuple[
            requests.Response,
            Optional[
                create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse
            ],
        ],
    ]:
        """Creates an endpoint that provides instant access to a protection group backup at
        a specific
        backup point or arbitrary point-in-time if the S3 continuous backup is enabled.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints'

        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_protection_group_instant_access_endpoint.',
                errors,
            )

        obj = create_s3_instant_access_endpoint_response.CreateS3InstantAccessEndpointResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def cost_estimates_protection_group_instant_access_endpoint(
        self,
        body: (
            cost_estimates_protection_group_instant_access_endpoint_v1_request.CostEstimatesProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        Union[
            estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse,
            estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse,
        ],
        tuple[
            requests.Response,
            Optional[
                Union[
                    estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse,
                    estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse,
                ]
            ],
        ],
    ]:
        """Estimates cost for creating and maintaining a S3 instant access endpoint with
        given parameters.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            Union[estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse, estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse]: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/cost-estimates'

        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing cost_estimates_protection_group_instant_access_endpoint.',
                errors,
            )
        text_unmarshalled_dict = json.loads(resp.text)

        obj: Any

        obj = estimate_cost_s3_instant_access_endpoint_sync_response.EstimateCostS3InstantAccessEndpointSyncResponse.from_dictionary(
            text_unmarshalled_dict
        )
        if resp.status_code == 200:
            if raw_response:
                return resp, obj
            return obj

        obj = estimate_cost_s3_instant_access_endpoint_async_response.EstimateCostS3InstantAccessEndpointAsyncResponse.from_dictionary(
            text_unmarshalled_dict
        )
        if resp.status_code == 202:
            if raw_response:
                return resp, obj
            return obj

        raise RuntimeError(
            f'Code should be unreachable; Unexpected response code: {resp.status_code}. '
        )

    def cost_estimates_details_protection_group_instant_access_endpoint(
        self, estimate_id: str | None = None, **kwargs
    ) -> Union[
        estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse,
        tuple[
            requests.Response,
            Optional[
                estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse
            ],
        ],
    ]:
        """Details of the cost estimate for an S3 instant access endpoint from a given
        estimate ID.

        Args:
            estimate_id:
                Performs the operation on the estimate with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/cost-estimates/{estimate_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'estimate_id': estimate_id}
        )
        _query_parameters: dict[str, Any] = {}

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
                'Error occurred while executing cost_estimates_details_protection_group_instant_access_endpoint.',
                errors,
            )

        obj = estimate_cost_details_s3_instant_access_endpoint_response.EstimateCostDetailsS3InstantAccessEndpointResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_protection_group_instant_access_endpoint(
        self, endpoint_id: str | None = None, **kwargs
    ) -> Union[
        read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse,
        tuple[
            requests.Response,
            Optional[read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse],
        ],
    ]:
        """Return detailed information for a specified S3 instant access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to read
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

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
                'Error occurred while executing read_protection_group_instant_access_endpoint.',
                errors,
            )

        obj = read_s3_instant_access_endpoint_response.ReadS3InstantAccessEndpointResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def update_protection_group_instant_access_endpoint(
        self,
        endpoint_id: str | None = None,
        body: (
            update_protection_group_instant_access_endpoint_v1_request.UpdateProtectionGroupInstantAccessEndpointV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse,
        tuple[
            requests.Response,
            Optional[
                update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse
            ],
        ],
    ]:
        """Updates an endpoint for S3 Instant Access.

        Args:
            endpoint_id:
                ID of the endpoint to update
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_protection_group_instant_access_endpoint.',
                errors,
            )

        obj = update_s3_instant_access_endpoint_response.UpdateS3InstantAccessEndpointResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def delete_protection_group_instant_access_endpoint(
        self, endpoint_id: str | None = None, **kwargs
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Deletes a S3 instant access endpoint and all its details.

        Args:
            endpoint_id:
                ID of the endpoint to delete
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.delete(
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
                'Error occurred while executing delete_protection_group_instant_access_endpoint.',
                errors,
            )

        if raw_response:
            return resp, resp.json()
        return resp

    def read_protection_group_instant_access_endpoint_uri(
        self, endpoint_id: str | None = None, **kwargs
    ) -> Union[
        read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse,
        tuple[
            requests.Response,
            Optional[
                read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse
            ],
        ],
    ]:
        """Reads the URI of S3 instant access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to read
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/_get_uri'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

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
                'Error occurred while executing read_protection_group_instant_access_endpoint_uri.',
                errors,
            )

        obj = read_s3_instant_access_endpoint_uri_response.ReadS3InstantAccessEndpointUriResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def add_protection_group_instant_access_endpoint_role(
        self,
        endpoint_id: str | None = None,
        body: (
            add_protection_group_instant_access_endpoint_role_v1_request.AddProtectionGroupInstantAccessEndpointRoleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse,
        tuple[
            requests.Response,
            Optional[
                add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse
            ],
        ],
    ]:
        """Adds a user-defined IAM role to allow access to an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to add a role
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing add_protection_group_instant_access_endpoint_role.',
                errors,
            )

        obj = add_s3_instant_access_endpoint_role_response.AddS3InstantAccessEndpointRoleResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def read_protection_group_instant_access_endpoint_role_permission(
        self, endpoint_id: str | None = None, **kwargs
    ) -> Union[
        read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse,
        tuple[
            requests.Response,
            Optional[
                read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse
            ],
        ],
    ]:
        """Reads the permissions JSON string to be attached to the user-defined IAM role
        that can access
        an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint to update a role
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/permissions'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id}
        )
        _query_parameters: dict[str, Any] = {}

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
                'Error occurred while executing read_protection_group_instant_access_endpoint_role_permission.',
                errors,
            )

        obj = read_s3_instant_access_endpoint_role_permission_response.ReadS3InstantAccessEndpointRolePermissionResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def update_protection_group_instant_access_endpoint_role(
        self,
        endpoint_id: str | None = None,
        role_id: str | None = None,
        body: (
            update_protection_group_instant_access_endpoint_role_v1_request.UpdateProtectionGroupInstantAccessEndpointRoleV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse,
        tuple[
            requests.Response,
            Optional[
                update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse
            ],
        ],
    ]:
        """Updates a user-defined IAM role that is attached to an S3 Instant Access
        endpoint if any
        changes are made to that role.

        Args:
            endpoint_id:
                ID of the endpoint to update a role
            role_id:
                ID of the currently enrolled role to be access the endpoint.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/{role_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id, 'role_id': role_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_protection_group_instant_access_endpoint_role.',
                errors,
            )

        obj = update_s3_instant_access_endpoint_role_response.UpdateS3InstantAccessEndpointRoleResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj

    def delete_protection_group_instant_access_endpoint_role(
        self, endpoint_id: str | None = None, role_id: str | None = None, **kwargs
    ) -> Union[
        delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse,
        tuple[
            requests.Response,
            Optional[
                delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse
            ],
        ],
    ]:
        """Deletes a user-defined IAM role attached to an S3 Instant Access endpoint.

        Args:
            endpoint_id:
                ID of the endpoint from which to delete a role.
            role_id:
                ID of the currently attached role to which access to the endpoint will be
                blocked.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            '/restores/protection-groups/instant-access-endpoints/{endpoint_id}/roles/{role_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'endpoint_id': endpoint_id, 'role_id': role_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.delete(
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
                'Error occurred while executing delete_protection_group_instant_access_endpoint_role.',
                errors,
            )

        obj = delete_s3_instant_access_endpoint_role_response.DeleteS3InstantAccessEndpointRoleResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
