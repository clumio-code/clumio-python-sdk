#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_v_mware_folder_stats_response
import requests


class VmwareVcenterFolderComplianceStatsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-folder-compliance-stats resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def read_vmware_vcenter_folder_compliance_stats(
        self, vcenter_id: str, folder_id: str
    ) -> read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse:
        """Returns the compliance statistics of VMs under folders and subfolders of the
        specified VMware folder.

        Args:
            vcenter_id:
                Performs the operation on a folder within the specified vCenter server.
            folder_id:
                Performs the operation on the folder with the specified ID.
        Returns:
            ReadVMwareFolderStatsResponse: Response from the API.
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

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-folder-compliance-stats=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_folder_compliance_stats.',
                errors,
            )
        return read_v_mware_folder_stats_response.ReadVMwareFolderStatsResponse.from_dictionary(
            resp
        )
