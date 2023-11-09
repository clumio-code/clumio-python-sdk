#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='VMTagWithCategoryModel')


class VMTagWithCategoryModel:
    """Implementation of the 'VMTagWithCategoryModel' model.

    VMTagWithCategoryModelA tag associated with the VM.

    Attributes:
        category_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
        category_name:
            The VMware-assigned name of the tag category.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
        name:
            The VMware-assigned name of the tag.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'category_id': 'category_id',
        'category_name': 'category_name',
        'p_id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
    }

    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
        p_id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
    ) -> None:
        """Constructor for the VMTagWithCategoryModel class."""

        # Initialize members of the class
        self.category_id: str = category_id
        self.category_name: str = category_name
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
        category_id = dictionary.get('category_id')
        category_name = dictionary.get('category_name')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        # Return an object of this model
        return cls(category_id, category_name, p_id, name, organizational_unit_id)
