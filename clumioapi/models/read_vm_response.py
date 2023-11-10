#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_info
from clumioapi.models import vm_compute_resource_folder_model
from clumioapi.models import vm_compute_resource_model
from clumioapi.models import vm_datacenter_folder_model
from clumioapi.models import vm_datacenter_model
from clumioapi.models import vm_embedded
from clumioapi.models import vm_folder_model
from clumioapi.models import vm_host_model
from clumioapi.models import vm_links
from clumioapi.models import vm_nic_model
from clumioapi.models import vm_resource_pool_model
from clumioapi.models import vm_tag_with_category_model

T = TypeVar('T', bound='ReadVmResponse')


class ReadVmResponse:
    """Implementation of the 'ReadVmResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        compliance_status:
            The policy compliance status of the resource. If the VM is deleted or
            unprotected, then this field has a value of `null`. Refer to the Compliance
            Status table for a complete list of compliance statuses.
        compute_resource:
            The compute resource from which the VM draws. If the VM is deleted, then
            `compute_resource.id` has a value of `null`.
        compute_resource_folder:
            The compute resource folder associated with this VM. If the VM is deleted, then
            this field has a value of `null`.
        datacenter:
            The data center in which the VM resides. If the VM is deleted, then
            `datacenter.id` has a value of `null`.
        datacenter_folder:
            The data center folder associated with this VM. If the VM is deleted, then this
            field has a value of `null`.
        host:
            The host on which the VM resides. If the VM is deleted, then `host.id` and
            `host.is_standalone` have values of `null`. The `host.name` field may also have
            a value of `null`.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the VM.
            VMs from different vCenters may have the same VMware-assigned ID.
        is_deleted:
            Determines whether the VM is deleted. If `true`, the VM is deleted.
        is_supported:
            Determines whether the VM is supported for backups. If `true`, the VM is
            supported for backups.
        last_backup_timestamp:
            The timestamp of when the VM was last
            backed up. If this VM has not been backed up, then this field has a value of
            `null`.
        name:
            The name of the virtual machine.
        nics:
            The NICs attached to the VM. If this VM has been deleted, then this field has a
            value of null. Additionally, for active VMs, if a NIC is not connected to any
            network, then the network of that NIC has a value of null.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the VM.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the resource. If the VM has been deleted, then this
            field has a value of `null`. Refer to the Protection Status table for a complete
            list of protection statuses.
        resource_pool:
            The resource pool from which the VM draws. If the VM is deleted, then
            `resource_pool.id` and `resource_pool.is_root` have values of `null`.
        tags:
            The tags applied to the VM. If the VM has been deleted, then `tags.id` and
            `tags.category_id` have values of `null`.
        unsupported_reason:
            The reason why the VM cannot be supported. If the VM is supported, then this
            field has a value of `null`.
        uuid:
            The Clumio-assigned ID of the VM.
            Use this parameter in the [GET /backups/files/search](#operation/list-files)
            endpoint
            to search for files in backups of this VM.
        vm_folder:
            The VM folder containing the VM. If the VM is deleted, then `vm_folder.id` has a
            value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'compliance_status': 'compliance_status',
        'compute_resource': 'compute_resource',
        'compute_resource_folder': 'compute_resource_folder',
        'datacenter': 'datacenter',
        'datacenter_folder': 'datacenter_folder',
        'host': 'host',
        'p_id': 'id',
        'is_deleted': 'is_deleted',
        'is_supported': 'is_supported',
        'last_backup_timestamp': 'last_backup_timestamp',
        'name': 'name',
        'nics': 'nics',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'resource_pool': 'resource_pool',
        'tags': 'tags',
        'unsupported_reason': 'unsupported_reason',
        'uuid': 'uuid',
        'vm_folder': 'vm_folder',
    }

    def __init__(
        self,
        embedded: vm_embedded.VmEmbedded = None,
        links: vm_links.VmLinks = None,
        compliance_status: str = None,
        compute_resource: vm_compute_resource_model.VMComputeResourceModel = None,
        compute_resource_folder: vm_compute_resource_folder_model.VMComputeResourceFolderModel = None,
        datacenter: vm_datacenter_model.VMDatacenterModel = None,
        datacenter_folder: vm_datacenter_folder_model.VMDatacenterFolderModel = None,
        host: vm_host_model.VMHostModel = None,
        p_id: str = None,
        is_deleted: bool = None,
        is_supported: bool = None,
        last_backup_timestamp: str = None,
        name: str = None,
        nics: Sequence[vm_nic_model.VMNicModel] = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
        resource_pool: vm_resource_pool_model.VMResourcePoolModel = None,
        tags: Sequence[vm_tag_with_category_model.VMTagWithCategoryModel] = None,
        unsupported_reason: str = None,
        uuid: str = None,
        vm_folder: vm_folder_model.VMFolderModel = None,
    ) -> None:
        """Constructor for the ReadVmResponse class."""

        # Initialize members of the class
        self.embedded: vm_embedded.VmEmbedded = embedded
        self.links: vm_links.VmLinks = links
        self.compliance_status: str = compliance_status
        self.compute_resource: vm_compute_resource_model.VMComputeResourceModel = compute_resource
        self.compute_resource_folder: vm_compute_resource_folder_model.VMComputeResourceFolderModel = (
            compute_resource_folder
        )
        self.datacenter: vm_datacenter_model.VMDatacenterModel = datacenter
        self.datacenter_folder: vm_datacenter_folder_model.VMDatacenterFolderModel = (
            datacenter_folder
        )
        self.host: vm_host_model.VMHostModel = host
        self.p_id: str = p_id
        self.is_deleted: bool = is_deleted
        self.is_supported: bool = is_supported
        self.last_backup_timestamp: str = last_backup_timestamp
        self.name: str = name
        self.nics: Sequence[vm_nic_model.VMNicModel] = nics
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.resource_pool: vm_resource_pool_model.VMResourcePoolModel = resource_pool
        self.tags: Sequence[vm_tag_with_category_model.VMTagWithCategoryModel] = tags
        self.unsupported_reason: str = unsupported_reason
        self.uuid: str = uuid
        self.vm_folder: vm_folder_model.VMFolderModel = vm_folder

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
            vm_embedded.VmEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            vm_links.VmLinks.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None
        )

        compliance_status = dictionary.get('compliance_status')
        key = 'compute_resource'
        compute_resource = (
            vm_compute_resource_model.VMComputeResourceModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'compute_resource_folder'
        compute_resource_folder = (
            vm_compute_resource_folder_model.VMComputeResourceFolderModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'datacenter'
        datacenter = (
            vm_datacenter_model.VMDatacenterModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'datacenter_folder'
        datacenter_folder = (
            vm_datacenter_folder_model.VMDatacenterFolderModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'host'
        host = (
            vm_host_model.VMHostModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        is_deleted = dictionary.get('is_deleted')
        is_supported = dictionary.get('is_supported')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        name = dictionary.get('name')
        nics = None
        if dictionary.get('nics'):
            nics = list()
            for value in dictionary.get('nics'):
                nics.append(vm_nic_model.VMNicModel.from_dictionary(value))

        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        key = 'resource_pool'
        resource_pool = (
            vm_resource_pool_model.VMResourcePoolModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(
                    vm_tag_with_category_model.VMTagWithCategoryModel.from_dictionary(value)
                )

        unsupported_reason = dictionary.get('unsupported_reason')
        uuid = dictionary.get('uuid')
        key = 'vm_folder'
        vm_folder = (
            vm_folder_model.VMFolderModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            embedded,
            links,
            compliance_status,
            compute_resource,
            compute_resource_folder,
            datacenter,
            datacenter_folder,
            host,
            p_id,
            is_deleted,
            is_supported,
            last_backup_timestamp,
            name,
            nics,
            organizational_unit_id,
            p_protection_info,
            protection_status,
            resource_pool,
            tags,
            unsupported_reason,
            uuid,
            vm_folder,
        )
