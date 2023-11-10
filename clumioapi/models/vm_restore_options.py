#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMRestoreOptions')


class VMRestoreOptions:
    """Implementation of the 'VMRestoreOptions' model.

    Additional VM restore options.

    Attributes:
        attempt_rapid_recovery:
            Determines whether a VM rapid recovery should be attempted or not.
            As a part of the rapid recovery, by default the Clumio backup service
            attempts the following Reverse Change Block Tracking (RCBT) operation. It
            retrieves the blocks changed since the backup was taken and applies them
            into a clone of the original VM to rollback the VM to the previous point
            in time. As a result typically it is much faster to restore a VM using
            rapid recovery RCBT. However if the clone operation is not desired to be
            performed for some reason, then rapid recovery RCBT can be turned off
            using this field.
            It is applicable to both in-place restore and restore to a new VM.
            If it is not set, then the behavior is same as setting it to true.
            If true or unset, rapid recovery is attempted first. If rapid recovery
            fails, then a full VM restore is performed.
            If false, rapid recovery is not attempted.
        clone_source_vm:
            Determines whether to preserve the original data by cloning the existing
            VM before performing an in-place restore.
            If `"restore_in_place":false`, then this parameter is ignored.
            If true, the original data is preserved by creating a clone of the VM.
            If false, a clone is not created. The original data in the source VM may
            get over-written by the restored data.
        cloned_vm_datastore_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the VMFS
            datastore to be used as the destination for the cloned VM.
            Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/datastores](#operation/list-vmware-
            vcenter-datastores) endpoint to fetch valid values.
            This field is required only if `"clone_source_vm":true`.
        cloned_vm_name:
            The name given to the cloned VM (see clone_source_vm parameter).
            The VM name cannot exceed 80 characters in length and must follow VMware
            VM naming conventions.
            This field is required only if `"clone_source_vm":true`.
        restore_in_place:
            Determines whether the restore should overwrite the existing VM i.e.
            perform an in-place restore or create a new VM for restore.
            If true, the existing VM is used for the restore. In this case if the VM
            is already deleted, the restore will fail.
            If false, a new VM is created for the restore. In this case if the VM
            is already deleted, the restore will still proceed.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'attempt_rapid_recovery': 'attempt_rapid_recovery',
        'clone_source_vm': 'clone_source_vm',
        'cloned_vm_datastore_id': 'cloned_vm_datastore_id',
        'cloned_vm_name': 'cloned_vm_name',
        'restore_in_place': 'restore_in_place',
    }

    def __init__(
        self,
        attempt_rapid_recovery: bool = None,
        clone_source_vm: bool = None,
        cloned_vm_datastore_id: str = None,
        cloned_vm_name: str = None,
        restore_in_place: bool = None,
    ) -> None:
        """Constructor for the VMRestoreOptions class."""

        # Initialize members of the class
        self.attempt_rapid_recovery: bool = attempt_rapid_recovery
        self.clone_source_vm: bool = clone_source_vm
        self.cloned_vm_datastore_id: str = cloned_vm_datastore_id
        self.cloned_vm_name: str = cloned_vm_name
        self.restore_in_place: bool = restore_in_place

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
        attempt_rapid_recovery = dictionary.get('attempt_rapid_recovery')
        clone_source_vm = dictionary.get('clone_source_vm')
        cloned_vm_datastore_id = dictionary.get('cloned_vm_datastore_id')
        cloned_vm_name = dictionary.get('cloned_vm_name')
        restore_in_place = dictionary.get('restore_in_place')
        # Return an object of this model
        return cls(
            attempt_rapid_recovery,
            clone_source_vm,
            cloned_vm_datastore_id,
            cloned_vm_name,
            restore_in_place,
        )
