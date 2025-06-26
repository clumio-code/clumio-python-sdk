#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SourceObjectFiltersV2')


class SourceObjectFiltersV2:
    """Implementation of the 'SourceObjectFiltersV2' model.

    Search for or restore only objects that pass the source object filter.

    Attributes:
        etag:
            Filter for objects with this etag.
        is_latest_version_only:
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
    _names = {
        'etag': 'etag',
        'is_latest_version_only': 'is_latest_version_only',
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
        etag: str = None,
        is_latest_version_only: bool = None,
        max_object_size_bytes: int = None,
        min_object_size_bytes: int = None,
        object_key_contains: str = None,
        object_key_matches: str = None,
        object_key_prefix: str = None,
        object_key_suffix: str = None,
        storage_classes: Sequence[str] = None,
        version_id: str = None,
    ) -> None:
        """Constructor for the SourceObjectFiltersV2 class."""

        # Initialize members of the class
        self.etag: str = etag
        self.is_latest_version_only: bool = is_latest_version_only
        self.max_object_size_bytes: int = max_object_size_bytes
        self.min_object_size_bytes: int = min_object_size_bytes
        self.object_key_contains: str = object_key_contains
        self.object_key_matches: str = object_key_matches
        self.object_key_prefix: str = object_key_prefix
        self.object_key_suffix: str = object_key_suffix
        self.storage_classes: Sequence[str] = storage_classes
        self.version_id: str = version_id

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
        etag = dictionary.get('etag')
        is_latest_version_only = dictionary.get('is_latest_version_only')
        max_object_size_bytes = dictionary.get('max_object_size_bytes')
        min_object_size_bytes = dictionary.get('min_object_size_bytes')
        object_key_contains = dictionary.get('object_key_contains')
        object_key_matches = dictionary.get('object_key_matches')
        object_key_prefix = dictionary.get('object_key_prefix')
        object_key_suffix = dictionary.get('object_key_suffix')
        storage_classes = dictionary.get('storage_classes')
        version_id = dictionary.get('version_id')
        # Return an object of this model
        return cls(
            etag,
            is_latest_version_only,
            max_object_size_bytes,
            min_object_size_bytes,
            object_key_contains,
            object_key_matches,
            object_key_prefix,
            object_key_suffix,
            storage_classes,
            version_id,
        )
