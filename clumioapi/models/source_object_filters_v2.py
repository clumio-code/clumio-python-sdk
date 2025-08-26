#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='SourceObjectFiltersV2')


@dataclasses.dataclass
class SourceObjectFiltersV2:
    """Implementation of the 'SourceObjectFiltersV2' model.

        Search for or restore only objects that pass the source object filter.

        Attributes:
            Etag:
                Filter for objects with this etag.

            IsLatestVersionOnly:
                If set to true, filter for latest versions only. otherwise, all versions will
    be returned.

            MaxObjectSizeBytes:
                Filter for objects with at most this size in bytes.

            MinObjectSizeBytes:
                Filter for objects with at least this size in bytes.

            ObjectKeyContains:
                Filter for objects whose key contains this string.

            ObjectKeyMatches:
                Filter for objects whose key matches this string.

            ObjectKeyPrefix:
                Filter for objects that start with this key prefix.

            ObjectKeySuffix:
                Filter for objects that end with this key suffix.

            StorageClasses:
                `s3 standard`, `s3 standard-ia`, `s3 intelligent-tiering`
    and `s3 one zone-ia`.

            VersionId:
                Filter for objects with this version id.

    """

    Etag: str | None = None
    IsLatestVersionOnly: bool | None = None
    MaxObjectSizeBytes: int | None = None
    MinObjectSizeBytes: int | None = None
    ObjectKeyContains: str | None = None
    ObjectKeyMatches: str | None = None
    ObjectKeyPrefix: str | None = None
    ObjectKeySuffix: str | None = None
    StorageClasses: Sequence[str] | None = None
    VersionId: str | None = None

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
        val = dictionary.get('etag', None)
        val_etag = val

        val = dictionary.get('is_latest_version_only', None)
        val_is_latest_version_only = val

        val = dictionary.get('max_object_size_bytes', None)
        val_max_object_size_bytes = val

        val = dictionary.get('min_object_size_bytes', None)
        val_min_object_size_bytes = val

        val = dictionary.get('object_key_contains', None)
        val_object_key_contains = val

        val = dictionary.get('object_key_matches', None)
        val_object_key_matches = val

        val = dictionary.get('object_key_prefix', None)
        val_object_key_prefix = val

        val = dictionary.get('object_key_suffix', None)
        val_object_key_suffix = val

        val = dictionary.get('storage_classes', None)
        val_storage_classes = val

        val = dictionary.get('version_id', None)
        val_version_id = val

        # Return an object of this model
        return cls(
            val_etag,
            val_is_latest_version_only,
            val_max_object_size_bytes,
            val_min_object_size_bytes,
            val_object_key_contains,
            val_object_key_matches,
            val_object_key_prefix,
            val_object_key_suffix,
            val_storage_classes,
            val_version_id,
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
