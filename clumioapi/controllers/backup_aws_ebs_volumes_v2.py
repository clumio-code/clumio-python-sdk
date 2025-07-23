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
from clumioapi.models import create_backup_aws_ebs_volume_v2_request
from clumioapi.models import list_ebs_backups_response
from clumioapi.models import on_demand_ebs_backup_response
from clumioapi.models import read_ebs_backup_response
import requests


class BackupAwsEbsVolumesV2Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-aws-ebs-volumes resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-aws-ebs-volumes=v2+json',
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
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_ebs_backups_response.ListEBSBackupsResponse,
        tuple[requests.Response, Optional[list_ebs_backups_response.ListEBSBackupsResponse]],
    ]:
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ebs_backups_response.ListEBSBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start, 'sort': sort, 'filter': filter}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_aws_ebs_volumes.', errors
            )

        obj = list_ebs_backups_response.ListEBSBackupsResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def create_backup_aws_ebs_volume(
        self,
        embed: str | None = None,
        body: (
            create_backup_aws_ebs_volume_v2_request.CreateBackupAwsEbsVolumeV2Request | None
        ) = None,
        **kwargs,
    ) -> Union[
        on_demand_ebs_backup_response.OnDemandEBSBackupResponse,
        tuple[requests.Response, Optional[on_demand_ebs_backup_response.OnDemandEBSBackupResponse]],
    ]:
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
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            on_demand_ebs_backup_response.OnDemandEBSBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes'

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
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing create_backup_aws_ebs_volume.', errors
            )

        obj = on_demand_ebs_backup_response.OnDemandEBSBackupResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj

    def read_backup_aws_ebs_volume(self, backup_id: str | None = None, **kwargs) -> Union[
        read_ebs_backup_response.ReadEBSBackupResponse,
        tuple[requests.Response, Optional[read_ebs_backup_response.ReadEBSBackupResponse]],
    ]:
        """Returns a representation of the specified EBS volume backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ebs_backup_response.ReadEBSBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ebs-volumes/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        raw_response = self.config.raw_response
        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_backup_aws_ebs_volume.', errors
            )

        obj = read_ebs_backup_response.ReadEBSBackupResponse.from_dictionary(resp.json())
        if raw_response:
            return resp, obj
        return obj
