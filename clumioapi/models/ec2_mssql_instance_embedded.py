#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLInstanceEmbedded')


class EC2MSSQLInstanceEmbedded:
    """Implementation of the 'EC2MSSQLInstanceEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_ec2_mssql_instance_stats:
            Stats pertaining to the EC2 MSSQL Instance.
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'get_ec2_mssql_instance_stats': 'get-ec2-mssql-instance-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self, get_ec2_mssql_instance_stats: object = None, read_policy_definition: object = None
    ) -> None:
        """Constructor for the EC2MSSQLInstanceEmbedded class."""

        # Initialize members of the class
        self.get_ec2_mssql_instance_stats: object = get_ec2_mssql_instance_stats
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
        get_ec2_mssql_instance_stats = dictionary.get('get-ec2-mssql-instance-stats')
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(get_ec2_mssql_instance_stats, read_policy_definition)
