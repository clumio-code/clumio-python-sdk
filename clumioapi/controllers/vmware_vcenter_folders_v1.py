#
# Copyright 2021. Clumio, Inc.
#

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_folders_response
from clumioapi.models import read_folder_response
import requests


class VmwareVcenterFoldersV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for vmware-vcenter-folders resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config

    def list_vmware_vcenter_folders(
        self,
        vcenter_id: str,
        limit: int = None,
        start: str = None,
        filter: str = None,
        embed: str = None,
    ) -> list_folders_response.ListFoldersResponse:
        """Returns a list of VMware folders in the specified vCenter server.

        The following table lists the supported Clumio folder types:


        +-------------------------+---------------------------+
        |       Folder Type       |        Description        |
        +=========================+===========================+
        | compute_resource_folder | Compute resource folders. |
        +-------------------------+---------------------------+
        | datacenter_folder       | Data center folders.      |
        +-------------------------+---------------------------+
        | vm_folder               | Virtual machine folders.  |
        +-------------------------+---------------------------+


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

                +---------------------------+------------------+-------------------------------+
                |           Field           | Filter Condition |          Description          |
                +===========================+==================+===============================+
                | *parent_folder.id         | $eq              | The VMware-assigned Managed   |
                |                           |                  | Object Reference (MoRef) ID   |
                |                           |                  | of the parent folder. For     |
                |                           |                  | example, filter={"parent_fold |
                |                           |                  | er.id":{"$eq":"group-d1"}}    |
                +---------------------------+------------------+-------------------------------+
                | *datacenter.id            | $eq              | The VMware-assigned Managed   |
                |                           |                  | Object Reference (MoRef) ID   |
                |                           |                  | of the data center associated |
                |                           |                  | with this folder. For         |
                |                           |                  | example, filter={"datacenter. |
                |                           |                  | id":{"$eq":"datacenter-394"}} |
                +---------------------------+------------------+-------------------------------+
                | type                      | $in              | The folder type. Examples of  |
                |                           |                  | folder types include          |
                |                           |                  | "datacenter_folder" and       |
                |                           |                  | "vm_folder". Refer to the     |
                |                           |                  | Folder Type table for a       |
                |                           |                  | complete list of folder       |
                |                           |                  | types. For example, filter={" |
                |                           |                  | type":{"$in":["datacenter_fol |
                |                           |                  | der"]}}                       |
                +---------------------------+------------------+-------------------------------+
                | name                      | $contains        | A substring of the name of    |
                |                           |                  | the folder. For example, filt |
                |                           |                  | er={"name":{"$contains":"fold |
                |                           |                  | ername"}}                     |
                +---------------------------+------------------+-------------------------------+
                | protection_info.policy_id | $eq              | The Clumio-assigned ID of the |
                |                           |                  | policy protecting the folder. |
                |                           |                  | For example, filter={"protect |
                |                           |                  | ion_info.policy_id":{"$eq":"9 |
                |                           |                  | c2934fc-ff4d-11e9-8e11-       |
                |                           |                  | 76706df7fe01"}}               |
                +---------------------------+------------------+-------------------------------+
                | protection_status         | $in              | The protection status of the  |
                |                           |                  | folder. Refer to the          |
                |                           |                  | Protection Status table for a |
                |                           |                  | complete list of protection   |
                |                           |                  | statuses. For example, filter |
                |                           |                  | ={"protection_status":{"$in": |
                |                           |                  | ["unsupported",               |
                |                           |                  | "protected"]}}                |
                +---------------------------+------------------+-------------------------------+

                *Only one VMware-assigned ID filter parameter can be set at a time. VMware-
                assigned ID filter parameters that cannot be set together include the following:

                parent_folder.id
                datacenter.id

            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-folder-           | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under the folders and subfolders |
                |                                       | of the specified folder. For         |
                |                                       | example, embed=read-vmware-vcenter-  |
                |                                       | folder-compliance-stats              |
                +---------------------------------------+--------------------------------------+

        Returns:
            ListFoldersResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/folders'
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id}
        )
        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter, 'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-folders=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_vmware_vcenter_folders.', errors
            )
        return list_folders_response.ListFoldersResponse.from_dictionary(resp)

    def read_vmware_vcenter_folder(
        self, vcenter_id: str, folder_id: str, embed: str = None
    ) -> read_folder_response.ReadFolderResponse:
        """Returns a representation of the specified VMware folder.

        Args:
            vcenter_id:
                Performs the operation on a folder within the specified vCenter server.
            folder_id:
                Performs the operation on the folder with the specified ID.
            embed:
                Embeds the details of an associated resource. Set the parameter to one of the
                following embeddable links to include additional details associated with the
                resource.

                +---------------------------------------+--------------------------------------+
                |            Embeddable Link            |             Description              |
                +=======================================+======================================+
                | read-vmware-vcenter-folder-           | Embeds the compliance statistics of  |
                | compliance-stats                      | VMs under folders and subfolders of  |
                |                                       | the specified folder. For example,   |
                |                                       | embed=read-vmware-vcenter-folder-    |
                |                                       | compliance-stats                     |
                +---------------------------------------+--------------------------------------+

        Returns:
            ReadFolderResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = (
            f'{self.config.base_path}/datasources/vmware/vcenters/{vcenter_id}/folders/{folder_id}'
        )
        _url_path = api_helper.append_url_with_template_parameters(
            _url_path, {'vcenter_id': vcenter_id, 'folder_id': folder_id}
        )
        _query_parameters = {}
        _query_parameters = {'embed': embed}

        # Prepare headers
        _headers = {
            'accept': 'application/vmware-vcenter-folders=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
        }
        # Execute request
        try:
            resp = self.client.get(_url_path, headers=_headers, params=_query_parameters)
        except requests.exceptions.HTTPError as http_error:
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_vmware_vcenter_folder.', errors
            )
        return read_folder_response.ReadFolderResponse.from_dictionary(resp)
