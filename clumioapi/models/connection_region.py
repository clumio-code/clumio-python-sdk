#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ConnectionRegion')


class ConnectionRegion:
    """Implementation of the 'ConnectionRegion' model.

    Attributes:
        p_id:
            The ID of the aws region.
        is_data_plane_region:
            Boolean that notes which regions can be designated as targets
        name:
            Name is a user friendly name of the AWS region.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_id': 'id',
        'is_data_plane_region': 'is_data_plane_region',
        'name': 'name',
    }

    def __init__(self, p_id: str, is_data_plane_region: bool, name: str) -> None:
        """Constructor for the ConnectionRegion class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.is_data_plane_region: bool = is_data_plane_region
        self.name: str = name

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        # Extract variables from the dictionary
        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_data_plane_region']
        val_is_data_plane_region = val

        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_is_data_plane_region,  # type: ignore
            val_name,  # type: ignore
        )
