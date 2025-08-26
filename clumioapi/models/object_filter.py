#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import prefix_filter as prefix_filter_

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
    _names: dict[str, str] = {
        'earliest_last_modified_timestamp': 'earliest_last_modified_timestamp',
        'latest_version_only': 'latest_version_only',
        'prefix_filters': 'prefix_filters',
        'storage_classes': 'storage_classes',
    }

    def __init__(
        self,
        earliest_last_modified_timestamp: str | None = None,
        latest_version_only: bool | None = None,
        prefix_filters: Sequence[prefix_filter_.PrefixFilter] | None = None,
        storage_classes: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the ObjectFilter class."""

        # Initialize members of the class
        self.earliest_last_modified_timestamp: str | None = earliest_last_modified_timestamp
        self.latest_version_only: bool | None = latest_version_only
        self.prefix_filters: Sequence[prefix_filter_.PrefixFilter] | None = prefix_filters
        self.storage_classes: Sequence[str] | None = storage_classes

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
        val = dictionary.get('earliest_last_modified_timestamp', None)
        val_earliest_last_modified_timestamp = val

        val = dictionary.get('latest_version_only', None)
        val_latest_version_only = val

        val = dictionary.get('prefix_filters', None)

        val_prefix_filters = None
        if val:
            val_prefix_filters = list()
            for value in val:
                val_prefix_filters.append(prefix_filter_.PrefixFilter.from_dictionary(value))

        val = dictionary.get('storage_classes', None)
        val_storage_classes = val

        # Return an object of this model
        return cls(
            val_earliest_last_modified_timestamp,
            val_latest_version_only,
            val_prefix_filters,
            val_storage_classes,
        )
