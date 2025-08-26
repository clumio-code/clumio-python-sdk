#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='NetworkInterface')


class NetworkInterface:
    """Implementation of the 'NetworkInterface' model.

    Attributes:
        device_index:
            The device index for the network interface.
        network_interface_native_id:
            The AWS-assigned ID for the network interface.
        public_ip:
            The public IP v4 address of the network interface if one was assigned.
        security_group_native_ids:
            The AWS-assigned IDs for the security groups associated with this network
            interface.
        subnet_native_id:
            The subnet native ID for the network interface.
        virtual_name:
            The AWS-assigned name of the network interface. For example, `eth0`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'device_index': 'device_index',
        'network_interface_native_id': 'network_interface_native_id',
        'public_ip': 'public_ip',
        'security_group_native_ids': 'security_group_native_ids',
        'subnet_native_id': 'subnet_native_id',
        'virtual_name': 'virtual_name',
    }

    def __init__(
        self,
        device_index: int | None = None,
        network_interface_native_id: str | None = None,
        public_ip: str | None = None,
        security_group_native_ids: Sequence[str] | None = None,
        subnet_native_id: str | None = None,
        virtual_name: str | None = None,
    ) -> None:
        """Constructor for the NetworkInterface class."""

        # Initialize members of the class
        self.device_index: int | None = device_index
        self.network_interface_native_id: str | None = network_interface_native_id
        self.public_ip: str | None = public_ip
        self.security_group_native_ids: Sequence[str] | None = security_group_native_ids
        self.subnet_native_id: str | None = subnet_native_id
        self.virtual_name: str | None = virtual_name

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
