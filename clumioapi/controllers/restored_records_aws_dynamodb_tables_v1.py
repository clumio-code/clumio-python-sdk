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
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_records_aws_dynamodb_table_v1_request
from clumioapi.models import restore_records_response_async
from clumioapi.models import restore_records_response_sync
import requests
import retrying


class RestoredRecordsAwsDynamodbTablesV1Controller:
    """A Controller to access Endpoints for restored-records-aws-dynamodb-tables resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-records-aws-dynamodb-tables=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_records_aws_dynamodb_table(
        self,
        embed: str | None = None,
        body: (
            restore_records_aws_dynamodb_table_v1_request.RestoreRecordsAwsDynamodbTableV1Request
            | None
        ) = None,
        **kwargs,
    ) -> Union[
        restore_records_response_sync.RestoreRecordsResponseSync,
        restore_records_response_async.RestoreRecordsResponseAsync,
    ]:
        """Start a DynamoDB backup records retrieval query with the query filters provided
        in user input. If the query preview flag is set in the input then the result
        will be returned to the response otherwise the query will run in background and
        a task id will be returned.

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

        def get_instance_from_response(resp: requests.Response) -> Any:

            obj: Any

            if resp.status_code == 200:
                obj = restore_records_response_sync.RestoreRecordsResponseSync.from_response(resp)
                return obj

            if resp.status_code == 202:
                obj = restore_records_response_async.RestoreRecordsResponseAsync.from_response(resp)
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for restore_records_aws_dynamodb_table.', resp=resp
            )

        # Prepare query URL
        _url_path = '/restores/aws/dynamodb-tables/records'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: Union[
            restore_records_response_sync.RestoreRecordsResponseSync,
            restore_records_response_async.RestoreRecordsResponseAsync,
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
            error_str = f'restore_records_aws_dynamodb_table for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredRecordsAwsDynamodbTablesV1ControllerPaginator:
    """A Controller to access Endpoints for restored-records-aws-dynamodb-tables resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
