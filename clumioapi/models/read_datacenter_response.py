#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ancestor_ref_model
from clumioapi.models import datacenter_embedded
from clumioapi.models import datacenter_links
from clumioapi.models import protection_info
from clumioapi.models import v_mware_datacenter_folder_id_model
from clumioapi.models import v_mware_root_compute_resource_folder_id_model
from clumioapi.models import v_mware_root_vm_folder_id_model

T = TypeVar('T', bound='ReadDatacenterResponse')


class ReadDatacenterResponse:
    """Implementation of the 'ReadDatacenterResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        ancestor_refs:
            The ancestor (parent) of the data center.
        datacenter_folder:
            The data center folder in which the data center resides.
        has_compute_resources:
            Determines whether compute resources exist directly under the hidden root
            compute resource folder. If `true`, then compute resources exist directly under
            the root compute resource folder.
        has_vm_folders:
            Determines whether VMs exist directly under the hidden root VM folder. If
            `true`, then VMs exist directly under the root VM folder.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the data center.
        name:
            The VMware-assigned name of this data center.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            datacenter.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of this data center. Refer to the Protection Status table
            for a complete list of protection statuses.
        root_compute_resource_folder:
            The hidden root compute resource folder of the data center.
        root_vm_folder:
            The hidden root virtual machine folder of the data center.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'ancestor_refs': 'ancestor_refs',
        'datacenter_folder': 'datacenter_folder',
        'has_compute_resources': 'has_compute_resources',
        'has_vm_folders': 'has_vm_folders',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'root_compute_resource_folder': 'root_compute_resource_folder',
        'root_vm_folder': 'root_vm_folder',
    }

    def __init__(
        self,
        embedded: datacenter_embedded.DatacenterEmbedded = None,
        etag: str = None,
        links: datacenter_links.DatacenterLinks = None,
        ancestor_refs: Sequence[ancestor_ref_model.AncestorRefModel] = None,
        datacenter_folder: v_mware_datacenter_folder_id_model.VMwareDatacenterFolderIDModel = None,
        has_compute_resources: bool = None,
        has_vm_folders: bool = None,
        p_id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
        root_compute_resource_folder: v_mware_root_compute_resource_folder_id_model.VMwareRootComputeResourceFolderIDModel = None,
        root_vm_folder: v_mware_root_vm_folder_id_model.VMwareRootVMFolderIDModel = None,
    ) -> None:
        """Constructor for the ReadDatacenterResponse class."""

        # Initialize members of the class
        self.embedded: datacenter_embedded.DatacenterEmbedded = embedded
        self.etag: str = etag
        self.links: datacenter_links.DatacenterLinks = links
        self.ancestor_refs: Sequence[ancestor_ref_model.AncestorRefModel] = ancestor_refs
        self.datacenter_folder: v_mware_datacenter_folder_id_model.VMwareDatacenterFolderIDModel = (
            datacenter_folder
        )
        self.has_compute_resources: bool = has_compute_resources
        self.has_vm_folders: bool = has_vm_folders
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.root_compute_resource_folder: v_mware_root_compute_resource_folder_id_model.VMwareRootComputeResourceFolderIDModel = (
            root_compute_resource_folder
        )
        self.root_vm_folder: v_mware_root_vm_folder_id_model.VMwareRootVMFolderIDModel = (
            root_vm_folder
        )

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None

        # Extract variables from the dictionary
        key = '_embedded'
        embedded = (
            datacenter_embedded.DatacenterEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            datacenter_links.DatacenterLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        ancestor_refs = None
        if dictionary.get('ancestor_refs'):
            ancestor_refs = list()
            for value in dictionary.get('ancestor_refs'):
                ancestor_refs.append(ancestor_ref_model.AncestorRefModel.from_dictionary(value))

        key = 'datacenter_folder'
        datacenter_folder = (
            v_mware_datacenter_folder_id_model.VMwareDatacenterFolderIDModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        has_compute_resources = dictionary.get('has_compute_resources')
        has_vm_folders = dictionary.get('has_vm_folders')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        key = 'root_compute_resource_folder'
        root_compute_resource_folder = (
            v_mware_root_compute_resource_folder_id_model.VMwareRootComputeResourceFolderIDModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'root_vm_folder'
        root_vm_folder = (
            v_mware_root_vm_folder_id_model.VMwareRootVMFolderIDModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            ancestor_refs,
            datacenter_folder,
            has_compute_resources,
            has_vm_folders,
            p_id,
            name,
            organizational_unit_id,
            p_protection_info,
            protection_status,
            root_compute_resource_folder,
            root_vm_folder,
        )
