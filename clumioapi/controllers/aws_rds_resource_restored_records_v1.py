#
# Copyright 2021. Clumio, Inc.
#

import json

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

    def list_rds_restored_records(
        self, limit: int = None, start: str = None, filter: str = None
    ) -> list_restored_records_response.ListRestoredRecordsResponse:
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
            list_restored_records_response.ListRestoredRecordsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/aws/rds-resources/records'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_rds_restored_records.', errors
            )

        return list_restored_records_response.ListRestoredRecordsResponse.from_dictionary(resp)

    def restore_rds_record(
        self,
        embed: str = None,
        body: restore_rds_record_v1_request.RestoreRdsRecordV1Request = None,
    ) -> restore_record_preview_response.RestoreRecordPreviewResponse | restore_record_response.RestoreRecordResponse:
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
            restore_record_preview_response.RestoreRecordPreviewResponse | restore_record_response.RestoreRecordResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/aws/rds-resources/records'

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
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_rds_record.', errors
            )
        unmarshalled_dict = json.loads(resp.text)
        if resp.status_code == 200:
            return restore_record_preview_response.RestoreRecordPreviewResponse.from_dictionary(
                unmarshalled_dict
            )
        if resp.status_code == 202:
            return restore_record_response.RestoreRecordResponse.from_dictionary(unmarshalled_dict)
