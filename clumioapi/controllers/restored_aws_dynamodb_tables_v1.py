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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_aws_dynamodb_table_v1_request
from clumioapi.models import restore_dynamo_db_table_response
import requests


class RestoredAwsDynamodbTablesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-dynamodb-tables resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-dynamodb-tables=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_aws_dynamodb_table(
        self,
        embed: str | None = None,
        body: restore_aws_dynamodb_table_v1_request.RestoreAwsDynamodbTableV1Request | None = None,
        **kwargs,
    ) -> restore_dynamo_db_table_response.RestoreDynamoDBTableResponse:
        """Restores the specified DynamoDB table backup to the specified target
        destination.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return restore_dynamo_db_table_response.RestoreDynamoDBTableResponse.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/restores/aws/dynamodb-tables'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: restore_dynamo_db_table_response.RestoreDynamoDBTableResponse
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
                f'restore_aws_dynamodb_table for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsDynamodbTablesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for restored-aws-dynamodb-tables resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = RestoredAwsDynamodbTablesV1Controller(config)
