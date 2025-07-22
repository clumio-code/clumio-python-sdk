#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AssetGroupFilter')


class AssetGroupFilter:
    """Implementation of the 'AssetGroupFilter' model.

    The asset groups to be filtered.

    Attributes:
        p_id:
            The id of asset group.
        region:
            The region of asset group. For example, `us-west-2`.
            This is supported for AWS asset groups only.
        p_type:
            The type of asset group.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_id': 'id', 'region': 'region', 'p_type': 'type'}

    def __init__(self, p_id: str, region: str, p_type: str) -> None:
        """Constructor for the AssetGroupFilter class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.region: str = region
        self.p_type: str = p_type

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

        val = dictionary['region']
        val_region = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_region,  # type: ignore
            val_p_type,  # type: ignore
        )
