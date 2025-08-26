#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2MSSQLFCIEmbedded')


@dataclasses.dataclass
class EC2MSSQLFCIEmbedded:
    """Implementation of the 'EC2MSSQLFCIEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        GetEc2MssqlFailoverClusterBackupStatusStats:
            Fcibackupstatusstats contain information about the backup status of the databases in the cluster.

        GetEc2MssqlFailoverClusterHostsInfo:
            Connectedhostsinfo contains information about the hosts associated with the cluster.

        GetEc2MssqlFailoverClusterStats:
            Fcistats contain information about the compliant databases in the cluster.

        ReadPolicyDefinition:
            Embeds the associated policy of a protected resource in the response if requested using the `embed` query parameter. unprotected resources will not have an associated policy.

    """

    GetEc2MssqlFailoverClusterBackupStatusStats: object | None = None
    GetEc2MssqlFailoverClusterHostsInfo: object | None = None
    GetEc2MssqlFailoverClusterStats: object | None = None
    ReadPolicyDefinition: object | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('get-ec2-mssql-failover-cluster-backup-status-stats', None)
        val_get_ec2_mssql_failover_cluster_backup_status_stats = val

        val = dictionary.get('get-ec2-mssql-failover-cluster-hosts-info', None)
        val_get_ec2_mssql_failover_cluster_hosts_info = val

        val = dictionary.get('get-ec2-mssql-failover-cluster-stats', None)
        val_get_ec2_mssql_failover_cluster_stats = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_ec2_mssql_failover_cluster_backup_status_stats,
            val_get_ec2_mssql_failover_cluster_hosts_info,
            val_get_ec2_mssql_failover_cluster_stats,
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
