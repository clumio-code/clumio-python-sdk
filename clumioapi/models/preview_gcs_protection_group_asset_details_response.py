#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcs_object as gcs_object_
from clumioapi.models import \
    preview_gcs_protection_group_asset_details_links as \
    preview_gcs_protection_group_asset_details_links_
import requests

T = TypeVar('T', bound='PreviewGCSProtectionGroupAssetDetailsResponse')


@dataclasses.dataclass
class PreviewGCSProtectionGroupAssetDetailsResponse:
    """Implementation of the 'PreviewGCSProtectionGroupAssetDetailsResponse' model.

    Attributes:
        Etag:
            The etag value.

        Links:
            Urls to pages related to the resource.

        Objects:
            The fetched objects as a result of the preview.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Etag': '_etag',
        'Links': '_links',
    }

    Etag: str | None = None
    Links: (
        preview_gcs_protection_group_asset_details_links_.PreviewGCSProtectionGroupAssetDetailsLinks
        | None
    ) = None
    Objects: Sequence[gcs_object_.GCSObject] | None = None
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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = preview_gcs_protection_group_asset_details_links_.PreviewGCSProtectionGroupAssetDetailsLinks.from_dictionary(
            val
        )

        val = dictionary.get('objects', None)

        val_objects = []
        if val:
            for value in val:
                val_objects.append(gcs_object_.GCSObject.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_objects,
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
