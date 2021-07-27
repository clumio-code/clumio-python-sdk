#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import protect_entities_hateoas_link
from clumioapi.models import read_policy_definition_hateoas_link
from clumioapi.models import unprotect_entities_hateoas_link
from clumioapi.models import vm_compute_resource_link
from clumioapi.models import vm_datacenter_link
from clumioapi.models import vm_folder_link

T = TypeVar('T', bound='VmLinks')


class VmLinks:
    """Implementation of the 'VmLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        create_backup_vmware_vm:
            A resource-specific HATEOAS link.
        list_backup_vmware_vms:
            A resource-specific HATEOAS link.
        list_restored_files:
            A resource-specific HATEOAS link.
        protect_entities:
            A HATEOAS link to protect the entities.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        read_vmware_vcenter_compute_resource:
            A HATEOAS link to the compute resource from which this VM draws from. Will be
            omitted for deleted VMs.
        read_vmware_vcenter_datacenter:
            A HATEOAS link to the data center in which this VM resides. Will be omitted for
            deleted VMs.
        read_vmware_vcenter_folder:
            A HATEOAS link to the VM folder in which this VM resides. Will be omitted for
            deleted VMs.
        unprotect_entities:
            A HATEOAS link to unprotect the entities.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'create_backup_vmware_vm': 'create-backup-vmware-vm',
        'list_backup_vmware_vms': 'list-backup-vmware-vms',
        'list_restored_files': 'list-restored-files',
        'protect_entities': 'protect-entities',
        'read_policy_definition': 'read-policy-definition',
        'read_vmware_vcenter_compute_resource': 'read-vmware-vcenter-compute-resource',
        'read_vmware_vcenter_datacenter': 'read-vmware-vcenter-datacenter',
        'read_vmware_vcenter_folder': 'read-vmware-vcenter-folder',
        'unprotect_entities': 'unprotect-entities',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        create_backup_vmware_vm: hateoas_link.HateoasLink = None,
        list_backup_vmware_vms: hateoas_link.HateoasLink = None,
        list_restored_files: hateoas_link.HateoasLink = None,
        protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        read_vmware_vcenter_compute_resource: vm_compute_resource_link.VmComputeResourceLink = None,
        read_vmware_vcenter_datacenter: vm_datacenter_link.VmDatacenterLink = None,
        read_vmware_vcenter_folder: vm_folder_link.VmFolderLink = None,
        unprotect_entities: unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink = None,
    ) -> None:
        """Constructor for the VmLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.create_backup_vmware_vm: hateoas_link.HateoasLink = create_backup_vmware_vm
        self.list_backup_vmware_vms: hateoas_link.HateoasLink = list_backup_vmware_vms
        self.list_restored_files: hateoas_link.HateoasLink = list_restored_files
        self.protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = (
            protect_entities
        )
        self.read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = (
            read_policy_definition
        )
        self.read_vmware_vcenter_compute_resource: vm_compute_resource_link.VmComputeResourceLink = (
            read_vmware_vcenter_compute_resource
        )
        self.read_vmware_vcenter_datacenter: vm_datacenter_link.VmDatacenterLink = (
            read_vmware_vcenter_datacenter
        )
        self.read_vmware_vcenter_folder: vm_folder_link.VmFolderLink = read_vmware_vcenter_folder
        self.unprotect_entities: unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink = (
            unprotect_entities
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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'create-backup-vmware-vm'
        create_backup_vmware_vm = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'list-backup-vmware-vms'
        list_backup_vmware_vms = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'list-restored-files'
        list_restored_files = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'protect-entities'
        protect_entities = (
            protect_entities_hateoas_link.ProtectEntitiesHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'read-policy-definition'
        read_policy_definition = (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'read-vmware-vcenter-compute-resource'
        read_vmware_vcenter_compute_resource = (
            vm_compute_resource_link.VmComputeResourceLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-vmware-vcenter-datacenter'
        read_vmware_vcenter_datacenter = (
            vm_datacenter_link.VmDatacenterLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-vmware-vcenter-folder'
        read_vmware_vcenter_folder = (
            vm_folder_link.VmFolderLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'unprotect-entities'
        unprotect_entities = (
            unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            create_backup_vmware_vm,
            list_backup_vmware_vms,
            list_restored_files,
            protect_entities,
            read_policy_definition,
            read_vmware_vcenter_compute_resource,
            read_vmware_vcenter_datacenter,
            read_vmware_vcenter_folder,
            unprotect_entities,
        )
