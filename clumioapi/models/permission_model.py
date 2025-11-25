#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='PermissionModel')


@dataclasses.dataclass
class PermissionModel:
    """Implementation of the 'PermissionModel' model.

    Attributes:
        Description:
            Description of the permission.

        Id:
            The clumio-assigned id of the permission.

        Name:
            Name of the permission.
            the following table lists the supported permissions for a role:

            +----------------------------------------------------+-------------------------+
            |                  permission name                   | full/partial applicable |
            +====================================================+=========================+
            | policy management                                  | yes                     |
            +----------------------------------------------------+-------------------------+
            | data source management                             | yes                     |
            +----------------------------------------------------+-------------------------+
            | perform backup (scheduled or on-demand)            | yes                     |
            +----------------------------------------------------+-------------------------+
            | regular restore                                    | no                      |
            +----------------------------------------------------+-------------------------+
            | redirected granular restore (things like grr &     | yes                     |
            | content download)                                  |                         |
            +----------------------------------------------------+-------------------------+
            | dashboards & reports                               | yes                     |
            +----------------------------------------------------+-------------------------+
            | some admin functions (user mgmt, sso/mfa, ip       | no                      |
            | allow, password expiry, ou, kms)                   |                         |
            +----------------------------------------------------+-------------------------+
            | other admin functions (api tokens, tasks, alerts   | yes                     |
            | and audit logs)                                    |                         |
            +----------------------------------------------------+-------------------------+

    """

    Description: str | None = None
    Id: str | None = None
    Name: str | None = None

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_description,
            val_id,
            val_name,
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
