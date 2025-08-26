#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import backup_aws_ec2_instances_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_aws_ec2_instance_v1_request
from clumioapi.models import list_ec2_backups_response
from clumioapi.models import on_demand_ec2_backup_response
from clumioapi.models import read_ec2_backup_response
import requests


class BackupAwsEc2InstancesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-ec2-instances resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-ec2-instances=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_ec2_instances(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_ec2_instances_types.ListBackupAwsEc2InstancesV1FilterT | None = None,
        **kwargs,
    ) -> list_ec2_backups_response.ListEC2BackupsResponse:
        """Returns a list of EC2 instances that have been backed up by Clumio. EC2 instance
        backups can be restored through the [POST
        /restores/aws/ec2-instances](#operation/restore-aws-ec2-instance) endpoint.

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
                | instance_id     | $eq              | The ID of the instance backup. For      |
                |                 |                  | example, filter={"instance_id":{"$eq":" |
                |                 |                  | d0ba78cc-582b-11ea-9bdc-82f798bd42fe"}} |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | The timestamp value of when the backup  |
                |                 |                  | started. Represented in RFC-3339        |
                |                 |                  | format. For example, filter={"start_tim |
                |                 |                  | estamp":{"$lte":"1985-04-               |
                |                 |                  | 12T23:20:50Z"}}                         |
                +-----------------+------------------+-----------------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_ec2_backups_response.ListEC2BackupsResponse.from_response(response)

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_ec2_backups_response.ListEC2BackupsResponse
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
                f'list_backup_aws_ec2_instances for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_backup_aws_ec2_instance(
        self,
        embed: str | None = None,
        body: (
            create_backup_aws_ec2_instance_v1_request.CreateBackupAwsEc2InstanceV1Request | None
        ) = None,
        **kwargs,
    ) -> on_demand_ec2_backup_response.OnDemandEC2BackupResponse:
        """Performs an on-demand backup for the specified EC2 instance.

        Args:
            embed:
                Embeds the details of each associated resource. Set the parameter to one of the
                following embeddable links to
                include additional details associated with the resource.

                +-----------------+------------------------------------------------------------+
                | Embeddable Link |                        Description                         |
                +=================+============================================================+
                | read-task       | Embeds the associated task in the response. For example,   |
                |                 | embed=read-task                                            |
                +-----------------+------------------------------------------------------------+

                For more information about embedded links, refer to the
                Embedding Referenced Resources section of this guide.
            body:

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return on_demand_ec2_backup_response.OnDemandEC2BackupResponse.from_response(response)

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: on_demand_ec2_backup_response.OnDemandEC2BackupResponse
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
                f'create_backup_aws_ec2_instance for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_aws_ec2_instance(
        self, backup_id: str | None = None, **kwargs
    ) -> read_ec2_backup_response.ReadEC2BackupResponse:
        """Returns a representation of the specified EC2 instance backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_ec2_backup_response.ReadEC2BackupResponse.from_response(response)

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_ec2_backup_response.ReadEC2BackupResponse
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
                f'read_backup_aws_ec2_instance for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupAwsEc2InstancesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-ec2-instances resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupAwsEc2InstancesV1Controller(config)

    def list_backup_aws_ec2_instances(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_ec2_instances_types.ListBackupAwsEc2InstancesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_ec2_backups_response.ListEC2BackupsResponse]:
        """Returns a list of EC2 instances that have been backed up by Clumio. EC2 instance
        backups can be restored through the [POST
        /restores/aws/ec2-instances](#operation/restore-aws-ec2-instance) endpoint.

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
                | instance_id     | $eq              | The ID of the instance backup. For      |
                |                 |                  | example, filter={"instance_id":{"$eq":" |
                |                 |                  | d0ba78cc-582b-11ea-9bdc-82f798bd42fe"}} |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | The timestamp value of when the backup  |
                |                 |                  | started. Represented in RFC-3339        |
                |                 |                  | format. For example, filter={"start_tim |
                |                 |                  | estamp":{"$lte":"1985-04-               |
                |                 |                  | 12T23:20:50Z"}}                         |
                +-----------------+------------------+-----------------------------------------+

        """
        start = start or '1'
        while True:
            response = self.controller.list_backup_aws_ec2_instances(
                limit=limit, start=start, sort=sort, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
