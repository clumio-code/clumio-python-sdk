#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting

T = TypeVar('T', bound='CreateBackupVmwareVmV1Request')


class CreateBackupVmwareVmV1Request:
    """Implementation of the 'CreateBackupVmwareVmV1Request' model.

    Attributes:
        settings:
            Settings for requesting on-demand backup directly.
        vcenter_id:
            Performs the operation on a VM within the specified vCenter server.
        vm_id:
            Performs the operation on the VM with the specified VMware-assigned Managed
            Object Reference (MoRef) ID.
    """

    # Create a mapping from Model property names to API property names
    _names = {'settings': 'settings', 'vcenter_id': 'vcenter_id', 'vm_id': 'vm_id'}

    def __init__(
        self,
        settings: on_demand_setting.OnDemandSetting = None,
        vcenter_id: str = None,
        vm_id: str = None,
    ) -> None:
        """Constructor for the CreateBackupVmwareVmV1Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting.OnDemandSetting = settings
        self.vcenter_id: str = vcenter_id
        self.vm_id: str = vm_id

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
        key = 'settings'
        settings = (
            on_demand_setting.OnDemandSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        vcenter_id = dictionary.get('vcenter_id')
        vm_id = dictionary.get('vm_id')
        # Return an object of this model
        return cls(settings, vcenter_id, vm_id)
