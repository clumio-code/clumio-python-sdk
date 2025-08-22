#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AddProtectionGroupInstantAccessEndpointRoleV1Request')


class AddProtectionGroupInstantAccessEndpointRoleV1Request:
    """Implementation of the 'AddProtectionGroupInstantAccessEndpointRoleV1Request' model.

    Attributes:
        is_allow_external_account:
            Allow the addition of a role from an external account. This requires a feature
            flag to be enabled, contact support@clumio.com.
        role_alias:
            Descriptive alias of the IAM role.
        role_arn:
            ARN of the IAM role to allow access the endpoint. The role must be accessible
            from AWS account
            registered with Clumio.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'is_allow_external_account': 'is_allow_external_account',
        'role_alias': 'role_alias',
        'role_arn': 'role_arn',
    }

    def __init__(
        self,
        is_allow_external_account: bool | None = None,
        role_alias: str | None = None,
        role_arn: str | None = None,
    ) -> None:
        """Constructor for the AddProtectionGroupInstantAccessEndpointRoleV1Request class."""

        # Initialize members of the class
        self.is_allow_external_account: bool | None = is_allow_external_account
        self.role_alias: str | None = role_alias
        self.role_arn: str | None = role_arn

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
        val = dictionary.get('is_allow_external_account', None)
        val_is_allow_external_account = val

        val = dictionary.get('role_alias', None)
        val_role_alias = val

        val = dictionary.get('role_arn', None)
        val_role_arn = val

        # Return an object of this model
        return cls(
            val_is_allow_external_account,
            val_role_alias,
            val_role_arn,
        )
