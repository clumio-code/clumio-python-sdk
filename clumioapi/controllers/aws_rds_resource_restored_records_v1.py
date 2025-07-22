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
from clumioapi.models import list_restored_records_response
from clumioapi.models import restore_rds_record_v1_request
from clumioapi.models import restore_record_preview_response
from clumioapi.models import restore_record_response
import requests


class AwsRdsResourceRestoredRecordsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for aws-rds-resource-restored-records resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.aws-rds-resource-restored-records=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_rds_restored_records(self, limit: int, start: str, filter: str, **kwargs) -> Union[
        list_restored_records_response.ListRestoredRecordsResponse,
        tuple[
            requests.Response, Optional[list_restored_records_response.ListRestoredRecordsResponse]
        ],
    ]:
        """Returns a list of RDS database restored-records.

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

                +----------+-----+--------------------------------------+
                | asset_id | $eq | The Clumio-assigned ID of the asset. |
                +==========+=====+======================================+
                | task_id  | $in | Task IDs associated with the record. |
                +----------+-----+--------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_restored_records_response.ListRestoredRecordsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/rds-resources/records'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

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
                'Error occurred while executing list_rds_restored_records.', errors
            )

        if self.config.raw_response:
            return resp, list_restored_records_response.ListRestoredRecordsResponse.from_dictionary(
                resp.json()
            )
        return list_restored_records_response.ListRestoredRecordsResponse.from_dictionary(
            resp.json()
        )

    def restore_rds_record(
        self, embed: str, body: restore_rds_record_v1_request.RestoreRdsRecordV1Request, **kwargs
    ) -> Union[
        Union[
            restore_record_preview_response.RestoreRecordPreviewResponse,
            restore_record_response.RestoreRecordResponse,
        ],
        tuple[
            requests.Response,
            Optional[
                Union[
                    restore_record_preview_response.RestoreRecordPreviewResponse,
                    restore_record_response.RestoreRecordResponse,
                ]
            ],
        ],
    ]:
        """Start a database backup query with the query statement provided in user input.
        If the query preview flag is set in the input then the result will be returned
        in the response otherwise the query will run in background and a task id will be
        returned.

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
            Union[restore_record_preview_response.RestoreRecordPreviewResponse, restore_record_response.RestoreRecordResponse]: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/rds-resources/records'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

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
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_rds_record.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            if self.config.raw_response:
                return (
                    resp,
                    restore_record_preview_response.RestoreRecordPreviewResponse.from_dictionary(
                        unmarshalled_dict
                    ),
                )
            return restore_record_preview_response.RestoreRecordPreviewResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            if self.config.raw_response:
                return resp, restore_record_response.RestoreRecordResponse.from_dictionary(
                    unmarshalled_dict
                )
            return restore_record_response.RestoreRecordResponse.from_dictionary(unmarshalled_dict)
        raise RuntimeError(
            f'Code should be unreachable; Unexpected response code: {resp.status_code}. '
        )
