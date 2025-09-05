#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AutoUserProvisioningRuleEmbedded')


class AutoUserProvisioningRuleEmbedded:
    """Implementation of the 'AutoUserProvisioningRuleEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_organizational_unit:
            Embeds the associated organizational units for the OU UUIDs in the response
            if requested using the `embed` query parameter.
        read_role:
            Embeds the associated role for the role UUID in the response if requested using
            the `embed` query parameter.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_organizational_unit': 'read-organizational-unit',
        'read_role': 'read-role',
    }

    def __init__(
        self, read_organizational_unit: object | None = None, read_role: object | None = None
    ) -> None:
        """Constructor for the AutoUserProvisioningRuleEmbedded class."""

        # Initialize members of the class
        self.read_organizational_unit: object | None = read_organizational_unit
        self.read_role: object | None = read_role

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
        val = dictionary.get('read-organizational-unit', None)
        val_read_organizational_unit = val

        val = dictionary.get('read-role', None)
        val_read_role = val

        # Return an object of this model
        return cls(
            val_read_organizational_unit,
            val_read_role,
        )
