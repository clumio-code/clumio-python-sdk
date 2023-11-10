#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMNicBackupModel')


class VMNicBackupModel:
    """Implementation of the 'VMNicBackupModel' model.

    Attributes:
        is_connected:
            Determines whether the NIC was connected to the network at the time of backup.
            If `true`, the NIC was connected to the network at the time of backup.
        mac_address:
            The media access control (MAC) address assigned to the NIC. The MAC address is
            assigned through the vSphere client.
        network_id:
            The network to which the NIC was attached.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'is_connected': 'is_connected',
        'mac_address': 'mac_address',
        'network_id': 'network_id',
    }

    def __init__(
        self, is_connected: bool = None, mac_address: str = None, network_id: str = None
    ) -> None:
        """Constructor for the VMNicBackupModel class."""

        # Initialize members of the class
        self.is_connected: bool = is_connected
        self.mac_address: str = mac_address
        self.network_id: str = network_id

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
        is_connected = dictionary.get('is_connected')
        mac_address = dictionary.get('mac_address')
        network_id = dictionary.get('network_id')
        # Return an object of this model
        return cls(is_connected, mac_address, network_id)
