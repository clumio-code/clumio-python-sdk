#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='EC2MSSQLDatabaseEmbedded')


@dataclasses.dataclass
class EC2MSSQLDatabaseEmbedded:
    """Implementation of the 'EC2MSSQLDatabaseEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        GetEc2MssqlFailoverClustersHostsInfo:
            Embed information about the hosts part of fci databases.

        ReadAwsEc2Instance:
            Aws inventory ec2 instance embed.

        ReadAwsEnvironment:
            Embed information for aws environment details.

        ReadPolicyDefinition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. unprotected resources will not have
            an associated policy.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'GetEc2MssqlFailoverClustersHostsInfo': 'get-ec2-mssql-failover-clusters-hosts-info',
        'ReadAwsEc2Instance': 'read-aws-ec2-instance',
        'ReadAwsEnvironment': 'read-aws-environment',
        'ReadPolicyDefinition': 'read-policy-definition',
    }

    GetEc2MssqlFailoverClustersHostsInfo: object | None = None
    ReadAwsEc2Instance: object | None = None
    ReadAwsEnvironment: object | None = None
    ReadPolicyDefinition: object | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('get-ec2-mssql-failover-clusters-hosts-info', None)
        val_get_ec2_mssql_failover_clusters_hosts_info = val

        val = dictionary.get('read-aws-ec2-instance', None)
        val_read_aws_ec2_instance = val

        val = dictionary.get('read-aws-environment', None)
        val_read_aws_environment = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_ec2_mssql_failover_clusters_hosts_info,
            val_read_aws_ec2_instance,
            val_read_aws_environment,
            val_read_policy_definition,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
