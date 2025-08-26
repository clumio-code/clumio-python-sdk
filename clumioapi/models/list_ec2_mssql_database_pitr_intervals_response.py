#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    ec2_mssql_database_pitr_interval_list_embedded as \
    ec2_mssql_database_pitr_interval_list_embedded_
from clumioapi.models import \
    ec2_mssql_database_pitr_interval_list_links as ec2_mssql_database_pitr_interval_list_links_

T = TypeVar('T', bound='ListEC2MssqlDatabasePitrIntervalsResponse')


class ListEC2MssqlDatabasePitrIntervalsResponse:
    """Implementation of the 'ListEC2MssqlDatabasePitrIntervalsResponse' model.

    ListEC2MssqlDatabasePitrIntervalsResponse represents the success response

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        filter_applied:
            The filter used in the request. The filter includes both manually-specified and
            system-generated filters.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'filter_applied': 'filter_applied',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: (
            ec2_mssql_database_pitr_interval_list_embedded_.EC2MssqlDatabasePitrIntervalListEmbedded
            | None
        ) = None,
        links: (
            ec2_mssql_database_pitr_interval_list_links_.EC2MssqlDatabasePitrIntervalListLinks
            | None
        ) = None,
        current_count: int | None = None,
        filter_applied: str | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> None:
        """Constructor for the ListEC2MssqlDatabasePitrIntervalsResponse class."""

        # Initialize members of the class
        self.embedded: (
            ec2_mssql_database_pitr_interval_list_embedded_.EC2MssqlDatabasePitrIntervalListEmbedded
            | None
        ) = embedded
        self.links: (
            ec2_mssql_database_pitr_interval_list_links_.EC2MssqlDatabasePitrIntervalListLinks
            | None
        ) = links
        self.current_count: int | None = current_count
        self.filter_applied: str | None = filter_applied
        self.limit: int | None = limit
        self.start: str | None = start

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
        val_embedded = ec2_mssql_database_pitr_interval_list_embedded_.EC2MssqlDatabasePitrIntervalListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = ec2_mssql_database_pitr_interval_list_links_.EC2MssqlDatabasePitrIntervalListLinks.from_dictionary(
            val
        )

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('filter_applied', None)
        val_filter_applied = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_filter_applied,
            val_limit,
            val_start,
        )
