#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AlertPrimaryEntity')


class AlertPrimaryEntity:
    """Implementation of the 'AlertPrimaryEntity' model.

    The primary object associated with or affected by the alert. Examples of primary
    entities include "aws_connection", "aws_ebs_volume" and "vmware_vm".

    Attributes:
        p_id:
            A system-generated ID assigned to this entity.
        p_type:
            Type is mostly an asset type or the type of Entity. Some examples are
            "restored_file", "vmware_vm",  etc.
        value:
            A system-generated value assigned to the entity. For example, if the primary
            entity type is "vmware_vm" for a virtual machine, then the value is the name of
            the VM.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'p_type': 'type', 'value': 'value'}

    def __init__(self, p_id: str = None, p_type: str = None, value: str = None) -> None:
        """Constructor for the AlertPrimaryEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.p_type: str = p_type
        self.value: str = value

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
        p_id = dictionary.get('id')
        p_type = dictionary.get('type')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(p_id, p_type, value)
