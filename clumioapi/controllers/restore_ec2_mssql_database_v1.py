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
from clumioapi.models import create_ec2_mssql_database_restore_response
from clumioapi.models import restore_ec2_mssql_database_v1_request
import requests


class RestoreEc2MssqlDatabaseV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restore-ec2-mssql-database resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restore-ec2-mssql-database=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_ec2_mssql_database(
        self,
        embed: str | None = None,
        body: restore_ec2_mssql_database_v1_request.RestoreEc2MssqlDatabaseV1Request | None = None,
        **kwargs,
    ) -> Union[
        create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse,
        tuple[
            requests.Response,
            Optional[
                create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse
            ],
        ],
    ]:
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/restores/aws/ec2-mssql/databases'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        raw_response = self.config.raw_response
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
            if raw_response:
                return http_error.response, None
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_ec2_mssql_database', error=http_error
            )

        obj = create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse.from_dictionary(
            resp.json()
        )
        if raw_response:
            return resp, obj
        return obj
