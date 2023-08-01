#
# Copyright 2021. Clumio, Inc.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import create_backup_vmware_vm_v1_request
from clumioapi.models import list_vm_backups_response
from clumioapi.models import on_demand_vm_backup_response
from clumioapi.models import read_vm_backup_response
import requests


class BackupVmwareVmsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for backup-vmware-vms resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.backup-vmware-vms=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_backup_vmware_vms(
        self, limit: int = None, start: str = None, sort: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_vm_backups_response.ListVMBackupsResponse,
        tuple[requests.Response, Optional[list_vm_backups_response.ListVMBackupsResponse]],
    ]:
        """Returns a list of VMware virtual machines (VMs) that have been backed up by
        Clumio. VM backups can be restored through the [POST
        /restores/vmware/vms](#operation/restore-vmware-vm) endpoint.

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
                vcenter_id and vm_id filter are required for this API. The following table lists
                the supported filter fields for this resource and the filter conditions that can
                be
                applied on those fields:

                +-----------------+------------------+-----------------------------------------+
                |      Field      | Filter Condition |               Description               |
                +=================+==================+=========================================+
                | start_timestamp | $lte, $gt        | The timestamp value of when the backup  |
                |                 |                  | started. Represented in RFC-3339        |
                |                 |                  | format. For example, filter={"start_tim |
                |                 |                  | estamp":{"$lte":"1985-04-               |
                |                 |                  | 12T23:20:50Z"}}                         |
                +-----------------+------------------+-----------------------------------------+
                | vcenter_id      | $eq              | The ID of the vCenter associated with   |
                |                 |                  | the backup VM. For example,             |
                |                 |                  | filter={"vcenter_id":{"$eq":"38"}}      |
                +-----------------+------------------+-----------------------------------------+
                | vm_id           | $eq              | The 128-bit universally unique          |
                |                 |                  | identifier (UUID) of the backup VM to   |
                |                 |                  | be restored. This field must be set     |
                |                 |                  | with vcenter_id. For example, filter={" |
                |                 |                  | vm_id":{"$eq":"50261484-4e52-373f-20ac- |
                |                 |                  | 8a8c2145f196"},"vcenter_id":{"$eq":"38" |
                |                 |                  | }}                                      |
                +-----------------+------------------+-----------------------------------------+

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_vm_backups_response.ListVMBackupsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/vmware/vms'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'sort': sort, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(
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
                'Error occurred while executing list_backup_vmware_vms.', errors
            )

        if self.config.raw_response:
            return resp, list_vm_backups_response.ListVMBackupsResponse.from_dictionary(resp.json())
        return list_vm_backups_response.ListVMBackupsResponse.from_dictionary(resp)

    def create_backup_vmware_vm(
        self,
        body: create_backup_vmware_vm_v1_request.CreateBackupVmwareVmV1Request = None,
        **kwargs,
    ) -> Union[
        on_demand_vm_backup_response.OnDemandVMBackupResponse,
        tuple[requests.Response, Optional[on_demand_vm_backup_response.OnDemandVMBackupResponse]],
    ]:
        """Performs an on-demand backup for the specified VM.

        Args:
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            on_demand_vm_backup_response.OnDemandVMBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/vmware/vms'

        _query_parameters = {}

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
                'Error occurred while executing create_backup_vmware_vm.', errors
            )

        if self.config.raw_response:
            return resp, on_demand_vm_backup_response.OnDemandVMBackupResponse.from_dictionary(
                resp.json()
            )
        return on_demand_vm_backup_response.OnDemandVMBackupResponse.from_dictionary(resp)

    def read_backup_vmware_vm(
        self, backup_id: int, **kwargs
    ) -> Union[
        read_vm_backup_response.ReadVMBackupResponse,
        tuple[requests.Response, Optional[read_vm_backup_response.ReadVMBackupResponse]],
    ]:
        """Returns a representation of the specified VM backup.

        Args:
            backup_id:
                Performs the operation on the backup with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_vm_backup_response.ReadVMBackupResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/backups/vmware/vms/{backup_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'backup_id': backup_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(
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
                'Error occurred while executing read_backup_vmware_vm.', errors
            )

        if self.config.raw_response:
            return resp, read_vm_backup_response.ReadVMBackupResponse.from_dictionary(resp.json())
        return read_vm_backup_response.ReadVMBackupResponse.from_dictionary(resp)
