#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PermissionModel')


class PermissionModel:
    """Implementation of the 'PermissionModel' model.

    Attributes:
        description:
            Description of the permission.
        id:
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
    _names = {'description': 'description', 'id': 'id', 'name': 'name'}

    def __init__(self, description: str = None, id: str = None, name: str = None) -> None:
        """Constructor for the PermissionModel class."""

        # Initialize members of the class
        self.description: str = description
        self.id: str = id
        self.name: str = name

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
        description = dictionary.get('description')
        id = dictionary.get('id')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(description, id, name)
