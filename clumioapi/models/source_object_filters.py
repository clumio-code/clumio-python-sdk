#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SourceObjectFilters')


class SourceObjectFilters:
    """Implementation of the 'SourceObjectFilters' model.

    Search for or restore only objects that pass the source object filter.

    Attributes:
        etag:
            Filter for objects with this etag.
        latest_version_only:
            If set to true, filter for latest versions only. Otherwise, all versions will
            be returned.
        max_object_size_bytes:
            Filter for objects with at most this size in bytes.
        min_object_size_bytes:
            Filter for objects with at least this size in bytes.
        object_key_contains:
            Filter for objects whose key contains this string.
        object_key_matches:
            Filter for objects whose key matches this string.
        object_key_prefix:
            Filter for objects that start with this key prefix.
        object_key_suffix:
            Filter for objects that end with this key suffix.
        storage_classes:
            Storage class to include in the restore. If not specified, then all objects
            across all storage
            classes will be restored. Valid values are: `S3 Standard`, `S3 Standard-IA`, `S3
            Intelligent-Tiering`
            and `S3 One Zone-IA`.
        version_id:
            Filter for objects with this version ID.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'etag': 'etag',
        'latest_version_only': 'latest_version_only',
        'max_object_size_bytes': 'max_object_size_bytes',
        'min_object_size_bytes': 'min_object_size_bytes',
        'object_key_contains': 'object_key_contains',
        'object_key_matches': 'object_key_matches',
        'object_key_prefix': 'object_key_prefix',
        'object_key_suffix': 'object_key_suffix',
        'storage_classes': 'storage_classes',
        'version_id': 'version_id',
    }

    def __init__(
        self,
        etag: str,
        latest_version_only: bool,
        max_object_size_bytes: int,
        min_object_size_bytes: int,
        object_key_contains: str,
        object_key_matches: str,
        object_key_prefix: str,
        object_key_suffix: str,
        storage_classes: Sequence[str],
        version_id: str,
    ) -> None:
        """Constructor for the SourceObjectFilters class."""

        # Initialize members of the class
        self.etag: str = etag
        self.latest_version_only: bool = latest_version_only
        self.max_object_size_bytes: int = max_object_size_bytes
        self.min_object_size_bytes: int = min_object_size_bytes
        self.object_key_contains: str = object_key_contains
        self.object_key_matches: str = object_key_matches
        self.object_key_prefix: str = object_key_prefix
        self.object_key_suffix: str = object_key_suffix
        self.storage_classes: Sequence[str] = storage_classes
        self.version_id: str = version_id

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

        # Extract variables from the dictionary
        val = dictionary['etag']
        val_etag = val

        val = dictionary['latest_version_only']
        val_latest_version_only = val

        val = dictionary['max_object_size_bytes']
        val_max_object_size_bytes = val

        val = dictionary['min_object_size_bytes']
        val_min_object_size_bytes = val

        val = dictionary['object_key_contains']
        val_object_key_contains = val

        val = dictionary['object_key_matches']
        val_object_key_matches = val

        val = dictionary['object_key_prefix']
        val_object_key_prefix = val

        val = dictionary['object_key_suffix']
        val_object_key_suffix = val

        val = dictionary['storage_classes']
        val_storage_classes = val

        val = dictionary['version_id']
        val_version_id = val

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_latest_version_only,  # type: ignore
            val_max_object_size_bytes,  # type: ignore
            val_min_object_size_bytes,  # type: ignore
            val_object_key_contains,  # type: ignore
            val_object_key_matches,  # type: ignore
            val_object_key_prefix,  # type: ignore
            val_object_key_suffix,  # type: ignore
            val_storage_classes,  # type: ignore
            val_version_id,  # type: ignore
        )
