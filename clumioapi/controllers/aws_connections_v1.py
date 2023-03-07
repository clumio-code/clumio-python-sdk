#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_aws_connection_response
from clumioapi.models import create_aws_connection_v1_request
from clumioapi.models import list_aws_connections_response
from clumioapi.models import read_aws_connection_response
from clumioapi.models import update_aws_connection_response
from clumioapi.models import update_aws_connection_v1_request
import requests


class AwsConnectionsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-connections resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-connections=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_connections(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_aws_connections_response.ListAWSConnectionsResponse:
        """Returns a list of AWS Connections

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +------------------------+-------------------+---------------------------------+
                |         Field          | Filter Condition  |           Description           |
                +========================+===================+=================================+
                | account_native_id      | $begins_with, $in | A prefix of the account ID to   |
                |                        |                   | search for or the list of       |
                |                        |                   | account IDs to return.          |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$begins_ |
                |                        |                   | with":"23345"}}                 |
                |                        |                   |                                 |
                |                        |                   |                                 |
                |                        |                   | {"account_native_id":{"$in":["1 |
                |                        |                   | 11111111111", "222222222222"]}} |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | account_alias          | $contains         | A substring within the account  |
                |                        |                   | alias (if available) to search  |
                |                        |                   | for.                            |
                |                        |                   |                                 |
                |                        |                   | {"account_alias":{"$contains":" |
                |                        |                   | foo"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_type        | $eq               | A connection type to search     |
                |                        |                   | for. Supported types are:       |
                |                        |                   | ['discover', 'protect'].        |
                |                        |                   |                                 |
                |                        |                   | {"connection_type":{"$eq":"prot |
                |                        |                   | ect"}}                          |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | connection_status      | $eq, $in          | The status of the connection to |
                |                        |                   | the environment, which is       |
                |                        |                   | mediated by a CloudFormation    |
                |                        |                   | stack. Possible values include  |
                |                        |                   | "connecting", "connected",      |
                |                        |                   | "unlinked". For example,        |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | eq":"connected"}}               |
                |                        |                   | filter={"connection_status":{"$ |
                |                        |                   | in":["unlinked","connected"]}}  |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | organizational_unit_id | $in               | Lists the connections in the    |
                |                        |                   | specified organizational units. |
                |                        |                   |                                 |
                |                        |                   | {"organizational_unit_id":{"$in |
                |                        |                   | ":["ca849d10-7ea1-4869-b2d0-    |
                |                        |                   | 46c42b5f2bea", "27b9ee09-c59c-  |
                |                        |                   | 466f-b2c4-223e9h8df7c8"]}}      |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+
                | services_enabled       | $contains         | Lists the connections that have |
                |                        |                   | the given asset_types enabled.  |
                |                        |                   | Supported types are: ['rds',    |
                |                        |                   | 's3', 'ebs', 'ec2mssql'].       |
                |                        |                   |                                 |
                |                        |                   | {"services_enabled":{"$contains |
                |                        |                   | ":"rds"}}                       |
                |                        |                   |                                 |
                |                        |                   |                                 |
                +------------------------+-------------------+---------------------------------+

        Returns:
            list_aws_connections_response.ListAWSConnectionsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_aws_connections.', errors
            )

        return list_aws_connections_response.ListAWSConnectionsResponse.from_dictionary(resp)

    def create_aws_connection(
        self, body: create_aws_connection_v1_request.CreateAwsConnectionV1Request = None
    ) -> create_aws_connection_response.CreateAWSConnectionResponse:
        """Initiate a new AWS connection.

        Args:
            body:

        Returns:
            create_aws_connection_response.CreateAWSConnectionResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws'

        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_aws_connection.', errors
            )

        return create_aws_connection_response.CreateAWSConnectionResponse.from_dictionary(resp)

    def read_aws_connection(
        self, connection_id: str
    ) -> read_aws_connection_response.ReadAWSConnectionResponse:
        """Returns a representation of the specified AWS connection.

        Args:
            connection_id:
                Performs the operation on the AWS connection with the specified ID.
        Returns:
            read_aws_connection_response.ReadAWSConnectionResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_aws_connection.', errors
            )

        return read_aws_connection_response.ReadAWSConnectionResponse.from_dictionary(resp)

    def delete_aws_connection(self, connection_id: str) -> object:
        """Delete the specified AWS connection.

        Args:
            connection_id:
                Performs the operation on the AWS connection with the specified ID.
        Returns:
            object: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.delete(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing delete_aws_connection.', errors
            )

        return resp

    def update_aws_connection(
        self,
        connection_id: str,
        body: update_aws_connection_v1_request.UpdateAwsConnectionV1Request = None,
    ) -> update_aws_connection_response.UpdateAWSConnectionResponse:
        """Returns a new template url for the specified configuration.

        Args:
            connection_id:
                Updates the connection with the specified connection ID
            body:

        Returns:
            update_aws_connection_response.UpdateAWSConnectionResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/connections/aws/{connection_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_id': connection_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_aws_connection.', errors
            )

        return update_aws_connection_response.UpdateAWSConnectionResponse.from_dictionary(resp)
