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

    def __init__(
        self,
        p_id: str | None = None,
        is_data_plane_region: bool | None = None,
        name: str | None = None,
    ) -> None:
        """Constructor for the ConnectionRegion class."""

        # Initialize members of the class
        self.p_id: str | None = p_id
        self.is_data_plane_region: bool | None = is_data_plane_region
        self.name: str | None = name

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_data_plane_region', None)
        val_is_data_plane_region = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_p_id,
            val_is_data_plane_region,
            val_name,
        )
