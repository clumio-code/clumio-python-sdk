#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import prefix_filter as prefix_filter_
import requests

T = TypeVar('T', bound='ObjectFilter')


@dataclasses.dataclass
class ObjectFilter:
    """Implementation of the 'ObjectFilter' model.

        ObjectFilterdefines which objects will be backed up.

        Attributes:
            EarliestLastModifiedTimestamp:
                The cutoff date for inclusion objects from the backup. any object with a last modified
    date after or equal  than this value will  be included in the backup. this is useful for
    filtering out old or irrelevant objects based on their modification timestamps.
    earliestlastmodifiedtimestamp support rfc-3339 format.

            LatestVersionOnly:
                Whether to back up only the latest object version.

            PrefixFilters:
                A list of prefixes to include or exclude in this protection group's backups.
    if not specified, then all objects will be backed up.

            StorageClasses:
                `s3 standard`, `s3 standard-ia`,
    `s3 intelligent-tiering`, and `s3 one zone-ia`.

    """

    EarliestLastModifiedTimestamp: str | None = None
    LatestVersionOnly: bool | None = None
    PrefixFilters: Sequence[prefix_filter_.PrefixFilter] | None = None
    StorageClasses: Sequence[str] | None = None

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
        val = dictionary.get('earliest_last_modified_timestamp', None)
        val_earliest_last_modified_timestamp = val

        val = dictionary.get('latest_version_only', None)
        val_latest_version_only = val

        val = dictionary.get('prefix_filters', None)

        val_prefix_filters = []
        if val:
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
