#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_records_aws_dynamodb_table_v1_request
from clumioapi.models import restore_records_response_async
from clumioapi.models import restore_records_response_sync
import requests


class RestoredRecordsAwsDynamodbTablesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-records-aws-dynamodb-tables resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-records-aws-dynamodb-tables=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_records_aws_dynamodb_table(
        self,
        embed: str = None,
        body: restore_records_aws_dynamodb_table_v1_request.RestoreRecordsAwsDynamodbTableV1Request = None,
        **kwargs,
    ) -> Union[
        Union[
            restore_records_response_sync.RestoreRecordsResponseSync,
            restore_records_response_async.RestoreRecordsResponseAsync,
        ],
        tuple[
            requests.Response,
            Optional[
                Union[
                    restore_records_response_sync.RestoreRecordsResponseSync,
                    restore_records_response_async.RestoreRecordsResponseAsync,
                ]
            ],
        ],
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            Union[restore_records_response_sync.RestoreRecordsResponseSync, restore_records_response_async.RestoreRecordsResponseAsync]: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/dynamodb-tables/records'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_records_aws_dynamodb_table.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            if self.config.raw_response:
                return (
                    resp,
                    restore_records_response_sync.RestoreRecordsResponseSync.from_dictionary(
                        unmarshalled_dict
                    ),
                )
            return restore_records_response_sync.RestoreRecordsResponseSync.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            if self.config.raw_response:
                return (
                    resp,
                    restore_records_response_async.RestoreRecordsResponseAsync.from_dictionary(
                        unmarshalled_dict
                    ),
                )
            return restore_records_response_async.RestoreRecordsResponseAsync.from_dictionary(
                unmarshalled_dict
            )
