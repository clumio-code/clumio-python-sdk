#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMHostModel')


class VMHostModel:
    """Implementation of the 'VMHostModel' model.

    The host on which the VM resides. If the VM is deleted, then `host.id` and
    `host.is_standalone` have values of `null`. The `host.name` field may also have
    a value of `null`.

    Attributes:
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the host.
        is_standalone:
            Determines whether the host is a standalone host. If `true`, the host is a
            standalone host.
        name:
            The VMware-assigned name of the host.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id', 'is_standalone': 'is_standalone', 'name': 'name'}

    def __init__(self, id: str = None, is_standalone: bool = None, name: str = None) -> None:
        """Constructor for the VMHostModel class."""

        # Initialize members of the class
        self.id: str = id
        self.is_standalone: bool = is_standalone
        self.name: str = name

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
        is_standalone = dictionary.get('is_standalone')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(id, is_standalone, name)
