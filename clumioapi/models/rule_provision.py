#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RuleProvision')


class RuleProvision:
    """Implementation of the 'RuleProvision' model.

    Specifies the role and the organizational units to be assigned to the user
    subject to the rule criteria.

    Attributes:
        organizational_unit_ids:
            The Clumio-assigned IDs of the organizational units to be assigned to the user.
            Use the [GET /organizational-units](#operation/list-organizational-units)
            endpoint to fetch valid values.
        role_id:
            The Clumio-assigned ID of the role to be assigned to the user.
            Use the [GET /roles](#operation/list-roles) endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'organizational_unit_ids': 'organizational_unit_ids',
        'role_id': 'role_id',
    }

    def __init__(self, organizational_unit_ids: Sequence[str], role_id: str) -> None:
        """Constructor for the RuleProvision class."""

        # Initialize members of the class
        self.organizational_unit_ids: Sequence[str] = organizational_unit_ids
        self.role_id: str = role_id

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
        val = dictionary['organizational_unit_ids']
        val_organizational_unit_ids = val

        val = dictionary['role_id']
        val_role_id = val

        # Return an object of this model
        return cls(
            val_organizational_unit_ids,  # type: ignore
            val_role_id,  # type: ignore
        )
