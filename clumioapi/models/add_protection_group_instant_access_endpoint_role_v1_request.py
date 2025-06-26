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
    _names = {
        'is_allow_external_account': 'is_allow_external_account',
        'role_alias': 'role_alias',
        'role_arn': 'role_arn',
    }

    def __init__(
        self, is_allow_external_account: bool = None, role_alias: str = None, role_arn: str = None
    ) -> None:
        """Constructor for the AddProtectionGroupInstantAccessEndpointRoleV1Request class."""

        # Initialize members of the class
        self.is_allow_external_account: bool = is_allow_external_account
        self.role_alias: str = role_alias
        self.role_arn: str = role_arn

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
        is_allow_external_account = dictionary.get('is_allow_external_account')
        role_alias = dictionary.get('role_alias')
        role_arn = dictionary.get('role_arn')
        # Return an object of this model
        return cls(is_allow_external_account, role_alias, role_arn)
