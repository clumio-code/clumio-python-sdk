#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateProtectionGroupInstantAccessEndpointRoleV1Request')


class UpdateProtectionGroupInstantAccessEndpointRoleV1Request:
    """Implementation of the 'UpdateProtectionGroupInstantAccessEndpointRoleV1Request' model.

    Attributes:
        updated_role_alias:
            The updated descriptive alias of the IAM role. The current alias will be
            retained if
            empty updated_role_alias is passed.
        updated_role_arn:
            The updated ARN of the IAM role to allow access to the endpoint. The role must
            be
            accessible from an AWS account registered with Clumio. The current ARN will be
            retained
            if empty updated_role_arn is passed.
    """

    # Create a mapping from Model property names to API property names
    _names = {'updated_role_alias': 'updated_role_alias', 'updated_role_arn': 'updated_role_arn'}

    def __init__(self, updated_role_alias: str = None, updated_role_arn: str = None) -> None:
        """Constructor for the UpdateProtectionGroupInstantAccessEndpointRoleV1Request class."""

        # Initialize members of the class
        self.updated_role_alias: str = updated_role_alias
        self.updated_role_arn: str = updated_role_arn

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
        updated_role_alias = dictionary.get('updated_role_alias')
        updated_role_arn = dictionary.get('updated_role_arn')
        # Return an object of this model
        return cls(updated_role_alias, updated_role_arn)
