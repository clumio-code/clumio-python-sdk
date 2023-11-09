#
# Copyright 2023. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_mssql_database_restore_response
from clumioapi.models import restore_mssql_database_v1_request
import requests


class RestoredMssqlDatabasesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-mssql-databases resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.restored-mssql-databases=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def restore_mssql_database(
        self,
        embed: str = None,
        body: restore_mssql_database_v1_request.RestoreMssqlDatabaseV1Request = None,
        **kwargs,
    ) -> Union[
        create_mssql_database_restore_response.CreateMssqlDatabaseRestoreResponse,
        tuple[
            requests.Response,
            Optional[create_mssql_database_restore_response.CreateMssqlDatabaseRestoreResponse],
        ],
    ]:
        """Creates a restored MSSQL database from a given backup or to a specified point in
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
            create_mssql_database_restore_response.CreateMssqlDatabaseRestoreResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/mssql/databases'

        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_mssql_database.', errors
            )

        if self.config.raw_response:
            return (
                resp,
                create_mssql_database_restore_response.CreateMssqlDatabaseRestoreResponse.from_dictionary(
                    resp.json()
                ),
            )
        return create_mssql_database_restore_response.CreateMssqlDatabaseRestoreResponse.from_dictionary(
            resp
        )
