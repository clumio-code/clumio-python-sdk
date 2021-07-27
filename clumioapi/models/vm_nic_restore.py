#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMNicRestore')


class VMNicRestore:
    """Implementation of the 'VMNicRestore' model.

    Attributes:
        mac_address:
            The unique media access control (MAC) address assigned to the network interface
            card (NIC). The MAC address is assigned through the vSphere client.
        network_id:
            The network connection for the virtual NIC. The NIC is configured in the vSphere
            client. Use the [GET
            /datasources/vmware/vcenters/{vcenter_id}/networks](#operation/list-vmware-
            vcenter-networks) endpoint to fetch valid values.
        should_connect:
            Determines whether the restored VM should automatically connect to the specified
            network after a restore.
            If `true`, the restored VM will automatically connect to the specified network
            after a restore.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'mac_address': 'mac_address',
        'network_id': 'network_id',
        'should_connect': 'should_connect',
    }

    def __init__(
        self, mac_address: str = None, network_id: str = None, should_connect: bool = None
    ) -> None:
        """Constructor for the VMNicRestore class."""

        # Initialize members of the class
        self.mac_address: str = mac_address
        self.network_id: str = network_id
        self.should_connect: bool = should_connect

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
        network_id = dictionary.get('network_id')
        should_connect = dictionary.get('should_connect')
        # Return an object of this model
        return cls(mac_address, network_id, should_connect)
