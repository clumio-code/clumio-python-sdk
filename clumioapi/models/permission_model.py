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

    def __init__(self, description: str, p_id: str, name: str) -> None:
        """Constructor for the PermissionModel class."""

        # Initialize members of the class
        self.description: str = description
        self.p_id: str = p_id
        self.name: str = name

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
        val = dictionary['description']
        val_description = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
        )
