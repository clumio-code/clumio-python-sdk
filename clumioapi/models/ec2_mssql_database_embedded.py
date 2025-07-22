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
    _names: dict[str, str] = {
        'get_ec2_mssql_failover_clusters_hosts_info': 'get-ec2-mssql-failover-clusters-hosts-info',
        'read_aws_ec2_instance': 'read-aws-ec2-instance',
        'read_aws_environment': 'read-aws-environment',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        get_ec2_mssql_failover_clusters_hosts_info: object,
        read_aws_ec2_instance: object,
        read_aws_environment: object,
        read_policy_definition: object,
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
        val = dictionary['get-ec2-mssql-failover-clusters-hosts-info']
        val_get_ec2_mssql_failover_clusters_hosts_info = val

        val = dictionary['read-aws-ec2-instance']
        val_read_aws_ec2_instance = val

        val = dictionary['read-aws-environment']
        val_read_aws_environment = val

        val = dictionary['read-policy-definition']
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_ec2_mssql_failover_clusters_hosts_info,  # type: ignore
            val_read_aws_ec2_instance,  # type: ignore
            val_read_aws_environment,  # type: ignore
            val_read_policy_definition,  # type: ignore
        )
