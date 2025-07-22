#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='InstanceStoreBlockDeviceMapping')


class InstanceStoreBlockDeviceMapping:
    """Implementation of the 'InstanceStoreBlockDeviceMapping' model.

    Attributes:
        encryption:
            Encryption for the instance store volume. Possible values include 'hardware
            encrypted'
            and 'Not encrypted'.
        is_nvme:
            Determines whether or not the volume is a NVME instance store volume or a
            non-NVME instance store volume.
        name:
            The device name for the instance store volume. For example, '/dev/sdb'.
        size:
            The size of the instance store volume. Measured in bytes (B).
        p_type:
            The type of the block device. Only possible value is "Instance Store".
        virtual_name:
            The AWS-assigned name of the instance store volume.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'encryption': 'encryption',
        'is_nvme': 'is_nvme',
        'name': 'name',
        'size': 'size',
        'p_type': 'type',
        'virtual_name': 'virtual_name',
    }

    def __init__(
        self, encryption: str, is_nvme: bool, name: str, size: int, p_type: str, virtual_name: str
    ) -> None:
        """Constructor for the InstanceStoreBlockDeviceMapping class."""

        # Initialize members of the class
        self.encryption: str = encryption
        self.is_nvme: bool = is_nvme
        self.name: str = name
        self.size: int = size
        self.p_type: str = p_type
        self.virtual_name: str = virtual_name

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        # Extract variables from the dictionary
        val = dictionary['encryption']
        val_encryption = val

        val = dictionary['is_nvme']
        val_is_nvme = val

        val = dictionary['name']
        val_name = val

        val = dictionary['size']
        val_size = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['virtual_name']
        val_virtual_name = val

        # Return an object of this model
        return cls(
            val_encryption,  # type: ignore
            val_is_nvme,  # type: ignore
            val_name,  # type: ignore
            val_size,  # type: ignore
            val_p_type,  # type: ignore
            val_virtual_name,  # type: ignore
        )
