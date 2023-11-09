#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link
from clumioapi.models import read_task_hateoas_link

T = TypeVar('T', bound='RestoreObjectsLinks')


class RestoreObjectsLinks:
    """Implementation of the 'RestoreObjectsLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_task:
            A HATEOAS link to the task associated with this resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_self': '_self', 'read_task': 'read-task'}

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_task: read_task_hateoas_link.ReadTaskHateoasLink = None,
    ) -> None:
        """Constructor for the RestoreObjectsLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_task: read_task_hateoas_link.ReadTaskHateoasLink = read_task

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

        key = 'read-task'
        read_task = (
            read_task_hateoas_link.ReadTaskHateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_task)
