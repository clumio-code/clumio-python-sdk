#
# Copyright 2021. Clumio, Inc.
#

import json

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
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
        self, limit: int = None, start: str = None, sort: str = None, filter: str = None
    ) -> list_ebs_backups_response_v1.ListEBSBackupsResponseV1:
        """Returns a list of EBS volumes that have been backed up by Clumio. EBS volume
        backups can be restored through the [POST /restores/aws/ebs-
        volumes](#operation/restore-aws-ebs-volume) endpoint.

        Args:
            limit:
                Limits the size of the response on each page to the specified number of items.
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

        Returns:
            list_ebs_backups_response_v1.ListEBSBackupsResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/ebs-volumes'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'sort': sort, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_aws_ebs_volumes.', errors
            )

        return list_ebs_backups_response_v1.ListEBSBackupsResponseV1.from_dictionary(resp)

    def create_backup_aws_ebs_volume(
        self,
        embed: str = None,
        body: create_backup_aws_ebs_volume_v1_request.CreateBackupAwsEbsVolumeV1Request = None,
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

        Returns:
            on_demand_ebs_backup_response_v1.OnDemandEBSBackupResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/ebs-volumes'

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
                'Error occurred while executing create_backup_aws_ebs_volume.', errors
            )

        return on_demand_ebs_backup_response_v1.OnDemandEBSBackupResponseV1.from_dictionary(resp)

    def read_backup_aws_ebs_volume(
        self, backup_id: str
    ) -> read_ebs_backup_response_v1.ReadEBSBackupResponseV1:
        """Returns a representation of the specified EBS volume backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            read_ebs_backup_response_v1.ReadEBSBackupResponseV1: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/aws/ebs-volumes/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_backup_aws_ebs_volume.', errors
            )

        return read_ebs_backup_response_v1.ReadEBSBackupResponseV1.from_dictionary(resp)
