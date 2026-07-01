#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    ec2_mssql_database_pitr_interval_links as ec2_mssql_database_pitr_interval_links_
import requests

T = TypeVar('T', bound='EC2MssqlDatabasePitrInterval')


@dataclasses.dataclass
class EC2MssqlDatabasePitrInterval:
    """Implementation of the 'EC2MssqlDatabasePitrInterval' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        EndTimestamp:
            End timestamp of the interval. represented in rfc-3339 format.

        StartTimestamp:
            Start timestamp of the interval. represented in rfc-3339 format.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: object | None = None
    Links: ec2_mssql_database_pitr_interval_links_.EC2MssqlDatabasePitrIntervalLinks | None = None
    EndTimestamp: str | None = None
    StartTimestamp: str | None = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_database_pitr_interval_links_.EC2MssqlDatabasePitrIntervalLinks.from_dictionary(
            val
        )

        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_end_timestamp,
            val_start_timestamp,
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
