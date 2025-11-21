#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='InstanceStoreBlockDeviceMapping')


@dataclasses.dataclass
class InstanceStoreBlockDeviceMapping:
    """Implementation of the 'InstanceStoreBlockDeviceMapping' model.

    Attributes:
        Encryption:
            Encryption for the instance store volume. possible values include 'hardware
            encrypted'
            and 'not encrypted'.

        IsNvme:
            Determines whether or not the volume is a nvme instance store volume or a
            non-nvme instance store volume.

        Name:
            The device name for the instance store volume. for example, '/dev/sdb'.

        Size:
            The size of the instance store volume. measured in bytes (b).

        Type:
            The type of the block device. only possible value is "instance store".

        VirtualName:
            The aws-assigned name of the instance store volume.

    """

    Encryption: str | None = None
    IsNvme: bool | None = None
    Name: str | None = None
    Size: int | None = None
    Type: str | None = None
    VirtualName: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('encryption', None)
        val_encryption = val

        val = dictionary.get('is_nvme', None)
        val_is_nvme = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('virtual_name', None)
        val_virtual_name = val

        # Return an object of this model
        return cls(
            val_encryption,
            val_is_nvme,
            val_name,
            val_size,
            val_type,
            val_virtual_name,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
