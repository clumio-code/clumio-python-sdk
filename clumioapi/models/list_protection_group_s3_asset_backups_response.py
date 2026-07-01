#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    protection_group_s3_asset_backup_list_embedded as \
    protection_group_s3_asset_backup_list_embedded_
from clumioapi.models import \
    protection_group_s3_asset_backup_list_links as protection_group_s3_asset_backup_list_links_
import requests

T = TypeVar('T', bound='ListProtectionGroupS3AssetBackupsResponse')


@dataclasses.dataclass
class ListProtectionGroupS3AssetBackupsResponse:
    """Implementation of the 'ListProtectionGroupS3AssetBackupsResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        CurrentCount:
            The number of items listed on the current page.

        FilterApplied:
            The filter used in the request. the filter includes both manually-specified and
            system-generated filters.

        Limit:
            The maximum number of items displayed per page in the response.

        Start:
            "1"`).

        TotalCount:
            The total number of items, summed across all pages.

        TotalPagesCount:
            The total number of pages of results.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: (
        protection_group_s3_asset_backup_list_embedded_.ProtectionGroupS3AssetBackupListEmbedded
        | None
    ) = None
    Links: (
        protection_group_s3_asset_backup_list_links_.ProtectionGroupS3AssetBackupListLinks | None
    ) = None
    CurrentCount: int | None = None
    FilterApplied: str | None = None
    Limit: int | None = None
    Start: str | None = None
    TotalCount: int | None = None
    TotalPagesCount: int | None = None
    raw_response: Optional[requests.Response] = None

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
        val_embedded = protection_group_s3_asset_backup_list_embedded_.ProtectionGroupS3AssetBackupListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = protection_group_s3_asset_backup_list_links_.ProtectionGroupS3AssetBackupListLinks.from_dictionary(
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

        val = dictionary.get('total_count', None)
        val_total_count = val

        val = dictionary.get('total_pages_count', None)
        val_total_pages_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_filter_applied,
            val_limit,
            val_start,
            val_total_count,
            val_total_pages_count,
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
        model_instance.raw_response = response
        return model_instance
