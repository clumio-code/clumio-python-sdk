#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_connection_groups_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_aws_connection_group_v1_request
from clumioapi.models import create_connection_group_response
from clumioapi.models import list_connection_groups_response
from clumioapi.models import read_connection_group_response
from clumioapi.models import update_aws_connection_group_v1_request
from clumioapi.models import update_connection_group_response
import requests


class AwsConnectionGroupsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-connection-groups resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-connection-groups=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_aws_connection_groups(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_connection_groups_types.ListAwsConnectionGroupsV1FilterT | None = None,
        **kwargs,
    ) -> list_connection_groups_response.ListConnectionGroupsResponse:
        """Returns a list of active connection groups that are managing AWS account
        connections.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | account_native_id      | $in              | The AWS account ID that belongs  |
                |                        |                  | to a connection group to be      |
                |                        |                  | searched.                        |
                |                        |                  |                                  |
                |                        |                  | {"account_native_id":{"$in":["11 |
                |                        |                  | 1111111111", "222222222222"]}}   |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $in              | Lists connection groups in the   |
                |                        |                  | specified organizational units.  |
                |                        |                  |                                  |
                |                        |                  | {"organizational_unit_id":{"$in" |
                |                        |                  | :["ca849d10-7ea1-4869-b2d0-      |
                |                        |                  | 46c42b5f2bea", "27b9ee09-c59c-   |
                |                        |                  | 466f-b2c4-223e9h8df7c8"]}}       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | account_alias          | $contains        | A substring within the account   |
                |                        |                  | alias (if available) to search   |
                |                        |                  | for.                             |
                |                        |                  |                                  |
                |                        |                  | {"account_alias":{"$contains":"f |
                |                        |                  | oo"}}                            |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | services_enabled       | $contains, $eq   | Lists the connection groups that |
                |                        |                  | have at least these asset_types  |
                |                        |                  | enabled or groups that have the  |
                |                        |                  | exact asset_types enabled.       |
                |                        |                  | Supported types are: ['rds',     |
                |                        |                  | 's3', 'ebs',                     |
                |                        |                  | 'ec2mssql','dynamodb',           |
                |                        |                  | 'iceberg_on_glue'].              |
                |                        |                  |                                  |
                |                        |                  | {"services_enabled":{"$contains" |
                |                        |                  | :["rds"]}}                       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                |                        |                  | {"services_enabled":{"$eq":["rds |
                |                        |                  | "]}}                             |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_connection_groups_response.ListConnectionGroupsResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws/connection-groups'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_connection_groups_response.ListConnectionGroupsResponse
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
                f'list_aws_connection_groups for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_aws_connection_group(
        self,
        body: (
            create_aws_connection_group_v1_request.CreateAwsConnectionGroupV1Request | None
        ) = None,
        **kwargs,
    ) -> create_connection_group_response.CreateConnectionGroupResponse:
        """Initiates a new connection group request, and in response returns a URL under
        field "deployment_template_url". Upon successfully deploying the cloudformation
        template
        retrieved from the URL in the AWS account, the connection-group is created or
        the request is discarded.

        NOTE - The lifecycle of a connection-group is governed by its CloudFormation
        stack. If the CFT for a connection-group is deleted from AWS, the connection-
        group is automatically deleted.
        The deletion does not affect any backups taken nor any connections it managed.

        Args:
            body:
                The body of the request.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return create_connection_group_response.CreateConnectionGroupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws/connection-groups'

        _query_parameters: dict[str, Any] = {}

        resp_instance: create_connection_group_response.CreateConnectionGroupResponse
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
                f'create_aws_connection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_connection_group(
        self,
        connection_group_id: str | None = None,
        embed: str | None = None,
        return_external_id: bool | None = None,
        **kwargs,
    ) -> read_connection_group_response.ReadConnectionGroupResponse:
        """Returns a representation of the specified connection group with the given ID.

        Args:
            connection_group_id:
                Performs the operation on the connection group with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------+---------------------------------------------------+
                |     Embeddable Link      |                    Description                    |
                +==========================+===================================================+
                | read-organizational-unit | Embeds the associated organizational unit in the  |
                |                          | response. For example, embed=read-organizational- |
                |                          | unit                                              |
                +--------------------------+---------------------------------------------------+

            return_external_id:
                If passed as true, then the API returns an externalId for the connection group.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_connection_group_response.ReadConnectionGroupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws/connection-groups/{connection_group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_group_id': connection_group_id}
        )
        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed, 'return_external_id': return_external_id}

        resp_instance: read_connection_group_response.ReadConnectionGroupResponse
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
                f'read_aws_connection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_aws_connection_group(
        self,
        connection_group_id: str | None = None,
        body: (
            update_aws_connection_group_v1_request.UpdateAwsConnectionGroupV1Request | None
        ) = None,
        **kwargs,
    ) -> update_connection_group_response.UpdateConnectionGroupResponse:
        """Initiates an update to a connection group, and in response returns a URL under
        field "deployment_template_url". Upon successfully updating the connection-
        group's stack with the cloudformation template
        retrieved from the URL, the connection-group update completes or the request is
        discarded.

        NOTE - The lifecycle of a connection-group is governed by its CloudFormation
        stack. If the CFT for a connection-group is deleted from AWS, the connection-
        group is automatically deleted.
        The deletion does not affect any backups taken nor any connections it managed.

        Args:
            connection_group_id:
                Updates the connection with the specified path
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return update_connection_group_response.UpdateConnectionGroupResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/connections/aws/connection-groups/{connection_group_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'connection_group_id': connection_group_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: update_connection_group_response.UpdateConnectionGroupResponse
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
            error_str = (
                f'update_aws_connection_group for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsConnectionGroupsV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for aws-connection-groups resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = AwsConnectionGroupsV1Controller(config)

    def list_aws_connection_groups(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: aws_connection_groups_types.ListAwsConnectionGroupsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_connection_groups_response.ListConnectionGroupsResponse]:
        """Returns a list of active connection groups that are managing AWS account
        connections.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +------------------------+------------------+----------------------------------+
                |         Field          | Filter Condition |           Description            |
                +========================+==================+==================================+
                | account_native_id      | $in              | The AWS account ID that belongs  |
                |                        |                  | to a connection group to be      |
                |                        |                  | searched.                        |
                |                        |                  |                                  |
                |                        |                  | {"account_native_id":{"$in":["11 |
                |                        |                  | 1111111111", "222222222222"]}}   |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | organizational_unit_id | $in              | Lists connection groups in the   |
                |                        |                  | specified organizational units.  |
                |                        |                  |                                  |
                |                        |                  | {"organizational_unit_id":{"$in" |
                |                        |                  | :["ca849d10-7ea1-4869-b2d0-      |
                |                        |                  | 46c42b5f2bea", "27b9ee09-c59c-   |
                |                        |                  | 466f-b2c4-223e9h8df7c8"]}}       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | account_alias          | $contains        | A substring within the account   |
                |                        |                  | alias (if available) to search   |
                |                        |                  | for.                             |
                |                        |                  |                                  |
                |                        |                  | {"account_alias":{"$contains":"f |
                |                        |                  | oo"}}                            |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+
                | services_enabled       | $contains, $eq   | Lists the connection groups that |
                |                        |                  | have at least these asset_types  |
                |                        |                  | enabled or groups that have the  |
                |                        |                  | exact asset_types enabled.       |
                |                        |                  | Supported types are: ['rds',     |
                |                        |                  | 's3', 'ebs',                     |
                |                        |                  | 'ec2mssql','dynamodb',           |
                |                        |                  | 'iceberg_on_glue'].              |
                |                        |                  |                                  |
                |                        |                  | {"services_enabled":{"$contains" |
                |                        |                  | :["rds"]}}                       |
                |                        |                  |                                  |
                |                        |                  |                                  |
                |                        |                  | {"services_enabled":{"$eq":["rds |
                |                        |                  | "]}}                             |
                |                        |                  |                                  |
                |                        |                  |                                  |
                +------------------------+------------------+----------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_aws_connection_groups(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
