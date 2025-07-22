#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import task_with_e_tag as task_with_e_tag_

T = TypeVar('T', bound='TaskListEmbedded')


class TaskListEmbedded:
    """Implementation of the 'TaskListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(self, items: Sequence[task_with_e_tag_.TaskWithETag]) -> None:
        """Constructor for the TaskListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[task_with_e_tag_.TaskWithETag] = items

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

        # Extract variables from the dictionary
        val = dictionary['items']

        val_items = None
        if val:
            val_items = list()
            for value in val:
                val_items.append(task_with_e_tag_.TaskWithETag.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_items,  # type: ignore
        )
