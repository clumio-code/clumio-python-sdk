#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AlertEmbedded')


class AlertEmbedded:
    """Implementation of the 'AlertEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_consolidated_alert:
            Embeds the associated consolidated alert in the response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'read_consolidated_alert': 'read-consolidated-alert'}

    def __init__(self, read_consolidated_alert: object | None = None) -> None:
        """Constructor for the AlertEmbedded class."""

        # Initialize members of the class
        self.read_consolidated_alert: object | None = read_consolidated_alert

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
        val = dictionary.get('read-consolidated-alert', None)
        val_read_consolidated_alert = val

        # Return an object of this model
        return cls(
            val_read_consolidated_alert,
        )
