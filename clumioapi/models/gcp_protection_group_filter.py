#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GCPProtectionGroupFilter')


@dataclasses.dataclass
class GCPProtectionGroupFilter:
    """Implementation of the 'GCPProtectionGroupFilter' model.

    Attributes:
        ExcludeObjectNamePrefixRegexes:
            A list of prefixes to exclude from the backup. if multiple prefixes are
            specified,
            then any object whose path matches one of the prefixes will be excluded from the
            backup.

        IncludeObjectNamePrefixRegexes:
            A list of prefixes to include in the backup. if multiple prefixes are specified,
            then any object whose path matches one of the prefixes will be included in the
            backup.

        LatestVersion:
            Specifies that the protection group is configured with the latest version of the
            filter.

        StorageClasses:
            Storage classes included in the backup (standard, nearline, coldline, archive).
            if empty, objects of all storage classes are backed up.

        UpdatedAfter:
            Only back up objects created after this timestamp (rfc-3339).

    """

    ExcludeObjectNamePrefixRegexes: Sequence[str] | None = None
    IncludeObjectNamePrefixRegexes: Sequence[str] | None = None
    LatestVersion: bool | None = None
    StorageClasses: Sequence[str] | None = None
    UpdatedAfter: str | None = None

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
        val = dictionary.get('exclude_object_name_prefix_regexes', None)
        val_exclude_object_name_prefix_regexes = val

        val = dictionary.get('include_object_name_prefix_regexes', None)
        val_include_object_name_prefix_regexes = val

        val = dictionary.get('latest_version', None)
        val_latest_version = val

        val = dictionary.get('storage_classes', None)
        val_storage_classes = val

        val = dictionary.get('updated_after', None)
        val_updated_after = val

        # Return an object of this model
        return cls(
            val_exclude_object_name_prefix_regexes,
            val_include_object_name_prefix_regexes,
            val_latest_version,
            val_storage_classes,
            val_updated_after,
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
