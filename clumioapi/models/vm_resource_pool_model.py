#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMResourcePoolModel')


class VMResourcePoolModel:
    """Implementation of the 'VMResourcePoolModel' model.

    The resource pool from which the VM draws. If the VM is deleted, then
    `resource_pool.id` and `resource_pool.is_root` have values of `null`.

    Attributes:
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool.
        is_root:
            Determines whether the resource pool is the default, hidden resource pool.
        name:
            The VMware-assigned name of the resource pool.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'is_root': 'is_root', 'name': 'name'}

    def __init__(self, p_id: str = None, is_root: bool = None, name: str = None) -> None:
        """Constructor for the VMResourcePoolModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.is_root: bool = is_root
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
        p_id = dictionary.get('id')
        is_root = dictionary.get('is_root')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(p_id, is_root, name)
