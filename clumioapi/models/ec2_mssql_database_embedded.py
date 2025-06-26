#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLDatabaseEmbedded')


class EC2MSSQLDatabaseEmbedded:
    """Implementation of the 'EC2MSSQLDatabaseEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        get_ec2_mssql_failover_clusters_hosts_info:
            Embed information about the Hosts part of FCI databases
        read_aws_ec2_instance:
            AWS inventory EC2 Instance embed
        read_aws_environment:
            Embed information for AWS Environment details
        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'get_ec2_mssql_failover_clusters_hosts_info': 'get-ec2-mssql-failover-clusters-hosts-info',
        'read_aws_ec2_instance': 'read-aws-ec2-instance',
        'read_aws_environment': 'read-aws-environment',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_ec2_mssql_failover_clusters_hosts_info: object = None,
        read_aws_ec2_instance: object = None,
        read_aws_environment: object = None,
        read_policy_definition: object = None,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseEmbedded class."""

        # Initialize members of the class
        self.get_ec2_mssql_failover_clusters_hosts_info: object = (
            get_ec2_mssql_failover_clusters_hosts_info
        )
        self.read_aws_ec2_instance: object = read_aws_ec2_instance
        self.read_aws_environment: object = read_aws_environment
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
        get_ec2_mssql_failover_clusters_hosts_info = dictionary.get(
            'get-ec2-mssql-failover-clusters-hosts-info'
        )
        read_aws_ec2_instance = dictionary.get('read-aws-ec2-instance')
        read_aws_environment = dictionary.get('read-aws-environment')
        read_policy_definition = dictionary.get('read-policy-definition')
        # Return an object of this model
        return cls(
            get_ec2_mssql_failover_clusters_hosts_info,
            read_aws_ec2_instance,
            read_aws_environment,
            read_policy_definition,
        )
