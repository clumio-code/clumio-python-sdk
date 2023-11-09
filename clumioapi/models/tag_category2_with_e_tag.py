#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import tag_category2_links

T = TypeVar('T', bound='TagCategory2WithETag')


class TagCategory2WithETag:
    """Implementation of the 'TagCategory2WithETag' model.

    TagCategory2WithETag to support etag string to be calculated

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource
        description:
            A description of the tag category.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the tag category.
        name:
            The VMware-assigned name of the tag category.
        number_of_tags:
            The number of tags in the tag category.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag
            category.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'description': 'description',
        'p_id': 'id',
        'name': 'name',
        'number_of_tags': 'number_of_tags',
        'organizational_unit_id': 'organizational_unit_id',
    }

    def __init__(
        self,
        etag: str = None,
        links: tag_category2_links.TagCategory2Links = None,
        description: str = None,
        p_id: str = None,
        name: str = None,
        number_of_tags: int = None,
        organizational_unit_id: str = None,
    ) -> None:
        """Constructor for the TagCategory2WithETag class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: tag_category2_links.TagCategory2Links = links
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name
        self.number_of_tags: int = number_of_tags
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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            tag_category2_links.TagCategory2Links.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        description = dictionary.get('description')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        number_of_tags = dictionary.get('number_of_tags')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        # Return an object of this model
        return cls(etag, links, description, p_id, name, number_of_tags, organizational_unit_id)
