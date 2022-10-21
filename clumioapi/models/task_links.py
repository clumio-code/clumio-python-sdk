#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link, hateoas_self_link

T = TypeVar('T', bound='TaskLinks')


class TaskLinks:
    """Implementation of the 'TaskLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_organizational_unit:
            A resource-specific HATEOAS link.
        update_task:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_organizational_unit': 'read-organizational-unit',
        'update_task': 'update-task',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_organizational_unit: hateoas_link.HateoasLink = None,
        update_task: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the TaskLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_organizational_unit: hateoas_link.HateoasLink = read_organizational_unit
        self.update_task: hateoas_link.HateoasLink = update_task

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

        key = 'read-organizational-unit'
        read_organizational_unit = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'update-task'
        update_task = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_organizational_unit, update_task)
