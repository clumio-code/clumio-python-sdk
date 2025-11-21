#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='RoleForOrganizationalUnits')


@dataclasses.dataclass
class RoleForOrganizationalUnits:
    """Implementation of the 'RoleForOrganizationalUnits' model.

    The organizational units assigned to the user, with the specified role.

    Attributes:
        OrganizationalUnitIds:
            The clumio-assigned ids of the organizational units assigned to the user.
            use the [get /organizational-units](#operation/list-organizational-units)
            endpoint to fetch
            valid values.

        RoleId:
            The clumio-assigned id of the role assigned to the user.
            use the [get /roles](#operation/list-roles) endpoint to fetch valid values.

    """

    OrganizationalUnitIds: Sequence[str] | None = None
    RoleId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('organizational_unit_ids', None)
        val_organizational_unit_ids = val

        val = dictionary.get('role_id', None)
        val_role_id = val

        # Return an object of this model
        return cls(
            val_organizational_unit_ids,
            val_role_id,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
