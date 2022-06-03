#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_vms_response
from clumioapi.models import read_vm_response
import requests


class VmwareVcenterVmsV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-vms resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.vmware-vcenter-vms=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }

    def list_vmware_vcenter_vms(
        self,
        vcenter_id: str,
        limit: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
    ) -> list_vms_response.ListVmsResponse:
        """Returns a list of VMs in the specified vCenter server.

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
                | name                        | $contains        | The name of the VM. For     |
                |                             |                  | example, filter={"name":{"$ |
                |                             |                  | contains":"clumio-vm"}}     |
                +-----------------------------+------------------+-----------------------------+
                | compliance_status           | $eq, $in         | The compliance status of    |
                |                             |                  | the VM. For example, filter |
                |                             |                  | ={"compliance_status":{"$eq |
                |                             |                  | ":"non_compliant"}}. This   |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true. This  |
                |                             |                  | parameter cannot be set if  |
                |                             |                  | the protection_status       |
                |                             |                  | filter parameter is set to  |
                |                             |                  | "unsupported" or            |
                |                             |                  | "unprotected". Refer to the |
                |                             |                  | Compliance Status table for |
                |                             |                  | a complete list of          |
                |                             |                  | compliance statuses.        |
                +-----------------------------+------------------+-----------------------------+
                | protection_status           | $in              | The protection status of    |
                |                             |                  | the VM. For example, filter |
                |                             |                  | ={"protection_status":{"$in |
                |                             |                  | ":["unsupported",           |
                |                             |                  | "protected"]}}. This        |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true. If    |
                |                             |                  | the compliance_status       |
                |                             |                  | filter parameter is set,    |
                |                             |                  | this parameter cannot be    |
                |                             |                  | set to "unsupported" or     |
                |                             |                  | "unprotected". Refer to the |
                |                             |                  | Protection Status table for |
                |                             |                  | a complete list of          |
                |                             |                  | protection statuses.        |
                +-----------------------------+------------------+-----------------------------+
                | protection_info.policy_id   | $eq              | The Clumio-assigned ID of   |
                |                             |                  | the Clumio policy           |
                |                             |                  | protecting the VM. For      |
                |                             |                  | example, filter={"protectio |
                |                             |                  | n_info.policy_id":{"$eq":"9 |
                |                             |                  | c2934fc-ff4d-11e9-8e11-     |
                |                             |                  | 76706df7fe01"}}. This       |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true. This  |
                |                             |                  | parameter cannot be set if  |
                |                             |                  | the protection_status       |
                |                             |                  | filter parameter is set to  |
                |                             |                  | "unsupported" or            |
                |                             |                  | "unprotected".              |
                +-----------------------------+------------------+-----------------------------+
                | tag.id                      | $eq              | The VMware-assigned ID of a |
                |                             |                  | tag assigned to the VM. For |
                |                             |                  | example, filter={"tag.id":{ |
                |                             |                  | "$eq":"d78cd819-ab15-48e2-  |
                |                             |                  | acea-3f94d3a9f2fb"}}. This  |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true.       |
                +-----------------------------+------------------+-----------------------------+
                | is_deleted                  | $eq              | The deletion status of the  |
                |                             |                  | VM. Set to true to return   |
                |                             |                  | deleted VMs. Set to false   |
                |                             |                  | to return active VMs. For   |
                |                             |                  | example, filter={"is_delete |
                |                             |                  | d":{"$eq":true}}            |
                +-----------------------------+------------------+-----------------------------+
                | *compute_resource.id        | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the compute resource     |
                |                             |                  | from which the VM draws.    |
                |                             |                  | For example, filter={"compu |
                |                             |                  | te_resource.id":{"$eq":"dom |
                |                             |                  | ain-s4298"}}. This          |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true.       |
                +-----------------------------+------------------+-----------------------------+
                | *compute_resource_folder.id | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of The compute resource     |
                |                             |                  | folder associated with this |
                |                             |                  | VM. For example, filter={"c |
                |                             |                  | ompute_resource_folder.id": |
                |                             |                  | {"$eq":"group-h182"}}. This |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true.       |
                +-----------------------------+------------------+-----------------------------+
                | *datacenter.id              | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the data center in which |
                |                             |                  | the VM resides. For         |
                |                             |                  | example, filter={"datacente |
                |                             |                  | r.id":{"$eq":"datacenter-   |
                |                             |                  | 9822"}}. This parameter     |
                |                             |                  | cannot be set with          |
                |                             |                  | is_deleted=true.            |
                +-----------------------------+------------------+-----------------------------+
                | *datacenter_folder.id       | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the data center folder   |
                |                             |                  | associated with this VM.    |
                |                             |                  | For example, filter={"datac |
                |                             |                  | enter_folder.id":{"$eq":"gr |
                |                             |                  | oup-d1"}}. This parameter   |
                |                             |                  | cannot be set with          |
                |                             |                  | is_deleted=true.            |
                +-----------------------------+------------------+-----------------------------+
                | *vm_folder.id               | $eq              | The VMware-assigned Managed |
                |                             |                  | Object Reference (MoRef) ID |
                |                             |                  | of the virtual machine      |
                |                             |                  | folder in which the VM      |
                |                             |                  | resides. For example, filte |
                |                             |                  | r={"vm_folder.id":{"$eq":"g |
                |                             |                  | roup-v9823"}}. This         |
                |                             |                  | parameter cannot be set     |
                |                             |                  | with is_deleted=true.       |
                +-----------------------------+------------------+-----------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                compute_resource.id
                compute_resource_folder.id
                datacenter.id
                datacenter_folder.id
                vm_folder.id

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected VM in   |
                |                        | the response. Has no effect on unprotected VMs. For |
                |                        | example, embed=read-policy-definition               |
                +------------------------+-----------------------------------------------------+

        Returns:
            ListVmsResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/vms'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_vms.', errors
            )
        return list_vms_response.ListVmsResponse.from_dictionary(resp)

    def read_vmware_vcenter_vm(
        self, vcenter_id: str, vm_id: str, embed: str = None
    ) -> read_vm_response.ReadVmResponse:
        """Returns a representation of the specified VM.

        Args:
            vcenter_id:
                Performs the operation on a VM within the specified vCenter server.
            vm_id:
                Performs the operation on the VM with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +------------------------+-----------------------------------------------------+
                |    Embeddable Link     |                     Description                     |
                +========================+=====================================================+
                | read-policy-definition | Embeds the associated policy of a protected VM in   |
                |                        | the response. Has no effect on unprotected VMs.     |
                +------------------------+-----------------------------------------------------+

        Returns:
            ReadVmResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/vms/{vm_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'vm_id': vm_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Execute request
        try:
            resp = self.client.get(_url_path, headers=self.headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_vm.', errors
            )
        return read_vm_response.ReadVmResponse.from_dictionary(resp)
