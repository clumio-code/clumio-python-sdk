#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='TagParentCategoryModel')


class TagParentCategoryModel:
    """Implementation of the 'TagParentCategoryModel' model.

    The tag category associated with the tag.

    Attributes:
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
        name:
            The VMware-assigned name of the tag category.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag
            category.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_id': 'id', 'name': 'name', 'organizational_unit_id': 'organizational_unit_id'}

    def __init__(
        self, p_id: str = None, name: str = None, organizational_unit_id: str = None
    ) -> None:
        """Constructor for the TagParentCategoryModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id

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
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        # Return an object of this model
        return cls(p_id, name, organizational_unit_id)
