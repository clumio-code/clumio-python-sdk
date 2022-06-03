#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_mssql_database_pitr_intervals_response
from clumioapi.models import list_mssql_databases_response
from clumioapi.models import read_mssql_database_response
import requests


class MssqlDatabasesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for mssql-databases resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.mssql-databases=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }

    def list_mssql_databases(
        self, limit: int = None, start: str = None, filter: str = None, embed: str = None
    ) -> list_mssql_databases_response.ListMssqlDatabasesResponse:
        """Returns a list of Databases

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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | name                      | $contains        | Filter Database where given   |
                |                           |                  | string is a substring of the  |
                |                           |                  | name.                         |
                +---------------------------+------------------+-------------------------------+
                | group_id                  | $eq              | Filter Database where given   |
                |                           |                  | string is a equal to the      |
                |                           |                  | group_id.                     |
                +---------------------------+------------------+-------------------------------+
                | subgroup_id               | $eq              | Filter Database where given   |
                |                           |                  | string is a equal to the      |
                |                           |                  | subgroup_id.                  |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter Database whose         |
                |                           |                  | policy_id is equal to the     |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter Database whose         |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | compliance_status         | $in              | Filter Database whose         |
                |                           |                  | compliance_status is in the   |
                |                           |                  | given array of string.        |
                +---------------------------+------------------+-------------------------------+
                | instance_id               | $eq              | Filter Database whose         |
                |                           |                  | instance id is equal to the   |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | host_id                   | $eq              | Filter Database whose host id |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | availability_group_id     | $eq              | Filter Database whose         |
                |                           |                  | availability group id is      |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter Database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | recovery_model            | $in              | Filter Database whose         |
                |                           |                  | recovery_model is in the      |
                |                           |                  | given array of string         |
                +---------------------------+------------------+-------------------------------+
                | type                      | $eq              | Filter Database whose type is |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +--------------------------+---------------------------------------------------+
                |     Embeddable Link      |                    Description                    |
                +==========================+===================================================+
                | read-management-group    | Embeds the associated management group details    |
                |                          | in the response. For example, embed=read-         |
                |                          | management-group                                  |
                +--------------------------+---------------------------------------------------+
                | read-management-subgroup | Embeds the associated management subgroup         |
                |                          | details in the response. For example, embed=read- |
                |                          | management-subgroup                               |
                +--------------------------+---------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
        Returns:
            ListMssqlDatabasesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/databases'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_databases.', errors
            )
        return list_mssql_databases_response.ListMssqlDatabasesResponse.from_dictionary(resp)

    def read_mssql_databases(
        self, database_id: str
    ) -> read_mssql_database_response.ReadMssqlDatabaseResponse:
        """Returns a representation of the specified database.

        Args:
            database_id:
                Performs the operation on a database within the specified database id.
        Returns:
            ReadMssqlDatabaseResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/mssql/databases/{database_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'database_id': database_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_mssql_databases.', errors
            )
        return read_mssql_database_response.ReadMssqlDatabaseResponse.from_dictionary(resp)

    def list_mssql_database_pitr_intervals(
        self, database_id: str, limit: int = None, start: str = None, filter: str = None
    ) -> list_mssql_database_pitr_intervals_response.ListMssqlDatabasePitrIntervalsResponse:
        """Returns restorable times as a list of intervals.

        Args:
            database_id:
                Performs the operation on a database within the specified database id.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page token used to browse the collection. Leave this parameter empty to
                get the first page.
                Other pages can be traversed using HATEOAS links.
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------+------------------+-----------------------------------------------+
                |   Field   | Filter Condition |                  Description                  |
                +===========+==================+===============================================+
                | timestamp | $lte, $gt        | Filter pitr intervals whose range is "less    |
                |           |                  | than or equal to" or                          |
                |           |                  | "greater than" a given timestamp.             |
                +-----------+------------------+-----------------------------------------------+

        Returns:
            ListMssqlDatabasePitrIntervalsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/mssql/databases/{database_id}/pitr-intervals'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'database_id': database_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_mssql_database_pitr_intervals.', errors
            )
        return list_mssql_database_pitr_intervals_response.ListMssqlDatabasePitrIntervalsResponse.from_dictionary(
            resp
        )
