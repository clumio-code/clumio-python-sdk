#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protection_info, tag2_embedded, tag2_links, tag_parent_category_model

T = TypeVar('T', bound='Tag2')


class Tag2:
    """Implementation of the 'Tag2' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        category:
            The tag category associated with the tag.
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag.
        name:
            The VMware-assigned name of the tag.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of this tag. Refer to the Protection Status table for a
            complete list of protection statuses.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'category': 'category',
        'id': 'id',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
    }

    def __init__(
        self,
        embedded: tag2_embedded.Tag2Embedded = None,
        links: tag2_links.Tag2Links = None,
        category: tag_parent_category_model.TagParentCategoryModel = None,
        id: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
    ) -> None:
        """Constructor for the Tag2 class."""

        # Initialize members of the class
        self.embedded: tag2_embedded.Tag2Embedded = embedded
        self.links: tag2_links.Tag2Links = links
        self.category: tag_parent_category_model.TagParentCategoryModel = category
        self.id: str = id
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status

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
        key = '_embedded'
        embedded = (
            tag2_embedded.Tag2Embedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            tag2_links.Tag2Links.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'category'
        category = (
            tag_parent_category_model.TagParentCategoryModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        id = dictionary.get('id')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        # Return an object of this model
        return cls(
            embedded,
            links,
            category,
            id,
            name,
            organizational_unit_id,
            p_protection_info,
            protection_status,
        )
