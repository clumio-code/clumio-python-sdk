#
# Copyright 2021. Clumio, Inc.
#

import json

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
        embed: str = None,
        body: restore_ec2_mssql_database_v1_request.RestoreEc2MssqlDatabaseV1Request = None,
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

        Returns:
            create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/aws/ec2-mssql/databases'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_ec2_mssql_database.', errors
            )

        return create_ec2_mssql_database_restore_response.CreateEC2MSSQLDatabaseRestoreResponse.from_dictionary(
            resp
        )
