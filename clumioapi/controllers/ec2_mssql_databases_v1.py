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
from clumioapi.controllers.types import ec2_mssql_databases_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_ec2_mssql_database_pitr_intervals_response
from clumioapi.models import list_ec2_mssql_databases_response
from clumioapi.models import read_ec2_mssql_database_response
import requests
import retrying


class Ec2MssqlDatabasesV1Controller:
    """A Controller to access Endpoints for ec2-mssql-databases resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.ec2-mssql-databases=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_ec2_mssql_databases(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_databases_types.ListEc2MssqlDatabasesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_ec2_mssql_databases_response.ListEC2MSSQLDatabasesResponse:
        """Returns a list of Databases

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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | name                      | $contains        | Filter database where given   |
                |                           |                  | string is a substring of the  |
                |                           |                  | name.                         |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter database whose         |
                |                           |                  | policy_id is equal to the     |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter database whose         |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter database which is      |
                |                           |                  | protected by deactivated      |
                |                           |                  | policy or not.                |
                +---------------------------+------------------+-------------------------------+
                | instance_id               | $eq              | Filter database whose         |
                |                           |                  | instance ID is equal to the   |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | host_id                   | $eq              | Filter database whose host ID |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | availability_group_id     | $eq              | Filter database whose         |
                |                           |                  | availability group ID is      |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | failover_cluster_id       | $eq              | Filter database whose         |
                |                           |                  | failover cluster ID is equal  |
                |                           |                  | to the given string.          |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | recovery_model            | $in              | Filter database whose         |
                |                           |                  | recovery_model is in the      |
                |                           |                  | given array of string         |
                +---------------------------+------------------+-------------------------------+
                | type                      | $eq              | Filter database whose type is |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | account_ids               | $in              | Filter databases which belong |
                |                           |                  | to any one or more of the     |
                |                           |                  | accounts in the list of       |
                |                           |                  | account_ids.                  |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources will not have  |
                |                        | an associated policy. For example, embed=read-      |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+
                | read-aws-environment   | Embeds the associated AWS Environment details in    |
                |                        | the response. For example, embed=read-aws-          |
                |                        | environment                                         |
                +------------------------+-----------------------------------------------------+
                | read-aws-ec2-instance  | Embeds the associated AWS EC2 Instance in the       |
                |                        | response. For example, embed=read-aws-ec2-instance  |
                +------------------------+-----------------------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_ec2_mssql_databases_response.ListEC2MSSQLDatabasesResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/databases'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_ec2_mssql_databases_response.ListEC2MSSQLDatabasesResponse
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
            error_str = f'list_ec2_mssql_databases for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_ec2_mssql_database(
        self, database_id: str | None = None, lookback_days: int | None = None, **kwargs
    ) -> read_ec2_mssql_database_response.ReadEC2MSSQLDatabaseResponse:
        """Returns a representation of the specified database.

        Args:
            database_id:
                Performs the operation on a database within the specified database id.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_ec2_mssql_database_response.ReadEC2MSSQLDatabaseResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/databases/{database_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'database_id': database_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'lookback_days': lookback_days,
        }

        resp_instance: read_ec2_mssql_database_response.ReadEC2MSSQLDatabaseResponse
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
            error_str = f'read_ec2_mssql_database for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_ec2_mssql_database_pitr_intervals(
        self,
        database_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_databases_types.ListEc2MssqlDatabasePitrIntervalsV1FilterT | None = None,
        **kwargs,
    ) -> list_ec2_mssql_database_pitr_intervals_response.ListEC2MssqlDatabasePitrIntervalsResponse:
        """Returns a list of time intervals (start timestamp and end timestamp) in which
        the MSSQL database can be restored.

        Args:
            database_id:
                Performs the operation on a database within the specified database id.
            limit:
                Limits the size of the items returned in the response.
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

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_ec2_mssql_database_pitr_intervals_response.ListEC2MssqlDatabasePitrIntervalsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/datasources/aws/ec2-mssql/databases/{database_id}/pitr-intervals'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'database_id': database_id}
        )

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: (
            list_ec2_mssql_database_pitr_intervals_response.ListEC2MssqlDatabasePitrIntervalsResponse
        )
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
            error_str = f'list_ec2_mssql_database_pitr_intervals for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class Ec2MssqlDatabasesV1ControllerPaginator:
    """A Controller to access Endpoints for ec2-mssql-databases resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_ec2_mssql_databases(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_databases_types.ListEc2MssqlDatabasesV1FilterT | None = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_mssql_databases_response.ListEC2MSSQLDatabasesResponse]:
        """Returns a list of Databases

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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | name                      | $contains        | Filter database where given   |
                |                           |                  | string is a substring of the  |
                |                           |                  | name.                         |
                +---------------------------+------------------+-------------------------------+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | Filter database whose         |
                |                           |                  | policy_id is equal to the     |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $eq              | Filter database whose         |
                |                           |                  | protection_status is equal to |
                |                           |                  | the given string.             |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter database which is      |
                |                           |                  | protected by deactivated      |
                |                           |                  | policy or not.                |
                +---------------------------+------------------+-------------------------------+
                | instance_id               | $eq              | Filter database whose         |
                |                           |                  | instance ID is equal to the   |
                |                           |                  | given string.                 |
                +---------------------------+------------------+-------------------------------+
                | host_id                   | $eq              | Filter database whose host ID |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | availability_group_id     | $eq              | Filter database whose         |
                |                           |                  | availability group ID is      |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | failover_cluster_id       | $eq              | Filter database whose         |
                |                           |                  | failover cluster ID is equal  |
                |                           |                  | to the given string.          |
                +---------------------------+------------------+-------------------------------+
                | status                    | $eq              | Filter database whose status  |
                |                           |                  | is equal to the given string. |
                +---------------------------+------------------+-------------------------------+
                | recovery_model            | $in              | Filter database whose         |
                |                           |                  | recovery_model is in the      |
                |                           |                  | given array of string         |
                +---------------------------+------------------+-------------------------------+
                | type                      | $eq              | Filter database whose type is |
                |                           |                  | equal to the given string.    |
                +---------------------------+------------------+-------------------------------+
                | account_ids               | $in              | Filter databases which belong |
                |                           |                  | to any one or more of the     |
                |                           |                  | accounts in the list of       |
                |                           |                  | account_ids.                  |
                +---------------------------+------------------+-------------------------------+

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the definition of the policy associated with |
                |                        | this resource. Unprotected resources will not have  |
                |                        | an associated policy. For example, embed=read-      |
                |                        | policy-definition                                   |
                +------------------------+-----------------------------------------------------+
                | read-aws-environment   | Embeds the associated AWS Environment details in    |
                |                        | the response. For example, embed=read-aws-          |
                |                        | environment                                         |
                +------------------------+-----------------------------------------------------+
                | read-aws-ec2-instance  | Embeds the associated AWS EC2 Instance in the       |
                |                        | response. For example, embed=read-aws-ec2-instance  |
                +------------------------+-----------------------------------------------------+

            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = Ec2MssqlDatabasesV1Controller(self.controller)
        while True:
            response = controller.list_ec2_mssql_databases(
                limit=limit,
                start=start,
                filter=filter,
                embed=embed,
                lookback_days=lookback_days,
                **kwargs,
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

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_ec2_mssql_database_pitr_intervals(
        self,
        database_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: ec2_mssql_databases_types.ListEc2MssqlDatabasePitrIntervalsV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[
        list_ec2_mssql_database_pitr_intervals_response.ListEC2MssqlDatabasePitrIntervalsResponse
    ]:
        """Returns a list of time intervals (start timestamp and end timestamp) in which
        the MSSQL database can be restored.

        Args:
            database_id:
                Performs the operation on a database within the specified database id.
            limit:
                Limits the size of the items returned in the response.
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

        """
        controller = Ec2MssqlDatabasesV1Controller(self.controller)
        while True:
            response = controller.list_ec2_mssql_database_pitr_intervals(
                database_id=database_id, limit=limit, start=start, filter=filter, **kwargs
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
