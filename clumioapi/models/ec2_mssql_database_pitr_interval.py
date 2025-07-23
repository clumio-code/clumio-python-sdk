#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    ec2_mssql_database_pitr_interval_links as ec2_mssql_database_pitr_interval_links_

T = TypeVar('T', bound='EC2MssqlDatabasePitrInterval')


class EC2MssqlDatabasePitrInterval:
    """Implementation of the 'EC2MssqlDatabasePitrInterval' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        end_timestamp:
            End timestamp of the interval. Represented in RFC-3339 format.
        start_timestamp:
            Start timestamp of the interval. Represented in RFC-3339 format.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'end_timestamp': 'end_timestamp',
        'start_timestamp': 'start_timestamp',
    }

    def __init__(
        self,
        embedded: object | None = None,
        links: (
            ec2_mssql_database_pitr_interval_links_.EC2MssqlDatabasePitrIntervalLinks | None
        ) = None,
        end_timestamp: str | None = None,
        start_timestamp: str | None = None,
    ) -> None:
        """Constructor for the EC2MssqlDatabasePitrInterval class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: (
            ec2_mssql_database_pitr_interval_links_.EC2MssqlDatabasePitrIntervalLinks | None
        ) = links
        self.end_timestamp: str | None = end_timestamp
        self.start_timestamp: str | None = start_timestamp

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

        dictionary = dictionary or {}
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
