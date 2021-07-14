#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_v_mware_v_center_networks_response
from clumioapi.models import read_v_mware_v_center_network_response
import requests


class VmwareVcenterNetworksV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-networks resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_vmware_vcenter_networks(
        self, vcenter_id: str, limit: int = None, start: str = None, filter: str = None
    ) -> list_v_mware_v_center_networks_response.ListVMwareVCenterNetworksResponse:
        """Returns a list of networks in the specified vCenter server.

        Args:
            vcenter_id:
                Performs the operation on the vCenter server with the specified ID.
            limit:
                Limits the size of the response on each page to the specified number of items.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria. The
                following table lists
                the supported filter fields for this resource and the filter conditions that can
                be applied on those fields:

                +--------------------+------------------+--------------------------------------+
                |       Field        | Filter Condition |             Description              |
                +====================+==================+======================================+
                | *datacenter.id     | $eq              | The VMware-assigned ID of the        |
                |                    |                  | datacenter associated with this      |
                |                    |                  | network. For example, filter={"datac |
                |                    |                  | enter.id":{"$eq":"datacenter-9301"}} |
                +--------------------+------------------+--------------------------------------+
                | *network_folder.id | $eq              | The VMware-assigned ID of the        |
                |                    |                  | network folder associated with this  |
                |                    |                  | network. For example, filter={"netwo |
                |                    |                  | rk_folder.id":{"$eq":"group-n349"}}  |
                +--------------------+------------------+--------------------------------------+
                | name               | $contains        | The name of the network. For         |
                |                    |                  | example,                             |
                |                    |                  | filter={"name":{"$contains":"backup- |
                |                    |                  | network"}}                           |
                +--------------------+------------------+--------------------------------------+
                | is_supported       | $eq              | Determines whether VMs can be        |
                |                    |                  | connected to the network. If true,   |
                |                    |                  | VMs can be connected to the network. |
                |                    |                  | For example,                         |
                |                    |                  | filter={"is_supported":{"$eq":true}} |
                +--------------------+------------------+--------------------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                datacenter.id
                network_folder.id

        Returns:
            ListVMwareVCenterNetworksResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/networks'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-networks=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_networks.', errors
            )
        return list_v_mware_v_center_networks_response.ListVMwareVCenterNetworksResponse.from_dictionary(
            resp
        )

    def read_vmware_vcenter_network(
        self, vcenter_id: str, network_id: str
    ) -> read_v_mware_v_center_network_response.ReadVMwareVCenterNetworkResponse:
        """Returns a representation of the specified network.

        Args:
            vcenter_id:
                Performs the operation on a network within the specified vCenter server.
            network_id:
                Performs the operation on the network with the specified ID.
        Returns:
            ReadVMwareVCenterNetworkResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/networks/{network_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'network_id': network_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-networks=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_network.', errors
            )
        return (
            read_v_mware_v_center_network_response.ReadVMwareVCenterNetworkResponse.from_dictionary(
                resp
            )
        )
