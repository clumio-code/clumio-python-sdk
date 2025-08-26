#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='NetworkInterface')


@dataclasses.dataclass
class NetworkInterface:
    """Implementation of the 'NetworkInterface' model.

    Attributes:
        DeviceIndex:
            The device index for the network interface.

        NetworkInterfaceNativeId:
            The aws-assigned id for the network interface.

        PublicIp:
            The public ip v4 address of the network interface if one was assigned.

        SecurityGroupNativeIds:
            The aws-assigned ids for the security groups associated with this network interface.

        SubnetNativeId:
            The subnet native id for the network interface.

        VirtualName:
            The aws-assigned name of the network interface. for example, `eth0`.

    """

    DeviceIndex: int | None = None
    NetworkInterfaceNativeId: str | None = None
    PublicIp: str | None = None
    SecurityGroupNativeIds: Sequence[str] | None = None
    SubnetNativeId: str | None = None
    VirtualName: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('device_index', None)
        val_device_index = val

        val = dictionary.get('network_interface_native_id', None)
        val_network_interface_native_id = val

        val = dictionary.get('public_ip', None)
        val_public_ip = val

        val = dictionary.get('security_group_native_ids', None)
        val_security_group_native_ids = val

        val = dictionary.get('subnet_native_id', None)
        val_subnet_native_id = val

        val = dictionary.get('virtual_name', None)
        val_virtual_name = val

        # Return an object of this model
        return cls(
            val_device_index,
            val_network_interface_native_id,
            val_public_ip,
            val_security_group_native_ids,
            val_subnet_native_id,
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
