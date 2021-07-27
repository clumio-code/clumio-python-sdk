#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_compute_resources_response
from clumioapi.models import read_compute_resource_response
import requests


class VmwareVcenterComputeResourcesV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-compute-resources resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_vmware_vcenter_compute_resources(
        self,
        vcenter_id: str,
        limit: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
    ) -> list_compute_resources_response.ListComputeResourcesResponse:
        """Returns a list of VMware compute resources in the specified vCenter server.

        The following table lists the supported Clumio protection statuses:


        +-------------------+-------------------------------------------------------+
        | Protection Status |                        Values                         |
        +===================+=======================================================+
        | protected         | A compute resource that is protected by a policy.     |
        +-------------------+-------------------------------------------------------+
        | unprotected       | A compute resource that is not protected by a policy. |
        +-------------------+-------------------------------------------------------+

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

                +-----------------------------+------------------+-----------------------------+
                |            Field            | Filter Condition |         Description         |
                +=============================+==================+=============================+
                | *compute_resource_folder.id | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the compute resource     |
                |                             |                  | folder. For example, filter |
                |                             |                  | ={"compute_resource_folder. |
                |                             |                  | id":{"$eq":"group-h4"}}     |
                +-----------------------------+------------------+-----------------------------+
                | *datacenter.id              | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the data center          |
                |                             |                  | associated with this        |
                |                             |                  | compute resource. For       |
                |                             |                  | example, filter={"datacente |
                |                             |                  | r.id":{"$eq":"datacenter-39 |
                |                             |                  | 4"}}                        |
                +-----------------------------+------------------+-----------------------------+
                | protection_info.policy_id   | eq               | The Clumio-assigned ID of   |
                |                             |                  | the policy protecting the   |
                |                             |                  | compute resource. For       |
                |                             |                  | example, filter={"protectio |
                |                             |                  | n_info.policy_id":{"$eq":"9 |
                |                             |                  | c2934fc-ff4d-11e9-8e11-7670 |
                |                             |                  | 6df7fe01"}}                 |
                +-----------------------------+------------------+-----------------------------+
                | protection_status           | in               | The protection status of    |
                |                             |                  | the compute resource. Refer |
                |                             |                  | to the Protection Status    |
                |                             |                  | table for a complete list   |
                |                             |                  | of protection statuses. For |
                |                             |                  | example, filter={"protectio |
                |                             |                  | n_status":{"$in":["unprotec |
                |                             |                  | ted", "protected"]}}        |
                +-----------------------------+------------------+-----------------------------+
                | is_cluster                  | eq               | Determines whether the      |
                |                             |                  | compute resource is a       |
                |                             |                  | cluster compute resource.   |
                |                             |                  | If true, then compute       |
                |                             |                  | resource is a cluster       |
                |                             |                  | compute resource            |
                |                             |                  | representing a host         |
                |                             |                  | cluster. For example, filte |
                |                             |                  | r={"is_cluster":{"$eq":true |
                |                             |                  | }}                          |
                +-----------------------------+------------------+-----------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                compute_resource_folder.id
                datacenter.id

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-compute-resource- | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under each compute resource in   |
                |                                       | the response. The response includes  |
                |                                       | VMs in all nested vCenter objects.   |
                |                                       | For example, embed=read-vmware-      |
                |                                       | vcenter-compute-resource-compliance- |
                |                                       | stats                                |
                +---------------------------------------+--------------------------------------+

        Returns:
            ListComputeResourcesResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/compute-resources'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-compute-resources=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_compute_resources.', errors
            )
        return list_compute_resources_response.ListComputeResourcesResponse.from_dictionary(resp)

    def read_vmware_vcenter_compute_resource(
        self, vcenter_id: str, compute_resource_id: str, embed: str = None
    ) -> read_compute_resource_response.ReadComputeResourceResponse:
        """Returns a representation of the specified VMware compute resource.

        Args:
            vcenter_id:
                Performs the operation on a compute resource within the specified vCenter
                server.
            compute_resource_id:
                Performs the operation on the compute resource with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-compute-resource- | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under the given compute          |
                |                                       | resource. The response includes VMs  |
                |                                       | in all nested vCenter objects. For   |
                |                                       | example, embed=read-vmware-vcenter-  |
                |                                       | compute-resource-compliance-stats    |
                +---------------------------------------+--------------------------------------+

        Returns:
            ReadComputeResourceResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/compute-resources/{compute_resource_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'compute_resource_id': compute_resource_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-compute-resources=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_compute_resource.', errors
            )
        return read_compute_resource_response.ReadComputeResourceResponse.from_dictionary(resp)
