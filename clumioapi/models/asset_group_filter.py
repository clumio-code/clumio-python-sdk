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

    def __init__(
        self, p_id: str | None = None, region: str | None = None, p_type: str | None = None
    ) -> None:
        """Constructor for the AssetGroupFilter class."""

        # Initialize members of the class
        self.p_id: str | None = p_id
        self.region: str | None = region
        self.p_type: str | None = p_type

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

        val = dictionary.get('region', None)
        val_region = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_p_id,
            val_region,
            val_p_type,
        )
