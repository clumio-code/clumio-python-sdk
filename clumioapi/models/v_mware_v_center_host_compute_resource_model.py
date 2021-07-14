#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMwareVCenterHostComputeResourceModel')


class VMwareVCenterHostComputeResourceModel:
    """Implementation of the 'VMwareVCenterHostComputeResourceModel' model.

    The VMware compute resource representing the host.

    Attributes:
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'id': 'id'}

    def __init__(self, id: str = None) -> None:
        """Constructor for the VMwareVCenterHostComputeResourceModel class."""

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
