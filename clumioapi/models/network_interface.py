#
# Copyright 2023. Clumio, Inc.
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
    _names = {
        'device_index': 'device_index',
        'network_interface_native_id': 'network_interface_native_id',
        'public_ip': 'public_ip',
        'security_group_native_ids': 'security_group_native_ids',
        'subnet_native_id': 'subnet_native_id',
        'virtual_name': 'virtual_name',
    }

    def __init__(
        self,
        device_index: int = None,
        network_interface_native_id: str = None,
        public_ip: str = None,
        security_group_native_ids: Sequence[str] = None,
        subnet_native_id: str = None,
        virtual_name: str = None,
    ) -> None:
        """Constructor for the NetworkInterface class."""

        # Initialize members of the class
        self.device_index: int = device_index
        self.network_interface_native_id: str = network_interface_native_id
        self.public_ip: str = public_ip
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.subnet_native_id: str = subnet_native_id
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
        device_index = dictionary.get('device_index')
        network_interface_native_id = dictionary.get('network_interface_native_id')
        public_ip = dictionary.get('public_ip')
        security_group_native_ids = dictionary.get('security_group_native_ids')
        subnet_native_id = dictionary.get('subnet_native_id')
        virtual_name = dictionary.get('virtual_name')
        # Return an object of this model
        return cls(
            device_index,
            network_interface_native_id,
            public_ip,
            security_group_native_ids,
            subnet_native_id,
            virtual_name,
        )
