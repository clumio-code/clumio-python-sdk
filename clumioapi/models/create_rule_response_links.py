#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import read_task_hateoas_link as read_task_hateoas_link_

T = TypeVar('T', bound='CreateRuleResponseLinks')


class CreateRuleResponseLinks:
    """Implementation of the 'CreateRuleResponseLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_task:
            A HATEOAS link to the task associated with this resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_self': '_self', 'read_task': 'read-task'}

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        read_task: read_task_hateoas_link_.ReadTaskHateoasLink | None = None,
    ) -> None:
        """Constructor for the CreateRuleResponseLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.read_task: read_task_hateoas_link_.ReadTaskHateoasLink | None = read_task

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
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-task', None)
        val_read_task = read_task_hateoas_link_.ReadTaskHateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_read_task,
        )
