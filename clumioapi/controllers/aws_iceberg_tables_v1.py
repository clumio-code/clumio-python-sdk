#
# Copyright 2023. Clumio, A Commvault Company.
#

import re
from typing import Any, Iterator
import urllib.parse

from clumioapi import api_helper
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_iceberg_tables_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_iceberg_tables_response
from clumioapi.models import read_iceberg_table_response
import requests
import retrying


class AwsIcebergTablesV1Controller:
    """A Controller to access Endpoints for aws-iceberg-tables resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.aws-iceberg-tables=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_aws_iceberg_tables(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            aws_iceberg_tables_types.ListAwsIcebergTablesV1FilterT
            | aws_iceberg_tables_types.ListAwsIcebergTablesV1FilterTypeDef
            | None
        ) = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> list_iceberg_tables_response.ListIcebergTablesResponse:
        """Returns a list of Iceberg Tables.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following
                table lists the supported filter fields for this resource and the filter
                conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include                       |
                |                           |                  | protected, unprotected, and   |
                |                           |                  | unsupported.                  |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active         |
                |                           |                  | Iceberg tables. filter={"is_d |
                |                           |                  | eleted":{"$in":["true","false |
                |                           |                  | "]}}                          |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq,$in          | The AWS-assigned ID of the    |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$in":["789901323485"]}}      |
                |                           |                  | retrieves                     |
                |                           |                  | Iceberg tables across all     |
                |                           |                  | regions in account            |
                |                           |                  | 789901323485.                 |
                +---------------------------+------------------+-------------------------------+
                | table_name                | $contains,$eq    | The name of the table. For    |
                |                           |                  | example,                      |
                |                           |                  | filter={"table_name":{"$conta |
                |                           |                  | ins":"dev"}} retrieves all    |
                |                           |                  | Iceberg tables                |
                |                           |                  | with "dev" in their name.     |
                +---------------------------+------------------+-------------------------------+
                | catalog_type              | $in              | The type of catalog. Possible |
                |                           |                  | values include                |
                |                           |                  | aws_iceberg_glue_table and    |
                |                           |                  | aws_iceberg_s3_table. For     |
                |                           |                  | example,                      |
                |                           |                  | filter={"catalog_type":{"$in" |
                |                           |                  | :["aws_iceberg_glue_table"]}} |
                |                           |                  | retrieves all                 |
                |                           |                  | Iceberg tables whose catalog  |
                |                           |                  | type is Glue.                 |
                +---------------------------+------------------+-------------------------------+
                | catalog                   | $contains,$eq    | The name of the catalog. For  |
                |                           |                  | example,                      |
                |                           |                  | filter={"catalog":{"$contains |
                |                           |                  | ":"dev"}} retrieves all       |
                |                           |                  | Iceberg tables                |
                |                           |                  | in the catalog containing     |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | namespace                 | $contains,$eq    | For example,                  |
                |                           |                  | filter={"namespace":{"$contai |
                |                           |                  | ns":"dev"}} retrieves all     |
                |                           |                  | Iceberg tables                |
                |                           |                  | in the namespace containing   |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The Clumio-assigned ID(s) of  |
                |                           |                  | AWS tag(s) applied to this    |
                |                           |                  | resource. For example,        |
                |                           |                  | filter={"tags.id":{"$all":["c |
                |                           |                  | 764b152-5819-11ea-bb9f-       |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                |                           |                  | retrieves all Iceberg tables  |
                |                           |                  | that are associated with the  |
                |                           |                  | 2 AWS tags identified by      |
                |                           |                  | these                         |
                |                           |                  | IDs. If multiple tags are     |
                |                           |                  | specified, all of them must   |
                |                           |                  | be applied to the same        |
                |                           |                  | Iceberg                       |
                |                           |                  | table.                        |
                +---------------------------+------------------+-------------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected Iceberg |
                |                        | Table into the response. For                        |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_iceberg_tables_response.ListIcebergTablesResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/iceberg-tables'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': api_helper.to_filter_query_str(
                filter, aws_iceberg_tables_types.ListAwsIcebergTablesV1FilterT
            ),
            'embed': embed,
            'lookback_days': lookback_days,
        }

        resp_instance: list_iceberg_tables_response.ListIcebergTablesResponse
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
            error_str = f'list_aws_iceberg_tables for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_aws_iceberg_table(
        self,
        table_id: str | None = None,
        lookback_days: int | None = None,
        embed: str | None = None,
        **kwargs,
    ) -> read_iceberg_table_response.ReadIcebergTableResponse:
        """Returns a representation of the specified Iceberg Table.

        Args:
            table_id:
                Performs the operation on the table with the specified ID.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected Iceberg |
                |                        | table into the response. For                        |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_iceberg_table_response.ReadIcebergTableResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/datasources/aws/iceberg-tables/{table_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'table_id': table_id}
        )

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'lookback_days': lookback_days,
            'embed': embed,
        }

        resp_instance: read_iceberg_table_response.ReadIcebergTableResponse
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
            error_str = f'read_aws_iceberg_table for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class AwsIcebergTablesV1ControllerPaginator:
    """A Controller to access Endpoints for aws-iceberg-tables resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_aws_iceberg_tables(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            aws_iceberg_tables_types.ListAwsIcebergTablesV1FilterT
            | aws_iceberg_tables_types.ListAwsIcebergTablesV1FilterTypeDef
            | None
        ) = None,
        embed: str | None = None,
        lookback_days: int | None = None,
        **kwargs,
    ) -> Iterator[list_iceberg_tables_response.ListIcebergTablesResponse]:
        """Returns a list of Iceberg Tables.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following
                table lists the supported filter fields for this resource and the filter
                conditions that can
                be applied on those fields:

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | environment_id            | $eq              | The Clumio-assigned ID of the |
                |                           |                  | AWS environment.              |
                +---------------------------+------------------+-------------------------------+
                | deactivated               | $eq              | Filter assets protected by a  |
                |                           |                  | deactivated policy.           |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting this        |
                |                           |                  | resource.                     |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of this |
                |                           |                  | resource. Possible values     |
                |                           |                  | include                       |
                |                           |                  | protected, unprotected, and   |
                |                           |                  | unsupported.                  |
                +---------------------------+------------------+-------------------------------+
                | backup_status             | $in              | The backup status of this     |
                |                           |                  | resource. Possible values     |
                |                           |                  | include success,              |
                |                           |                  | partial_success, failure and  |
                |                           |                  | no_backup.                    |
                +---------------------------+------------------+-------------------------------+
                | is_deleted                | $eq,$in          | The deletion status of this   |
                |                           |                  | resource. If not specified,   |
                |                           |                  | retrieves only active         |
                |                           |                  | Iceberg tables. filter={"is_d |
                |                           |                  | eleted":{"$in":["true","false |
                |                           |                  | "]}}                          |
                +---------------------------+------------------+-------------------------------+
                | account_native_id         | $eq,$in          | The AWS-assigned ID of the    |
                |                           |                  | account to which this         |
                |                           |                  | resource belongs. For         |
                |                           |                  | example,                      |
                |                           |                  | filter={"account_native_id":{ |
                |                           |                  | "$in":["789901323485"]}}      |
                |                           |                  | retrieves                     |
                |                           |                  | Iceberg tables across all     |
                |                           |                  | regions in account            |
                |                           |                  | 789901323485.                 |
                +---------------------------+------------------+-------------------------------+
                | table_name                | $contains,$eq    | The name of the table. For    |
                |                           |                  | example,                      |
                |                           |                  | filter={"table_name":{"$conta |
                |                           |                  | ins":"dev"}} retrieves all    |
                |                           |                  | Iceberg tables                |
                |                           |                  | with "dev" in their name.     |
                +---------------------------+------------------+-------------------------------+
                | catalog_type              | $in              | The type of catalog. Possible |
                |                           |                  | values include                |
                |                           |                  | aws_iceberg_glue_table and    |
                |                           |                  | aws_iceberg_s3_table. For     |
                |                           |                  | example,                      |
                |                           |                  | filter={"catalog_type":{"$in" |
                |                           |                  | :["aws_iceberg_glue_table"]}} |
                |                           |                  | retrieves all                 |
                |                           |                  | Iceberg tables whose catalog  |
                |                           |                  | type is Glue.                 |
                +---------------------------+------------------+-------------------------------+
                | catalog                   | $contains,$eq    | The name of the catalog. For  |
                |                           |                  | example,                      |
                |                           |                  | filter={"catalog":{"$contains |
                |                           |                  | ":"dev"}} retrieves all       |
                |                           |                  | Iceberg tables                |
                |                           |                  | in the catalog containing     |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | namespace                 | $contains,$eq    | For example,                  |
                |                           |                  | filter={"namespace":{"$contai |
                |                           |                  | ns":"dev"}} retrieves all     |
                |                           |                  | Iceberg tables                |
                |                           |                  | in the namespace containing   |
                |                           |                  | "dev".                        |
                +---------------------------+------------------+-------------------------------+
                | tags.id                   | $all             | The Clumio-assigned ID(s) of  |
                |                           |                  | AWS tag(s) applied to this    |
                |                           |                  | resource. For example,        |
                |                           |                  | filter={"tags.id":{"$all":["c |
                |                           |                  | 764b152-5819-11ea-bb9f-       |
                |                           |                  | b2e1c9a040ad","c764abb6-5819- |
                |                           |                  | 11ea-bb9f-b2e1c9a040ad"]}}    |
                |                           |                  | retrieves all Iceberg tables  |
                |                           |                  | that are associated with the  |
                |                           |                  | 2 AWS tags identified by      |
                |                           |                  | these                         |
                |                           |                  | IDs. If multiple tags are     |
                |                           |                  | specified, all of them must   |
                |                           |                  | be applied to the same        |
                |                           |                  | Iceberg                       |
                |                           |                  | table.                        |
                +---------------------------+------------------+-------------------------------+

                For more information about filtering, refer to the Filtering section
                of this guide.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following
                embeddable links to include additional details associated with the resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected Iceberg |
                |                        | Table into the response. For                        |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

                For more information about embedded links, refer to the Embedding
                Referenced Resources section of this guide.
            lookback_days:
                Calculate backup status for the last `lookback_days` days.
        """
        controller = AwsIcebergTablesV1Controller(self.controller)
        while True:
            response = controller.list_aws_iceberg_tables(
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
