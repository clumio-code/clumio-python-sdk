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
        filter: str | None = None,
        **kwargs,
    ) -> Union[
        list_ec2_backups_response.ListEC2BackupsResponse,
        tuple[requests.Response, Optional[list_ec2_backups_response.ListEC2BackupsResponse]],
    ]:
        """Returns a list of EC2 instances that have been backed up by Clumio. EC2 instance
        backups can be restored through the [POST
        /restores/aws/ec2-instances](#operation/restore-aws-ec2-instance) endpoint.

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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_ec2_backups_response.ListEC2BackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'limit': limit, 'start': start, 'sort': sort, 'filter': filter}

        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_backup_aws_ec2_instances.', errors
            )

        if self.config.raw_response:
            return resp, list_ec2_backups_response.ListEC2BackupsResponse.from_dictionary(
                resp.json()
            )
        return list_ec2_backups_response.ListEC2BackupsResponse.from_dictionary(resp.json())

    def create_backup_aws_ec2_instance(
        self,
        embed: str | None = None,
        body: (
            create_backup_aws_ec2_instance_v1_request.CreateBackupAwsEc2InstanceV1Request | None
        ) = None,
        **kwargs,
    ) -> Union[
        on_demand_ec2_backup_response.OnDemandEC2BackupResponse,
        tuple[requests.Response, Optional[on_demand_ec2_backup_response.OnDemandEC2BackupResponse]],
    ]:
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            on_demand_ec2_backup_response.OnDemandEC2BackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp: requests.Response = self.client.post(
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
                'Error occurred while executing create_backup_aws_ec2_instance.', errors
            )

        if self.config.raw_response:
            return resp, on_demand_ec2_backup_response.OnDemandEC2BackupResponse.from_dictionary(
                resp.json()
            )
        return on_demand_ec2_backup_response.OnDemandEC2BackupResponse.from_dictionary(resp.json())

    def read_backup_aws_ec2_instance(self, backup_id: str | None = None, **kwargs) -> Union[
        read_ec2_backup_response.ReadEC2BackupResponse,
        tuple[requests.Response, Optional[read_ec2_backup_response.ReadEC2BackupResponse]],
    ]:
        """Returns a representation of the specified EC2 instance backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_ec2_backup_response.ReadEC2BackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/backups/aws/ec2-instances/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters: dict[str, Any] = {}

        # Execute request
        try:
            resp: requests.Response = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_backup_aws_ec2_instance.', errors
            )

        if self.config.raw_response:
            return resp, read_ec2_backup_response.ReadEC2BackupResponse.from_dictionary(resp.json())
        return read_ec2_backup_response.ReadEC2BackupResponse.from_dictionary(resp.json())
