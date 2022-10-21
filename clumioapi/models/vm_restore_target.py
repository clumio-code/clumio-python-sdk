#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import vm_nic_restore, vm_restore_tag

T = TypeVar('T', bound='VMRestoreTarget')


class VMRestoreTarget:
    """Implementation of the 'VMRestoreTarget' model.

    The configuration of the VM to be restored.

    Attributes:
        datacenter_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the data center to be
            used as the restore destination. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/datacenters](#operation/list-vmware-
            vcenter-datacenters) endpoint to fetch valid values.
        datastore_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the VMFS datastore to
            be used as the restore destination. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/datastores](#operation/list-vmware-
            vcenter-datastores) endpoint to fetch valid values.
            While performing an in-place restore, this parameter is optional.
            If `"options.restore_in_place":false`, then this parameter is required.
        host_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the vSphere host to
            be used as the restore destination. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/hosts](#operation/list-vmware-vcenter-
            hosts) endpoint to fetch valid values.
            If provided, the specified host (`host_id`) must belong to a compute resource
            that is the parent of the specified resource pool (`resource_pool_id`).
            If not provided, the VMware Distributed Resource Scheduler (DRS) will
            automatically select a host that belongs to a compute resource that is the
            parent of the specified resource pool (`resource_pool_id`).
        network_options:
            The network connections for the restored VM. Multiple network connections can be
            configured.
        parent_vm_folder_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the VM folder to be
            used as the restore destination. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/folders](#operation/list-vmware-
            vcenter-folders) endpoint to fetch valid values.
        resource_pool_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool to
            be used as the restore destination. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/resource-pools](#operation/list-
            vmware-vcenter-resource-pools) endpoint to fetch valid values.
        should_power_on:
            Determines whether the VM should remain powered on after the restore. If `true`,
            the VM will remain powered on after the restore. Users may choose to power off a
            VM to change the network configurations.
        tags:
            The VMware-assigned tags to be associated with the restored VM. A VM can be
            associated with multiple tags.
            The restored VM will not inherit any tags that were associated with the original
            VM.
            To find the tags that were associated with the original VM,
            use the [GET /backups/vmware/vms](#operation/list-backup-vmware-vms) endpoint to
            display the original VM's tag keys (``) and tag values (``).
        vcenter_id:
            The Clumio-assigned ID of the vCenter to be used as the restore destination.
        vm_name:
            The name given to the restored VM. The VM name cannot exceed 80 characters in
            length and must follow VMware VM naming conventions.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'datacenter_id': 'datacenter_id',
        'datastore_id': 'datastore_id',
        'host_id': 'host_id',
        'network_options': 'network_options',
        'parent_vm_folder_id': 'parent_vm_folder_id',
        'resource_pool_id': 'resource_pool_id',
        'should_power_on': 'should_power_on',
        'tags': 'tags',
        'vcenter_id': 'vcenter_id',
        'vm_name': 'vm_name',
    }

    def __init__(
        self,
        datacenter_id: str = None,
        datastore_id: str = None,
        host_id: str = None,
        network_options: Sequence[vm_nic_restore.VMNicRestore] = None,
        parent_vm_folder_id: str = None,
        resource_pool_id: str = None,
        should_power_on: bool = None,
        tags: Sequence[vm_restore_tag.VMRestoreTag] = None,
        vcenter_id: str = None,
        vm_name: str = None,
    ) -> None:
        """Constructor for the VMRestoreTarget class."""

        # Initialize members of the class
        self.datacenter_id: str = datacenter_id
        self.datastore_id: str = datastore_id
        self.host_id: str = host_id
        self.network_options: Sequence[vm_nic_restore.VMNicRestore] = network_options
        self.parent_vm_folder_id: str = parent_vm_folder_id
        self.resource_pool_id: str = resource_pool_id
        self.should_power_on: bool = should_power_on
        self.tags: Sequence[vm_restore_tag.VMRestoreTag] = tags
        self.vcenter_id: str = vcenter_id
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
        datacenter_id = dictionary.get('datacenter_id')
        datastore_id = dictionary.get('datastore_id')
        host_id = dictionary.get('host_id')
        network_options = None
        if dictionary.get('network_options'):
            network_options = list()
            for value in dictionary.get('network_options'):
                network_options.append(vm_nic_restore.VMNicRestore.from_dictionary(value))

        parent_vm_folder_id = dictionary.get('parent_vm_folder_id')
        resource_pool_id = dictionary.get('resource_pool_id')
        should_power_on = dictionary.get('should_power_on')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(vm_restore_tag.VMRestoreTag.from_dictionary(value))

        vcenter_id = dictionary.get('vcenter_id')
        vm_name = dictionary.get('vm_name')
        # Return an object of this model
        return cls(
            datacenter_id,
            datastore_id,
            host_id,
            network_options,
            parent_vm_folder_id,
            resource_pool_id,
            should_power_on,
            tags,
            vcenter_id,
            vm_name,
        )
