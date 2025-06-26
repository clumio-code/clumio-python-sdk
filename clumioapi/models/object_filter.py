#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import prefix_filter

T = TypeVar('T', bound='ObjectFilter')


class ObjectFilter:
    """Implementation of the 'ObjectFilter' model.

    ObjectFilterdefines which objects will be backed up.

    Attributes:
        earliest_last_modified_timestamp:
            The cutoff date for inclusion objects from the backup. Any object with a last
            modified
            date after or equal  than this value will  be included in the backup. This is
            useful for
            filtering out old or irrelevant objects based on their modification timestamps.
            EarliestLastModifiedTimeStamp support RFC-3339 format.
        latest_version_only:
            Whether to back up only the latest object version.
        prefix_filters:
            A list of prefixes to include or exclude in this protection group's backups.
            If not specified, then all objects will be backed up.
        storage_classes:
            Storage class to include in the backup. If not specified, then all objects
            across all storage
            classes will be backed up. Valid values are: `S3 Standard`, `S3 Standard-IA`,
            `S3 Intelligent-Tiering`, and `S3 One Zone-IA`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'earliest_last_modified_timestamp': 'earliest_last_modified_timestamp',
        'latest_version_only': 'latest_version_only',
        'prefix_filters': 'prefix_filters',
        'storage_classes': 'storage_classes',
    }

    def __init__(
        self,
        earliest_last_modified_timestamp: str = None,
        latest_version_only: bool = None,
        prefix_filters: Sequence[prefix_filter.PrefixFilter] = None,
        storage_classes: Sequence[str] = None,
    ) -> None:
        """Constructor for the ObjectFilter class."""

        # Initialize members of the class
        self.earliest_last_modified_timestamp: str = earliest_last_modified_timestamp
        self.latest_version_only: bool = latest_version_only
        self.prefix_filters: Sequence[prefix_filter.PrefixFilter] = prefix_filters
        self.storage_classes: Sequence[str] = storage_classes

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
        earliest_last_modified_timestamp = dictionary.get('earliest_last_modified_timestamp')
        latest_version_only = dictionary.get('latest_version_only')
        prefix_filters = None
        if dictionary.get('prefix_filters'):
            prefix_filters = list()
            for value in dictionary.get('prefix_filters'):
                prefix_filters.append(prefix_filter.PrefixFilter.from_dictionary(value))

        storage_classes = dictionary.get('storage_classes')
        # Return an object of this model
        return cls(
            earliest_last_modified_timestamp, latest_version_only, prefix_filters, storage_classes
        )
