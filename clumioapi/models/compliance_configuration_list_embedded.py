#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_configuration as compliance_configuration_

T = TypeVar('T', bound='ComplianceConfigurationListEmbedded')


class ComplianceConfigurationListEmbedded:
    """Implementation of the 'ComplianceConfigurationListEmbedded' model.

    An array of embedded resources related to this resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'items': 'items'}

    def __init__(
        self, items: Sequence[compliance_configuration_.ComplianceConfiguration] | None = None
    ) -> None:
        """Constructor for the ComplianceConfigurationListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[compliance_configuration_.ComplianceConfiguration] | None = items

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
                    compliance_configuration_.ComplianceConfiguration.from_dictionary(value)
                )

        # Return an object of this model
        return cls(
            val_items,
        )
