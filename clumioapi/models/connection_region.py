#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ConnectionRegion')


class ConnectionRegion:
    """Implementation of the 'ConnectionRegion' model.

    Attributes:
        p_id:
            The Clumio-assigned ID of the connection.
        is_data_plane_region:
            Boolean that notes which regions can be designated as targets
        name:
            Name is a user friendly name of the AWS region.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'is_data_plane_region': 'is_data_plane_region', 'name': 'name'}

    def __init__(
        self, p_id: str = None, is_data_plane_region: bool = None, name: str = None
    ) -> None:
        """Constructor for the ConnectionRegion class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.is_data_plane_region: bool = is_data_plane_region
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
        is_data_plane_region = dictionary.get('is_data_plane_region')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(p_id, is_data_plane_region, name)
