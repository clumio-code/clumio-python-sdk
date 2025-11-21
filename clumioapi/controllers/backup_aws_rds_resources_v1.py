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
from clumioapi.controllers.types import backup_aws_rds_resources_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_rds_database_backups_response
from clumioapi.models import list_rds_option_groups_response
from clumioapi.models import read_rds_database_backup_response
import requests
import retrying


class BackupAwsRdsResourcesV1Controller:
    """A Controller to access Endpoints for backup-aws-rds-resources resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-rds-resources=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_backup_aws_rds_resources(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_rds_resources_types.ListBackupAwsRdsResourcesV1FilterT | None = None,
        **kwargs,
    ) -> list_rds_database_backups_response.ListRdsDatabaseBackupsResponse:
        """Retrieves a list of RDS database backups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            sort:
                Returns the list of backups in the order specified. Set `sort` to the name of
                the sort field by
                which to sort in ascending order. To sort the list in reverse order, prefix the
                field name
                with a minus sign (`-`). Only one field may be sorted at a time.

                The following table lists the supported sort fields for this resource:

                +-----------------+------------------------------------------------------------+
                |   Sort Field    |                        Description                         |
                +=================+============================================================+
                | start_timestamp | Sorts the backups in ascending timestamp order (oldest     |
                |                 | first). For example, sort=start_timestamp                  |
                +-----------------+------------------------------------------------------------+

                If a sort order is not specified, the individual rules are sorted by
                "start_timestamp" in descending timestamp order (newest first).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | resource_id     | $eq              | Filter database backups whose database  |
                |                 |                  | ID equal the specified string. For      |
                |                 |                  | example, filter={"resource_id":{"$eq":" |
                |                 |                  | fdba79ed-502b-11fb-9bdc-83d528bd52dc"}} |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | Filter database backups whose start     |
                |                 |                  | timestamp is "less than or equal to" or |
                |                 |                  | "greater than" a given timestamp.       |
                |                 |                  | Represented in RFC-3339 format. For     |
                |                 |                  | example, filter={"start_timestamp":{"$l |
                |                 |                  | te":"1985-04-12T23:20:50Z"}}            |
                +-----------------+------------------+-----------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_rds_database_backups_response.ListRdsDatabaseBackupsResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_rds_database_backups_response.ListRdsDatabaseBackupsResponse
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
                f'list_backup_aws_rds_resources for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_aws_rds_resource(
        self, backup_id: str | None = None, **kwargs
    ) -> read_rds_database_backup_response.ReadRdsDatabaseBackupResponse:
        """Returns a representation of the specified RDS database backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_rds_database_backup_response.ReadRdsDatabaseBackupResponse.from_response(
                resp
            )

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_rds_database_backup_response.ReadRdsDatabaseBackupResponse
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
                f'read_backup_aws_rds_resource for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def list_aws_rds_resources_option_groups(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            backup_aws_rds_resources_types.ListAwsRdsResourcesOptionGroupsV1FilterT | None
        ) = None,
        **kwargs,
    ) -> list_rds_option_groups_response.ListRdsOptionGroupsResponse:
        """Retrieves a list of RDS option groups which are superset of persistent and
        permanent
        options present in the backup snapshot for a given environment.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
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

                +----------------+------------------+------------------------------------------+
                |     Field      | Filter Condition |               Description                |
                +================+==================+==========================================+
                | environment_id | $eq              | The Clumio-assigned ID of the AWS        |
                |                |                  | environment.                             |
                +----------------+------------------+------------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_rds_option_groups_response.ListRdsOptionGroupsResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/backups/aws/rds-resources/{backup_id}/option-groups'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )

        if start:
            _url_path = f'{_url_path}?start={start}'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_rds_option_groups_response.ListRdsOptionGroupsResponse
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
            error_str = f'list_aws_rds_resources_option_groups for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupAwsRdsResourcesV1ControllerPaginator:
    """A Controller to access Endpoints for backup-aws-rds-resources resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_backup_aws_rds_resources(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_rds_resources_types.ListBackupAwsRdsResourcesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_rds_database_backups_response.ListRdsDatabaseBackupsResponse]:
        """Retrieves a list of RDS database backups.

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            sort:
                Returns the list of backups in the order specified. Set `sort` to the name of
                the sort field by
                which to sort in ascending order. To sort the list in reverse order, prefix the
                field name
                with a minus sign (`-`). Only one field may be sorted at a time.

                The following table lists the supported sort fields for this resource:

                +-----------------+------------------------------------------------------------+
                |   Sort Field    |                        Description                         |
                +=================+============================================================+
                | start_timestamp | Sorts the backups in ascending timestamp order (oldest     |
                |                 | first). For example, sort=start_timestamp                  |
                +-----------------+------------------------------------------------------------+

                If a sort order is not specified, the individual rules are sorted by
                "start_timestamp" in descending timestamp order (newest first).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | resource_id     | $eq              | Filter database backups whose database  |
                |                 |                  | ID equal the specified string. For      |
                |                 |                  | example, filter={"resource_id":{"$eq":" |
                |                 |                  | fdba79ed-502b-11fb-9bdc-83d528bd52dc"}} |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | Filter database backups whose start     |
                |                 |                  | timestamp is "less than or equal to" or |
                |                 |                  | "greater than" a given timestamp.       |
                |                 |                  | Represented in RFC-3339 format. For     |
                |                 |                  | example, filter={"start_timestamp":{"$l |
                |                 |                  | te":"1985-04-12T23:20:50Z"}}            |
                +-----------------+------------------+-----------------------------------------+

        """
        controller = BackupAwsRdsResourcesV1Controller(self.controller)
        while True:
            response = controller.list_backup_aws_rds_resources(
                limit=limit, start=start, sort=sort, filter=filter, **kwargs
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
    def list_aws_rds_resources_option_groups(
        self,
        backup_id: str | None = None,
        limit: int | None = None,
        start: str | None = None,
        filter: (
            backup_aws_rds_resources_types.ListAwsRdsResourcesOptionGroupsV1FilterT | None
        ) = None,
        **kwargs,
    ) -> Iterator[list_rds_option_groups_response.ListRdsOptionGroupsResponse]:
        """Retrieves a list of RDS option groups which are superset of persistent and
        permanent
        options present in the backup snapshot for a given environment.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
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

                +----------------+------------------+------------------------------------------+
                |     Field      | Filter Condition |               Description                |
                +================+==================+==========================================+
                | environment_id | $eq              | The Clumio-assigned ID of the AWS        |
                |                |                  | environment.                             |
                +----------------+------------------+------------------------------------------+

        """
        controller = BackupAwsRdsResourcesV1Controller(self.controller)
        while True:
            response = controller.list_aws_rds_resources_option_groups(
                backup_id=backup_id, limit=limit, start=start, filter=filter, **kwargs
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
