#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import folder_embedded
from clumioapi.models import folder_links
from clumioapi.models import protection_info
from clumioapi.models import v_mware_v_center_folder_datacenter_model
from clumioapi.models import v_mware_v_center_parent_folder_model

T = TypeVar('T', bound='FolderWithETag')


class FolderWithETag:
    """Implementation of the 'FolderWithETag' model.

    FolderWithETag to support etag string to be calculated

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        datacenter:
            The data center associated with this folder.
        descendant_folder_count:
            Count of all descendant folders inside this folder
        has_child_folders:
            Determines whether the folder has direct child folders.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the folder.
        is_root:
            Determines whether the folder is a hidden root folder. If `true`, the folder is
            a hidden root folder.
        is_supported:
            Determines whether the folder can be used as a restore destination. If `true`,
            the folder can be used as a restore destination, and backups can be restored to
            the folder.
        name:
            The VMware-assigned name of the folder.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the folder.
        parent_folder:
            The parent folder under which this folder resides.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of this folder. Refer to the Protection Status table for a
            complete list of protection statuses.
        p_type:
            The folder type. Examples of folder types include "datacenter_folder" and
            "vm_folder". Refer to the Folder Type table for a complete list of folder types.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'datacenter': 'datacenter',
        'descendant_folder_count': 'descendant_folder_count',
        'has_child_folders': 'has_child_folders',
        'p_id': 'id',
        'is_root': 'is_root',
        'is_supported': 'is_supported',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'parent_folder': 'parent_folder',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'p_type': 'type',
    }

    def __init__(
        self,
        embedded: folder_embedded.FolderEmbedded = None,
        etag: str = None,
        links: folder_links.FolderLinks = None,
        datacenter: v_mware_v_center_folder_datacenter_model.VMwareVCenterFolderDatacenterModel = None,
        descendant_folder_count: int = None,
        has_child_folders: bool = None,
        p_id: str = None,
        is_root: bool = None,
        is_supported: bool = None,
        name: str = None,
        organizational_unit_id: str = None,
        parent_folder: v_mware_v_center_parent_folder_model.VMwareVCenterParentFolderModel = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the FolderWithETag class."""

        # Initialize members of the class
        self.embedded: folder_embedded.FolderEmbedded = embedded
        self.etag: str = etag
        self.links: folder_links.FolderLinks = links
        self.datacenter: (
            v_mware_v_center_folder_datacenter_model.VMwareVCenterFolderDatacenterModel
        ) = datacenter
        self.descendant_folder_count: int = descendant_folder_count
        self.has_child_folders: bool = has_child_folders
        self.p_id: str = p_id
        self.is_root: bool = is_root
        self.is_supported: bool = is_supported
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.parent_folder: v_mware_v_center_parent_folder_model.VMwareVCenterParentFolderModel = (
            parent_folder
        )
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.p_type: str = p_type

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
            folder_embedded.FolderEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            folder_links.FolderLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'datacenter'
        datacenter = (
            v_mware_v_center_folder_datacenter_model.VMwareVCenterFolderDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        descendant_folder_count = dictionary.get('descendant_folder_count')
        has_child_folders = dictionary.get('has_child_folders')
        p_id = dictionary.get('id')
        is_root = dictionary.get('is_root')
        is_supported = dictionary.get('is_supported')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'parent_folder'
        parent_folder = (
            v_mware_v_center_parent_folder_model.VMwareVCenterParentFolderModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            datacenter,
            descendant_folder_count,
            has_child_folders,
            p_id,
            is_root,
            is_supported,
            name,
            organizational_unit_id,
            parent_folder,
            p_protection_info,
            protection_status,
            p_type,
        )
