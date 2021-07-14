#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlInstanceEmbedded')


class MssqlInstanceEmbedded:
    """Implementation of the 'MssqlInstanceEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_mssql_instance_stats:

        read_management_group:
            Embedded types
        read_management_subgroup:
            Embedded types
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'get_mssql_instance_stats': 'get-mssql-instance-stats',
        'read_management_group': 'read-management-group',
        'read_management_subgroup': 'read-management-subgroup',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_mssql_instance_stats: object = None,
        read_management_group: object = None,
        read_management_subgroup: object = None,
        read_policy_definition: object = None,
    ) -> None:
        """Constructor for the MssqlInstanceEmbedded class."""

        # Initialize members of the class
        self.get_mssql_instance_stats: object = get_mssql_instance_stats
        self.read_management_group: object = read_management_group
        self.read_management_subgroup: object = read_management_subgroup
        self.read_policy_definition: object = read_policy_definition

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
        get_mssql_instance_stats = dictionary.get('get-mssql-instance-stats')
        read_management_group = dictionary.get('read-management-group')
        read_management_subgroup = dictionary.get('read-management-subgroup')
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(
            get_mssql_instance_stats,
            read_management_group,
            read_management_subgroup,
            read_policy_definition,
        )
