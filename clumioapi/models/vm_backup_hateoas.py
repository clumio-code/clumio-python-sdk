#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import (
    vm_backup_hateoas_links,
    vm_nic_backup_model,
    vm_tag_with_category_model,
)

T = TypeVar('T', bound='VMBackupHateoas')


class VMBackupHateoas:
    """Implementation of the 'VMBackupHateoas' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        browsing_failed_reason:
            The reason that browsing is unavailable for the backup. Possible values include
            "file_limit_exceeded" and
            "browsing_unavailable". If browse indexing is successful, then this field has a
            value of `null`.
        datacenter_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the data center
            associated with this backup.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        host_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the
            host associated with this backup.
        id:
            The Clumio-assigned ID of the backup.
        is_browsable:
            Determines whether browsing is available for the backup. If `true`, then
            browsing is available for the backup.
        nics:
            The network interface controller (NIC) information for the VM at the time of
            backup.
        resource_pool_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool
            associated with this backup.
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        tags:
            The VMware-assigned tags associated with the VM at the time of backup.
        vcenter_endpoint:
            The IP address or FQDN of the vCenter server associated with this backup.
            If a backup was initiated before 2020-06-30, when this field was introduced,
            then this field has a value of `null`.
        vcenter_id:
            The Clumio-assigned ID of the vCenter associated with this backup.
        vm_folder_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the
            VM folder associated with this backup.
        vm_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the
            VM associated with this backup.
        vm_name:
            The name of the virtual machine associated with this backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'browsing_failed_reason': 'browsing_failed_reason',
        'datacenter_id': 'datacenter_id',
        'expiration_timestamp': 'expiration_timestamp',
        'host_id': 'host_id',
        'id': 'id',
        'is_browsable': 'is_browsable',
        'nics': 'nics',
        'resource_pool_id': 'resource_pool_id',
        'start_timestamp': 'start_timestamp',
        'tags': 'tags',
        'vcenter_endpoint': 'vcenter_endpoint',
        'vcenter_id': 'vcenter_id',
        'vm_folder_id': 'vm_folder_id',
        'vm_id': 'vm_id',
        'vm_name': 'vm_name',
    }

    def __init__(
        self,
        links: vm_backup_hateoas_links.VMBackupHateoasLinks = None,
        browsing_failed_reason: str = None,
        datacenter_id: str = None,
        expiration_timestamp: str = None,
        host_id: str = None,
        id: str = None,
        is_browsable: bool = None,
        nics: Sequence[vm_nic_backup_model.VMNicBackupModel] = None,
        resource_pool_id: str = None,
        start_timestamp: str = None,
        tags: Sequence[vm_tag_with_category_model.VMTagWithCategoryModel] = None,
        vcenter_endpoint: str = None,
        vcenter_id: str = None,
        vm_folder_id: str = None,
        vm_id: str = None,
        vm_name: str = None,
    ) -> None:
        """Constructor for the VMBackupHateoas class."""

        # Initialize members of the class
        self.links: vm_backup_hateoas_links.VMBackupHateoasLinks = links
        self.browsing_failed_reason: str = browsing_failed_reason
        self.datacenter_id: str = datacenter_id
        self.expiration_timestamp: str = expiration_timestamp
        self.host_id: str = host_id
        self.id: str = id
        self.is_browsable: bool = is_browsable
        self.nics: Sequence[vm_nic_backup_model.VMNicBackupModel] = nics
        self.resource_pool_id: str = resource_pool_id
        self.start_timestamp: str = start_timestamp
        self.tags: Sequence[vm_tag_with_category_model.VMTagWithCategoryModel] = tags
        self.vcenter_endpoint: str = vcenter_endpoint
        self.vcenter_id: str = vcenter_id
        self.vm_folder_id: str = vm_folder_id
        self.vm_id: str = vm_id
        self.vm_name: str = vm_name

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
        key = '_links'
        links = (
            vm_backup_hateoas_links.VMBackupHateoasLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        browsing_failed_reason = dictionary.get('browsing_failed_reason')
        datacenter_id = dictionary.get('datacenter_id')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        host_id = dictionary.get('host_id')
        id = dictionary.get('id')
        is_browsable = dictionary.get('is_browsable')
        nics = None
        if dictionary.get('nics'):
            nics = list()
            for value in dictionary.get('nics'):
                nics.append(vm_nic_backup_model.VMNicBackupModel.from_dictionary(value))

        resource_pool_id = dictionary.get('resource_pool_id')
        start_timestamp = dictionary.get('start_timestamp')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(
                    vm_tag_with_category_model.VMTagWithCategoryModel.from_dictionary(value)
                )

        vcenter_endpoint = dictionary.get('vcenter_endpoint')
        vcenter_id = dictionary.get('vcenter_id')
        vm_folder_id = dictionary.get('vm_folder_id')
        vm_id = dictionary.get('vm_id')
        vm_name = dictionary.get('vm_name')
        # Return an object of this model
        return cls(
            links,
            browsing_failed_reason,
            datacenter_id,
            expiration_timestamp,
            host_id,
            id,
            is_browsable,
            nics,
            resource_pool_id,
            start_timestamp,
            tags,
            vcenter_endpoint,
            vcenter_id,
            vm_folder_id,
            vm_id,
            vm_name,
        )
