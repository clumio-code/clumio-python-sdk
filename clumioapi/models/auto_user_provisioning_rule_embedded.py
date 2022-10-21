#
# Copyright 2021. Clumio, Inc.
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
    _names = { 
        'read_organizational_unit': 'read-organizational-unit',
        'read_role': 'read-role'
    }

    def __init__(self,
        read_organizational_unit:  = None,
        read_role: None = None
    ) -> None:
        """Constructor for the AutoUserProvisioningRuleEmbedded class."""

        # Initialize members of the class
        self.read_organizational_unit: object = read_organizational_unit
        self.read_role: object = read_role

    @classmethod
    def from_dictionary(
        cls: Type,
        dictionary: Mapping[str, Any]
    ) -> Optional[T]:
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
        read_organizational_unit = dictionary.get('read-organizational-unit')
        read_role = dictionary.get('read-role')
        # Return an object of this model
        return cls(
            read_organizational_unit,
            read_role)
