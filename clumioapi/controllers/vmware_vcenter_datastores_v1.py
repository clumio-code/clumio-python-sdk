#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_v_mware_datastores_response
from clumioapi.models import read_v_mware_datastore_response
import requests


class VmwareVcenterDatastoresV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-datastores resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_vmware_vcenter_datastores(
        self, vcenter_id: str, limit: int = None, start: str = None, filter: str = None
    ) -> list_v_mware_datastores_response.ListVMwareDatastoresResponse:
        """Returns a list of datastores in the specified vCenter server.


        Supported Datastore Types
        Clumio supports the following VMware datastore types:

        Network File System (nfs)
        vSAN (virtual_storage_area_network)
        vSphere Virtual Machine File System (vmfs)
        Virtual Volumes (virtual_volume)

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

                +-----------------------+------------------+-----------------------------------+
                |         Field         | Filter Condition |            Description            |
                +=======================+==================+===================================+
                | *datacenter.id        | $eq              | The VMware-assigned Managed       |
                |                       |                  | Object Reference (MoRef) ID of    |
                |                       |                  | the data center in which this     |
                |                       |                  | datastore resides. For example, f |
                |                       |                  | ilter={"datacenter.id":{"$eq":"da |
                |                       |                  | tacenter-9301"}}                  |
                +-----------------------+------------------+-----------------------------------+
                | *datastore_folder.id  | $eq              | The VMware-assigned Managed       |
                |                       |                  | Object Reference (MoRef) ID of    |
                |                       |                  | the datastore folder in which     |
                |                       |                  | this datastore resides. For       |
                |                       |                  | example, filter={"datastore_folde |
                |                       |                  | r.id":{"$eq":"group-s349"}}       |
                +-----------------------+------------------+-----------------------------------+
                | *hosts.id             | $all             | The VMware-assigned Managed       |
                |                       |                  | Object Reference (MoRef) ID of    |
                |                       |                  | the hosts associated with this    |
                |                       |                  | datastore. For example, filter={" |
                |                       |                  | hosts.id":{"$all":["host-114","ho |
                |                       |                  | st-395"]}}. If multiple hosts are |
                |                       |                  | specified, all of them must be    |
                |                       |                  | associated with the same          |
                |                       |                  | datastore.                        |
                +-----------------------+------------------+-----------------------------------+
                | *compute_resources.id | $all             | The VMware-assigned Managed       |
                |                       |                  | Object Reference (MoRef) ID of    |
                |                       |                  | the compute resources associated  |
                |                       |                  | with this datastore. For example, |
                |                       |                  | filter={"compute_resources.id":{" |
                |                       |                  | $all":["domain-c9827","domain-s21 |
                |                       |                  | 532"]}}. If multiple compute      |
                |                       |                  | resources are specified, all of   |
                |                       |                  | them must be associated with the  |
                |                       |                  | same datastore.                   |
                +-----------------------+------------------+-----------------------------------+
                | type                  | $eq              | The type of datastore. Possible   |
                |                       |                  | values include "nfs",             |
                |                       |                  | "virtual_storage_area_network",   |
                |                       |                  | "virtual_volume", and "vmfs".     |
                |                       |                  | Refer to the Supported Datastore  |
                |                       |                  | Types list for a complete list of |
                |                       |                  | datastore types. For example,     |
                |                       |                  | filter={"type":{"$eq":"vmfs"}}    |
                +-----------------------+------------------+-----------------------------------+
                | is_supported          | $eq              | Determines whether the datastore  |
                |                       |                  | can be used as a restore          |
                |                       |                  | destination. If true, the         |
                |                       |                  | datastore can be used as a        |
                |                       |                  | restore destination and backups   |
                |                       |                  | can be restored to the datastore. |
                |                       |                  | For example, filter={"is_supporte |
                |                       |                  | d":{"$eq":true}}                  |
                +-----------------------+------------------+-----------------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                datacenter.id
                datastore_folder.id
                hosts.id
                compute_resources.id

        Returns:
            ListVMwareDatastoresResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/datastores'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-datastores=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_datastores.', errors
            )
        return list_v_mware_datastores_response.ListVMwareDatastoresResponse.from_dictionary(resp)

    def read_vmware_vcenter_datastore(
        self, vcenter_id: str, datastore_id: str
    ) -> read_v_mware_datastore_response.ReadVMwareDatastoreResponse:
        """Returns a representation of the specified datastore.

        Args:
            vcenter_id:
                Performs the operation on a datastore within the specified vCenter server.
            datastore_id:
                Performs the operation on the datastore with the specified ID.
        Returns:
            ReadVMwareDatastoreResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/datastores/{datastore_id}'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'datastore_id': datastore_id}
        )
        _query_parameters = {}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-datastores=v1+json',
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_datastore.', errors
            )
        return read_v_mware_datastore_response.ReadVMwareDatastoreResponse.from_dictionary(resp)