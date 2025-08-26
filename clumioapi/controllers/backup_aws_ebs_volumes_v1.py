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
from clumioapi.controllers.types import backup_aws_ebs_volumes_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_aws_ebs_volume_v1_request
from clumioapi.models import list_ebs_backups_response_v1
from clumioapi.models import on_demand_ebs_backup_response_v1
from clumioapi.models import read_ebs_backup_response_v1
import requests


class BackupAwsEbsVolumesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-ebs-volumes resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-ebs-volumes=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_aws_ebs_volumes(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_ebs_volumes_types.ListBackupAwsEbsVolumesV1FilterT | None = None,
        **kwargs,
    ) -> list_ebs_backups_response_v1.ListEBSBackupsResponseV1:
        """Returns a list of EBS volumes that have been backed up by Clumio. EBS volume
        backups can be restored through the [POST /restores/aws/ebs-
        volumes](#operation/restore-aws-ebs-volume) endpoint.

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
                | volume_id       | $eq              | The ID of the volume backup. For        |
                |                 |                  | example, filter={"volume_id":{"$eq":"d0 |
                |                 |                  | ba78cc-582b-11ea-9bdc-82f798bd42fe"}}   |
                +-----------------+------------------+-----------------------------------------+
                | start_timestamp | $lte, $gt        | The timestamp value of when the backup  |
                |                 |                  | started. Represented in RFC-3339        |
                |                 |                  | format. For example, filter={"start_tim |
                |                 |                  | estamp":{"$lte":"1985-04-               |
                |                 |                  | 12T23:20:50Z"}}                         |
                +-----------------+------------------+-----------------------------------------+

        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return list_ebs_backups_response_v1.ListEBSBackupsResponseV1.from_response(response)

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'sort': sort,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_ebs_backups_response_v1.ListEBSBackupsResponseV1
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
                f'list_backup_aws_ebs_volumes for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def create_backup_aws_ebs_volume(
        self,
        embed: str | None = None,
        body: (
            create_backup_aws_ebs_volume_v1_request.CreateBackupAwsEbsVolumeV1Request | None
        ) = None,
        **kwargs,
    ) -> on_demand_ebs_backup_response_v1.OnDemandEBSBackupResponseV1:
        """Performs an on-demand backup for the specified EBS volume.

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
            return on_demand_ebs_backup_response_v1.OnDemandEBSBackupResponseV1.from_response(
                response
            )

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        resp_instance: on_demand_ebs_backup_response_v1.OnDemandEBSBackupResponseV1
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
                f'create_backup_aws_ebs_volume for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_backup_aws_ebs_volume(
        self, backup_id: str | None = None, **kwargs
    ) -> read_ebs_backup_response_v1.ReadEBSBackupResponseV1:
        """Returns a representation of the specified EBS volume backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        """

        def get_instance_from_response(response: requests.Response) -> Any:
            return read_ebs_backup_response_v1.ReadEBSBackupResponseV1.from_response(response)

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        resp_instance: read_ebs_backup_response_v1.ReadEBSBackupResponseV1
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
                f'read_backup_aws_ebs_volume for url {urllib.parse.unquote(resp.url)} failed.'
            )
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class BackupAwsEbsVolumesV1ControllerPaginator(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-ebs-volumes resource with pagination."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.controller = BackupAwsEbsVolumesV1Controller(config)

    def list_backup_aws_ebs_volumes(
        self,
        limit: int | None = None,
        start: str | None = None,
        sort: str | None = None,
        filter: backup_aws_ebs_volumes_types.ListBackupAwsEbsVolumesV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_ebs_backups_response_v1.ListEBSBackupsResponseV1]:
        """Returns a list of EBS volumes that have been backed up by Clumio. EBS volume
        backups can be restored through the [POST /restores/aws/ebs-
        volumes](#operation/restore-aws-ebs-volume) endpoint.

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
                | volume_id       | $eq              | The ID of the volume backup. For        |
                |                 |                  | example, filter={"volume_id":{"$eq":"d0 |
                |                 |                  | ba78cc-582b-11ea-9bdc-82f798bd42fe"}}   |
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
            response = self.controller.list_backup_aws_ebs_volumes(
                limit=limit, start=start, sort=sort, filter=filter, **kwargs
            )
            yield response
            if not response.Links.Next.Href:  # type: ignore
                break

            start = str(int(start) + 1)
