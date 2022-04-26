#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
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

    def list_protection_groups(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_protection_groups_response.ListProtectionGroupsResponse:
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
                | is_deleted                | $eq              | The deletion status of the    |
                |                           |                  | protection group. Set to      |
                |                           |                  | "true" to retrieve deleted    |
                |                           |                  | protection group. For         |
                |                           |                  | example, filter={"is_deleted" |
                |                           |                  | :{"$eq":true}}                |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains        | The AWS-assigned name of this |
                |                           |                  | resource. For example, filter |
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
                |                           |                  | If the compliance_status      |
                |                           |                  | filter parameter is set, this |
                |                           |                  | parameter value cannot        |
                |                           |                  | include "unprotected".        |
                +---------------------------+------------------+-------------------------------+

        Returns:
            ListProtectionGroupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/protection-groups'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_protection_groups.', errors
            )
        return list_protection_groups_response.ListProtectionGroupsResponse.from_dictionary(resp)

    def read_protection_group(
        self, group_id: str
    ) -> read_protection_group_response.ReadProtectionGroupResponse:
        """Returns a representation of the specified protection group.

        Args:
            group_id:
                Performs the operation on the ProtectionGroup with the specified ID.
        Returns:
            ReadProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_protection_group.', errors
            )
        return read_protection_group_response.ReadProtectionGroupResponse.from_dictionary(resp)

    def create_protection_group(
        self, body: create_protection_group_v1_request.CreateProtectionGroupV1Request = None
    ) -> create_protection_group_response.CreateProtectionGroupResponse:
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
            CreateProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/protection-groups'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_protection_group.', errors
            )
        return create_protection_group_response.CreateProtectionGroupResponse.from_dictionary(resp)

    def update_protection_group(
        self,
        group_id: str,
        body: update_protection_group_v1_request.UpdateProtectionGroupV1Request = None,
    ) -> update_protection_group_response.UpdateProtectionGroupResponse:
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
            UpdateProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.put(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_protection_group.', errors
            )
        return update_protection_group_response.UpdateProtectionGroupResponse.from_dictionary(resp)

    def delete_protection_group(self, group_id: str) -> object:
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
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/protection-groups/{group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.delete(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_protection_group.', errors
            )
        return resp

    def add_bucket_protection_group(
        self,
        group_id: str,
        body: add_bucket_protection_group_v1_request.AddBucketProtectionGroupV1Request = None,
    ) -> add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse:
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
            AddBucketToProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/protection-groups/{group_id}/buckets'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing add_bucket_protection_group.', errors
            )
        return add_bucket_to_protection_group_response.AddBucketToProtectionGroupResponse.from_dictionary(
            resp
        )

    def delete_bucket_protection_group(
        self, group_id: str, bucket_id: str
    ) -> delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse:
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
            DeleteBucketFromProtectionGroupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/protection-groups/{group_id}/buckets/{bucket_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'group_id': group_id, 'bucket_id': bucket_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/api.clumio.protection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.delete(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_bucket_protection_group.', errors
            )
        return delete_bucket_from_protection_group_response.DeleteBucketFromProtectionGroupResponse.from_dictionary(
            resp
        )
