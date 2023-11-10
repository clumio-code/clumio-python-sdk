#
# Copyright 2023. Clumio, Inc.
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
    _names = {
        'encryption': 'encryption',
        'is_nvme': 'is_nvme',
        'name': 'name',
        'size': 'size',
        'p_type': 'type',
        'virtual_name': 'virtual_name',
    }

    def __init__(
        self,
        encryption: str = None,
        is_nvme: bool = None,
        name: str = None,
        size: int = None,
        p_type: str = None,
        virtual_name: str = None,
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
        encryption = dictionary.get('encryption')
        is_nvme = dictionary.get('is_nvme')
        name = dictionary.get('name')
        size = dictionary.get('size')
        p_type = dictionary.get('type')
        virtual_name = dictionary.get('virtual_name')
        # Return an object of this model
        return cls(encryption, is_nvme, name, size, p_type, virtual_name)
