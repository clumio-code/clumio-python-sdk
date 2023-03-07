#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMwareResourcePoolComputeResourceModel')


class VMwareResourcePoolComputeResourceModel:
    """Implementation of the 'VMwareResourcePoolComputeResourceModel' model.

    The compute resource that the resource pool comprises.

    Attributes:
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id'}

    def __init__(self, p_id: str = None) -> None:
        """Constructor for the VMwareResourcePoolComputeResourceModel class."""

        # Initialize members of the class
        self.p_id: str = p_id

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
        # Return an object of this model
        return cls(p_id)
