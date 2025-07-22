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
from clumioapi.models import add_bucket_protection_group_v1_request
from clumioapi.models import add_bucket_to_protection_group_response
from clumioapi.models import create_protection_group_response
from clumioapi.models import create_protection_group_v1_request
from clumioapi.models import delete_bucket_from_protection_group_response
from clumioapi.models import list_protection_groups_response
from clumioapi.models import read_protection_group_response
from clumioapi.models import update_protection_group_response
from clumioapi.models import update_protection_group_v1_request
import requests


class ProtectionGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for protection-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_protection_groups(
        self, limit: int, start: str, filter: str, lookback_days: int, **kwargs
    ) -> Union[
        list_protection_groups_response.ListProtectionGroupsResponse,
        tuple[
            requests.Response,
            Optional[list_protection_groups_response.ListProtectionGroupsResponse],
        ],
    ]:
        """Returns a list of protection groups.

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
                | is_deleted                | $eq,$in          | The deletion status of the    |
                |                           |                  | protection group. Set to      |
                |                           |                  | "true" to retrieve deleted    |
                |                           |                  | protection group. For         |
                |                           |                  | example, filter={"is_deleted" |
                |                           |                  | :{"$eq":true}} filter={"is_de |
                |                           |                  | leted":{"$in":["true","false" |
                |                           |                  | ]}}                           |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains, $eq   | The AWS-assigned name of this |
                |                           |                  | resource, can use either the  |
                |                           |                  | contains or exact equal       |
                |                           |                  | operator. For example, filter |
                |                           |                  | ={"name":{"$contains":"dev"}} |
                |                           |                  | retrieves all protection      |
                |                           |                  | groups with "dev" in their    |
                |                           |                  | name.                         |
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
                | organizational_unit_id    | $in              | Denotes the organizational    |
                |                           |                  | unit IDs that can own the     |
                |                           |                  | assets that are returned. For |
                |                           |                  | example, filter={"organizatio |
                |                           |                  | nal_unit_id":{"$in":["c764b15 |
                |                           |                  | 2-5819-11ea-bb9f-             |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                +---------------------------+------------------+-------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_protection_groups_response.ListProtectionGroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/protection-groups'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter,
            'lookback_days': lookback_days,
        }

        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_protection_groups.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                list_protection_groups_response.ListProtectionGroupsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return list_protection_groups_response.ListProtectionGroupsResponse.from_dictionary(
            resp.json()
        )

    def read_protection_group(self, group_id: str, lookback_days: int, **kwargs) -> Union[
        read_protection_group_response.ReadProtectionGroupResponse,
        tuple[
            requests.Response, Optional[read_protection_group_response.ReadProtectionGroupResponse]
        ],
    ]:
        """Returns a representation of the specified protection group.

        Args:
            group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_protection_group_response.ReadProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/datasources/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'lookback_days': lookback_days}

        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_protection_group.', errors
            )

        if self.config.raw_response:
            return resp, read_protection_group_response.ReadProtectionGroupResponse.from_dictionary(
                resp.json()
            )
        return read_protection_group_response.ReadProtectionGroupResponse.from_dictionary(
            resp.json()
        )

    def create_protection_group(
        self, body: create_protection_group_v1_request.CreateProtectionGroupV1Request, **kwargs
    ) -> Union[
        create_protection_group_response.CreateProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[create_protection_group_response.CreateProtectionGroupResponse],
        ],
    ]:
        """Creates a new protection group by specifying object filters. Appearance in
        datasources/protection-groups read/listing is asynchronous and may take a few
        seconds to minutes at most. As a result, the protection group won't be
        protectable
        via /policies/assignments until it appears in the /datasources/protection-groups
        endpoint. Additionally, to create a protection group in the context of another
        Organizational
        Unit, refer to the Getting Started
        documentation.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_protection_group_response.CreateProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/protection-groups'

        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_protection_group_response.CreateProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return create_protection_group_response.CreateProtectionGroupResponse.from_dictionary(
            resp.json()
        )

    def update_protection_group(
        self,
        group_id: str,
        body: update_protection_group_v1_request.UpdateProtectionGroupV1Request,
        **kwargs,
    ) -> Union[
        update_protection_group_response.UpdateProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[update_protection_group_response.UpdateProtectionGroupResponse],
        ],
    ]:
        """Updates a protection group by modifying object filters. Appearance in
        datasources/protection-groups read/listing is asynchronous and may take a few
        seconds to minutes at most. Must be in the same OU context as the creator of
        this
        protection group.

        Args:
            group_id:
                ID of the protection group to update
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_protection_group_response.UpdateProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.put(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                update_protection_group_response.UpdateProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return update_protection_group_response.UpdateProtectionGroupResponse.from_dictionary(
            resp.json()
        )

    def delete_protection_group(
        self, group_id: str, **kwargs
    ) -> Union[object, tuple[requests.Response, Optional[object]]]:
        """Marks a protection group as deleted by taking the protection group ID.
        Appearance
        in /datasources/protection-groups read/listing is asynchronous and may take a
        few
        seconds to minutes at most. Must be in the same OU context as the creator of
        this
        protection group.

        Args:
            group_id:
                ID of the protection group to delete
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_protection_group.', errors
            )

        if self.config.raw_response:
            return resp, resp.json()
        return resp

    def add_bucket_protection_group(
        self,
        group_id: str,
        body: add_bucket_protection_group_v1_request.AddBucketProtectionGroupV1Request,
        **kwargs,
    ) -> Union[
        add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse],
        ],
    ]:
        """Adds a bucket to protection group and creates a child protection group S3 asset.
        Appearance in /datasources/protection-groups/s3-assets read/listing is
        asynchronous
        and may take a few seconds to minutes at most. Must be in the same OU context as
        the creator of this protection group. Bucket ID in body can be found in
        datasources/aws/s3.

        Args:
            group_id:
                ID of the protection group
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/protection-groups/{group_id}/buckets'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing add_bucket_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse.from_dictionary(
            resp.json()
        )

    def delete_bucket_protection_group(self, group_id: str, bucket_id: str, **kwargs) -> Union[
        delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse,
        tuple[
            requests.Response,
            Optional[
                delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse
            ],
        ],
    ]:
        """Deletes a bucket from a protection group and the child protection group S3
        asset.
        Appearance in /datasources/protection-groups/s3-assets read/listing is
        asynchronous
        and may take a few seconds to minutes at most. Must be in the same OU context as
        the creator of this protection group. Bucket ID in path can be found in
        datasources/aws/s3.

        Args:
            group_id:
                ID of the protection group
            bucket_id:
                ID of the bucket to delete
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/protection-groups/{group_id}/buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id, 'bucket_id': bucket_id}
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.delete(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_bucket_protection_group.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse.from_dictionary(
                    resp.json()
                ),
            )
        return delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse.from_dictionary(
            resp.json()
        )
