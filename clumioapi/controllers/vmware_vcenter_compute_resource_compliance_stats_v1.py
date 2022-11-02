#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_v_mware_compute_resource_stats_response
import requests


class VmwareVcenterComputeResourceComplianceStatsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-compute-resource-compliance-stats resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-compute-resource-compliance-stats=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def read_vmware_vcenter_compute_resource_compliance_stats(
        self, vcenter_id: str, compute_resource_id: str
    ) -> read_v_mware_compute_resource_stats_response.ReadVMwareComputeResourceStatsResponse:
        """Returns a representation of the compliance statistics of the specified VMware
        compute resource.

        Args:
            vcenter_id:
                Performs the operation on a compute resource within the specified vCenter
                server.
            compute_resource_id:
                Performs the operation on the compute resource with the specified ID.
        Returns:
            ReadVMwareComputeResourceStatsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/compute-resources/{compute_resource_id}/stats/compliance'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'compute_resource_id': compute_resource_id}
        )
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_compute_resource_compliance_stats.',
                errors,
            )
        return read_v_mware_compute_resource_stats_response.ReadVMwareComputeResourceStatsResponse.from_dictionary(
            resp
        )
