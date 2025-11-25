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
from clumioapi.models import create_ec2_mssql_database_restore_response
from clumioapi.models import restore_ec2_mssql_database_v1_request
import requests
import retrying


class RestoreEc2MssqlDatabaseV1Controller:
    """A Controller to access Endpoints for restore-ec2-mssql-database resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.restore-ec2-mssql-database=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def restore_ec2_mssql_database(
        self,
        embed: str | None = None,
        body: restore_ec2_mssql_database_v1_request.RestoreEc2MssqlDatabaseV1Request | None = None,
        **kwargs,
    ) -> create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse:
        """Restores an EC2 MSSQL database from a given backup or to a specified point in
        time.

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
            return create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/restores/aws/ec2-mssql/databases'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'embed': embed,
        }

        resp_instance: (
            create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse
        )
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
                f'restore_ec2_mssql_database for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class RestoreEc2MssqlDatabaseV1ControllerPaginator:
    """A Controller to access Endpoints for restore-ec2-mssql-database resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
