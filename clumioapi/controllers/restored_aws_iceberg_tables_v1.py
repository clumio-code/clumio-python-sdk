#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any
import urllib.parse

from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_aws_iceberg_table_response
from clumioapi.models import restore_aws_iceberg_table_v1_request
import requests


class RestoredAwsIcebergTablesV1Controller:
    """A Controller to access Endpoints for restored-aws-iceberg-tables resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restored-aws-iceberg-tables=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_aws_iceberg_table(
        self,
        body: restore_aws_iceberg_table_v1_request.RestoreAwsIcebergTableV1Request | None = None,
        **kwargs,
    ) -> restore_aws_iceberg_table_response.RestoreAWSIcebergTableResponse:
        """Restores the specified source AWS Iceberg Table snapshots to the specified
        target destination. The source AWS Iceberg Table must be one that was backed up
        by Clumio.

        Args:
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return restore_aws_iceberg_table_response.RestoreAWSIcebergTableResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/aws/iceberg-tables'

        _query_parameters: dict[str, Any] = {}

        resp_instance: restore_aws_iceberg_table_response.RestoreAWSIcebergTableResponse
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
                f'restore_aws_iceberg_table for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoredAwsIcebergTablesV1ControllerPaginator:
    """A Controller to access Endpoints for restored-aws-iceberg-tables resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
