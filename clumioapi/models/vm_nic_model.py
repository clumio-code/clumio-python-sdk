#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import vm_nic_network_model

T = TypeVar('T', bound='VMNicModel')


class VMNicModel:
    """Implementation of the 'VMNicModel' model.

    The network interface card (NIC) attached to the VM.

    Attributes:
        mac_address:
            The MAC address of the NIC.
        network:
            The network associated with this NIC.
    """

    # Create a mapping from Model property names to API property names
    _names = {'mac_address': 'mac_address', 'network': 'network'}

    def __init__(
        self, mac_address: str = None, network: vm_nic_network_model.VMNicNetworkModel = None
    ) -> None:
        """Constructor for the VMNicModel class."""

        # Initialize members of the class
        self.mac_address: str = mac_address
        self.network: vm_nic_network_model.VMNicNetworkModel = network

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
        mac_address = dictionary.get('mac_address')
        key = 'network'
        network = (
            vm_nic_network_model.VMNicNetworkModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(mac_address, network)
