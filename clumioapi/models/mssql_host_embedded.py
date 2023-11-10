#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlHostEmbedded')


class MssqlHostEmbedded:
    """Implementation of the 'MssqlHostEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_mssql_host_stats:
            host level stats
        read_management_group:
            Embeds details about the management group if requested using the `embed` query.
        read_management_subgroup:
            Embeds details about the management subgroup if requested using the `embed`
            query.
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'get_mssql_host_stats': 'get-mssql-host-stats',
        'read_management_group': 'read-management-group',
        'read_management_subgroup': 'read-management-subgroup',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_mssql_host_stats: object = None,
        read_management_group: object = None,
        read_management_subgroup: object = None,
        read_policy_definition: object = None,
    ) -> None:
        """Constructor for the MssqlHostEmbedded class."""

        # Initialize members of the class
        self.get_mssql_host_stats: object = get_mssql_host_stats
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
        get_mssql_host_stats = dictionary.get('get-mssql-host-stats')
        read_management_group = dictionary.get('read-management-group')
        read_management_subgroup = dictionary.get('read-management-subgroup')
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(
            get_mssql_host_stats,
            read_management_group,
            read_management_subgroup,
            read_policy_definition,
        )
