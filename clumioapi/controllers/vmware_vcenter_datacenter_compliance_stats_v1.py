#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import read_v_mware_datacenter_stats_response
import requests


class VmwareVcenterDatacenterComplianceStatsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-datacenter-compliance-stats resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def read_vmware_vcenter_datacenter_compliance_stats(
        self, vcenter_id: str, datacenter_id: str
    ) -> read_v_mware_datacenter_stats_response.ReadVMwareDatacenterStatsResponse:
        """Returns a representation of the compliance statistics of the specified data
        center.

        Args:
            vcenter_id:
                Performs the operation on a data center within the specified vCenter server.
            datacenter_id:
                Performs the operation on the data center with the specified ID.
        Returns:
            ReadVMwareDatacenterStatsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/datacenters/{datacenter_id}/stats/compliance'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'datacenter_id': datacenter_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-datacenter-compliance-stats=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_datacenter_compliance_stats.',
                errors,
            )
        return read_v_mware_datacenter_stats_response.ReadVMwareDatacenterStatsResponse.from_dictionary(
            resp
        )
