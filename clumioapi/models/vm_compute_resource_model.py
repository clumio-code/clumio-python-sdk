#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMComputeResourceModel')


class VMComputeResourceModel:
    """Implementation of the 'VMComputeResourceModel' model.

    The compute resource from which the VM draws. If the VM is deleted, then
    `compute_resource.id` has a value of `null`.

    Attributes:
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
        name:
            The VMware-assigned name of the compute resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id', 'name': 'name'}

    def __init__(self, id: str = None, name: str = None) -> None:
        """Constructor for the VMComputeResourceModel class."""

        # Initialize members of the class
        self.id: str = id
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
        name = dictionary.get('name')
        # Return an object of this model
        return cls(id, name)
