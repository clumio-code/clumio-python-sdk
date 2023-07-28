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
from clumioapi.models import read_v_mware_folder_stats_response
import requests


class VmwareVcenterFolderComplianceStatsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-folder-compliance-stats resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-folder-compliance-stats=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_vmware_vcenter_folder_compliance_stats(
        self, vcenter_id: str, folder_id: str, **kwargs
    ) -> Union[
        read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse,
        tuple[
            requests.Response,
            Optional[read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse],
        ],
    ]:
        """Returns the compliance statistics of VMs under folders and subfolders of the
        specified VMware folder.

        Args:
            vcenter_id:
                Performs the operation on a folder within the specified vCenter server.
            folder_id:
                Performs the operation on the folder with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/folders/{folder_id}/stats/compliance'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'folder_id': folder_id}
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
                'Error occurred while executing read_vmware_vcenter_folder_compliance_stats.',
                errors,
            )

        if self.config.raw_response:
            return (
                resp,
                read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse.from_dictionary(
                    resp.json()
                ),
            )
        return read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse.from_dictionary(
            resp
        )
