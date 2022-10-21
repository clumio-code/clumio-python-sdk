#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link, hateoas_self_link

T = TypeVar('T', bound='OrganizationalUnitLinks')


class OrganizationalUnitLinks:
    """Implementation of the 'OrganizationalUnitLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_organizational_unit:
            A resource-specific HATEOAS link.
        patch_organizational_unit:
            A resource-specific HATEOAS link.
        read_task:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'delete_organizational_unit': 'delete-organizational-unit',
        'patch_organizational_unit': 'patch-organizational-unit',
        'read_task': 'read-task',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        delete_organizational_unit: hateoas_link.HateoasLink = None,
        patch_organizational_unit: hateoas_link.HateoasLink = None,
        read_task: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the OrganizationalUnitLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.delete_organizational_unit: hateoas_link.HateoasLink = delete_organizational_unit
        self.patch_organizational_unit: hateoas_link.HateoasLink = patch_organizational_unit
        self.read_task: hateoas_link.HateoasLink = read_task

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'delete-organizational-unit'
        delete_organizational_unit = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'patch-organizational-unit'
        patch_organizational_unit = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-task'
        read_task = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, delete_organizational_unit, patch_organizational_unit, read_task)
