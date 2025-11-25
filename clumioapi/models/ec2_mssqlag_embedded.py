#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='EC2MSSQLAGEmbedded')


@dataclasses.dataclass
class EC2MSSQLAGEmbedded:
    """Implementation of the 'EC2MSSQLAGEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        GetMssqlEc2AvailabilityGroupBackupStatusStats:
            Availability group level backup status stats.

        GetMssqlEc2AvailabilityGroupStats:
            Availability group level protection stats.

        ReadPolicyDefinition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. unprotected resources will not have
            an associated policy.

    """

    GetMssqlEc2AvailabilityGroupBackupStatusStats: object | None = None
    GetMssqlEc2AvailabilityGroupStats: object | None = None
    ReadPolicyDefinition: object | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('get-mssql-ec2-availability-group-backup-status-stats', None)
        val_get_mssql_ec2_availability_group_backup_status_stats = val

        val = dictionary.get('get-mssql-ec2-availability-group-stats', None)
        val_get_mssql_ec2_availability_group_stats = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_get_mssql_ec2_availability_group_backup_status_stats,
            val_get_mssql_ec2_availability_group_stats,
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
