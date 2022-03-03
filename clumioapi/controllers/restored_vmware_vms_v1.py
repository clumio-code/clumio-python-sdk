#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import restore_v_mware_vm_response
from clumioapi.models import restore_vmware_vm_v1_request
import requests


class RestoredVmwareVmsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for restored-vmware-vms resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def restore_vmware_vm(
        self, body: restore_vmware_vm_v1_request.RestoreVmwareVmV1Request = None
    ) -> restore_v_mware_vm_response.RestoreVMwareVMResponse:
        """Restores the specified source VM backup to the specified target destination. The
        source VM must be one that was backed up by Clumio.

        Args:
            body:

        Returns:
            RestoreVMwareVMResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/restores/vmware/vms'

        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/restored-vmware-vms=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.post(
                _url_path,
                headers=_headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
            )
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing restore_vmware_vm.', errors
            )
        return restore_v_mware_vm_response.RestoreVMwareVMResponse.from_dictionary(resp)
