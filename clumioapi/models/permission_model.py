#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PermissionModel')


class PermissionModel:
    """Implementation of the 'PermissionModel' model.

    Attributes:
        description:
            Description of the permission.
        p_id:
            The Clumio-assigned ID of the permission.
        name:
            Name of the permission.
            The following table lists the supported permissions for a role:

            +----------------------------------------------------+-------------------------+
            |                  Permission Name                   | Full/Partial Applicable |
            +====================================================+=========================+
            | Policy Management                                  | Yes                     |
            +----------------------------------------------------+-------------------------+
            | Data Source Management                             | Yes                     |
            +----------------------------------------------------+-------------------------+
            | Perform Backup (Scheduled or On-demand)            | Yes                     |
            +----------------------------------------------------+-------------------------+
            | Regular Restore                                    | No                      |
            +----------------------------------------------------+-------------------------+
            | Redirected Granular Restore (things like GRR &     | Yes                     |
            | content download)                                  |                         |
            +----------------------------------------------------+-------------------------+
            | Dashboards & Reports                               | Yes                     |
            +----------------------------------------------------+-------------------------+
            | Some Admin Functions (User mgmt, SSO/MFA, IP       | No                      |
            | Allow, Password expiry, OU, KMS)                   |                         |
            +----------------------------------------------------+-------------------------+
            | Other Admin Functions (API Tokens, Tasks, Alerts   | Yes                     |
            | and Audit Logs)                                    |                         |
            +----------------------------------------------------+-------------------------+
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'description': 'description', 'p_id': 'id', 'name': 'name'}

    def __init__(
        self, description: str | None = None, p_id: str | None = None, name: str | None = None
    ) -> None:
        """Constructor for the PermissionModel class."""

        # Initialize members of the class
        self.description: str | None = description
        self.p_id: str | None = p_id
        self.name: str | None = name

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_description,
            val_p_id,
            val_name,
        )
