#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RoleForOrganizationalUnits')


class RoleForOrganizationalUnits:
    """Implementation of the 'RoleForOrganizationalUnits' model.

    The organizational units assigned to the user, with the specified role.

    Attributes:
        organizational_unit_ids:
            The Clumio-assigned IDs of the organizational units assigned to the user.
            Use the [GET /organizational-units](#operation/list-organizational-units)
            endpoint to fetch valid values.
        role_id:
            The Clumio-assigned ID of the role assigned to the user.
            Use the [GET /roles](#operation/list-roles) endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names = {'organizational_unit_ids': 'organizational_unit_ids', 'role_id': 'role_id'}

    def __init__(self, organizational_unit_ids: Sequence[str] = None, role_id: str = None) -> None:
        """Constructor for the RoleForOrganizationalUnits class."""

        # Initialize members of the class
        self.organizational_unit_ids: Sequence[str] = organizational_unit_ids
        self.role_id: str = role_id

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
        organizational_unit_ids = dictionary.get('organizational_unit_ids')
        role_id = dictionary.get('role_id')
        # Return an object of this model
        return cls(organizational_unit_ids, role_id)
