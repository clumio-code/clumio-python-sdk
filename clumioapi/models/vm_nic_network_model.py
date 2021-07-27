#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMNicNetworkModel')


class VMNicNetworkModel:
    """Implementation of the 'VMNicNetworkModel' model.

    The network associated with this NIC.

    Attributes:
        id:
            The VMware-assigned ID of this network.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id'}

    def __init__(self, id: str = None) -> None:
        """Constructor for the VMNicNetworkModel class."""

        # Initialize members of the class
        self.id: str = id

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
        id = dictionary.get('id')
        # Return an object of this model
        return cls(id)
