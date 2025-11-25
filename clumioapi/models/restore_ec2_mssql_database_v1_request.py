#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_mssql_restore_source as ec2_mssql_restore_source_
from clumioapi.models import ec2_mssql_restore_target as ec2_mssql_restore_target_
import requests

T = TypeVar('T', bound='RestoreEc2MssqlDatabaseV1Request')


@dataclasses.dataclass
class RestoreEc2MssqlDatabaseV1Request:
    """Implementation of the 'RestoreEc2MssqlDatabaseV1Request' model.

    Attributes:
        Source:
            The ec2 mssql database backup to be restored. only one of `backup` or `pitr`
            should be set.
            `pitr` a database backup at a specific point in time to be restored.

        Target:
            The configuration of the ec2 mssql database to which the data has to be
            restored.

    """

    Source: ec2_mssql_restore_source_.EC2MSSQLRestoreSource | None = None
    Target: ec2_mssql_restore_target_.EC2MSSQLRestoreTarget | None = None

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
        val = dictionary.get('source', None)
        val_source = ec2_mssql_restore_source_.EC2MSSQLRestoreSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = ec2_mssql_restore_target_.EC2MSSQLRestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
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
