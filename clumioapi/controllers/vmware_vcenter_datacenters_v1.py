#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_datacenters_response
from clumioapi.models import read_datacenter_response
import requests


class VmwareVcenterDatacentersV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-datacenters resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-datacenters=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }

    def list_vmware_vcenter_datacenters(
        self,
        vcenter_id: str,
        limit: int = None,
        start: str = None,
        filter: str = None,
        _embed: str = None,
    ) -> list_datacenters_response.ListDatacentersResponse:
        """Returns a list of VMware data centers in the specified vCenter server.

        Args:
            vcenter_id:
                Performs the operation on the vCenter server with the specified Clumio-assigned
                ID.
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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | datacenter_folder.id      | $eq              | The VMware-assigned Managed   |
                |                           |                  | Object Reference (MoRef) ID   |
                |                           |                  | of the data center folder.    |
                |                           |                  | For example, filter={"datacen |
                |                           |                  | ter_folder.id":{"$eq":"group- |
                |                           |                  | d1"}}                         |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | eq               | The Clumio-assigned ID of the |
                |                           |                  | policy protecting the data    |
                |                           |                  | center. For example, filter={ |
                |                           |                  | "protection_info.policy_id":{ |
                |                           |                  | "$eq":"9c2934fc-ff4d-11e9-    |
                |                           |                  | 8e11-76706df7fe01"}}          |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | in               | The protection status of the  |
                |                           |                  | data center. Refer to the     |
                |                           |                  | Protection Status table for a |
                |                           |                  | complete list of protection   |
                |                           |                  | statuses. For example, filter |
                |                           |                  | ={"protection_status":{"$in": |
                |                           |                  | ["unprotected",               |
                |                           |                  | "protected"]}}                |
                +---------------------------+------------------+-------------------------------+

            _embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-datacenter-       | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under each data center in the    |
                |                                       | response. The response includes VMs  |
                |                                       | in all nested vCenter objects. For   |
                |                                       | example, embed=read-vmware-vcenter-  |
                |                                       | datacenter-compliance-stats          |
                +---------------------------------------+--------------------------------------+

        Returns:
            ListDatacentersResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/datacenters'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, '_embed': _embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_datacenters.', errors
            )
        return list_datacenters_response.ListDatacentersResponse.from_dictionary(resp)

    def read_vmware_vcenter_datacenter(
        self, vcenter_id: str, datacenter_id: str, embed: str = None
    ) -> read_datacenter_response.ReadDatacenterResponse:
        """Returns a representation of the specified VMware data center within the
        specified vCenter server.

        Args:
            vcenter_id:
                Performs the operation on a data center within the specified vCenter server.
            datacenter_id:
                Performs the operation on the datacenter with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-datacenter-       | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under the given data center. The |
                |                                       | response includes VMs in all nested  |
                |                                       | vCenter objects. For example,        |
                |                                       | embed=read-vmware-vcenter-           |
                |                                       | datacenter-compliance-stats          |
                +---------------------------------------+--------------------------------------+

        Returns:
            ReadDatacenterResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/datacenters/{datacenter_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'datacenter_id': datacenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_datacenter.', errors
            )
        return read_datacenter_response.ReadDatacenterResponse.from_dictionary(resp)
