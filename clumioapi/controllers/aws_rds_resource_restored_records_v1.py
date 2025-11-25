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
from clumioapi.controllers.types import aws_rds_resource_restored_records_types
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_restored_records_response
from clumioapi.models import restore_rds_record_v1_request
from clumioapi.models import restore_record_preview_response
from clumioapi.models import restore_record_response
import requests
import retrying


class AwsRdsResourceRestoredRecordsV1Controller:
    """A Controller to access Endpoints for aws-rds-resource-restored-records resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-rds-resource-restored-records=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_rds_restored_records(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            aws_rds_resource_restored_records_types.ListRdsRestoredRecordsV1FilterT | None
        ) = None,
        **kwargs,
    ) -> list_restored_records_response.ListRestoredRecordsResponse:
        """Returns a list of RDS database restored-records.

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_restored_records_response.ListRestoredRecordsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/restores/aws/rds-resources/records'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_restored_records_response.ListRestoredRecordsResponse
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
                f'list_rds_restored_records for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def restore_rds_record(
        self,
        embed: str | None = None,
        body: restore_rds_record_v1_request.RestoreRdsRecordV1Request | None = None,
        **kwargs,
    ) -> Union[
        restore_record_preview_response.RestoreRecordPreviewResponse,
        restore_record_response.RestoreRecordResponse,
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:

            obj: Any

            if resp.status_code == 200:
                obj = restore_record_preview_response.RestoreRecordPreviewResponse.from_response(
                    resp
                )
                return obj

            if resp.status_code == 202:
                obj = restore_record_response.RestoreRecordResponse.from_response(resp)
                return obj

            raise clumio_exception.ClumioException(
                f'Unexpected response code for restore_rds_record.', resp=resp
            )

        # Prepare query URL
        _url_path = '/restores/aws/rds-resources/records'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: Union[
            restore_record_preview_response.RestoreRecordPreviewResponse,
            restore_record_response.RestoreRecordResponse,
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
            error_str = f'restore_rds_record for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsRdsResourceRestoredRecordsV1ControllerPaginator:
    """A Controller to access Endpoints for aws-rds-resource-restored-records resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_rds_restored_records(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            aws_rds_resource_restored_records_types.ListRdsRestoredRecordsV1FilterT | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_restored_records_response.ListRestoredRecordsResponse]:
        """Returns a list of RDS database restored-records.

        Args:
            limit:
                Limits the size of the items returned in the response.
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

        """
        controller = AwsRdsResourceRestoredRecordsV1Controller(self.controller)
        while True:
            response = controller.list_rds_restored_records(
                limit=limit, start=start, filter=filter, **kwargs
            )
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
