#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link, hateoas_self_link

T = TypeVar('T', bound='ManagementGroupLinks')


class ManagementGroupLinks:
    """Implementation of the 'ManagementGroupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        list_management_subgroups:
            A resource-specific HATEOAS link.
        update_management_group:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'list_management_subgroups': 'list-management-subgroups',
        'update_management_group': 'update-management-group',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        list_management_subgroups: hateoas_link.HateoasLink = None,
        update_management_group: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the ManagementGroupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.list_management_subgroups: hateoas_link.HateoasLink = list_management_subgroups
        self.update_management_group: hateoas_link.HateoasLink = update_management_group

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

        key = 'list-management-subgroups'
        list_management_subgroups = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'update-management-group'
        update_management_group = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, list_management_subgroups, update_management_group)
