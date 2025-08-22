#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import consolidated_alert_with_e_tag as consolidated_alert_with_e_tag_

T = TypeVar('T', bound='ConsolidatedAlertListEmbedded')


class ConsolidatedAlertListEmbedded:
    """Implementation of the 'ConsolidatedAlertListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(
        self,
        items: Sequence[consolidated_alert_with_e_tag_.ConsolidatedAlertWithETag] | None = None,
    ) -> None:
        """Constructor for the ConsolidatedAlertListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[consolidated_alert_with_e_tag_.ConsolidatedAlertWithETag] | None = (
            items
        )

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
        val = dictionary.get('items', None)

        val_items = None
        if val:
            val_items = list()
            for value in val:
                val_items.append(
                    consolidated_alert_with_e_tag_.ConsolidatedAlertWithETag.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_items,
        )
