#
# Copyright 2023. Clumio, Inc.
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
    _names = {'p_id': 'id', 'region': 'region', 'p_type': 'type'}

    def __init__(self, p_id: str = None, region: str = None, p_type: str = None) -> None:
        """Constructor for the AssetGroupFilter class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.region: str = region
        self.p_type: str = p_type

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
        region = dictionary.get('region')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(p_id, region, p_type)
