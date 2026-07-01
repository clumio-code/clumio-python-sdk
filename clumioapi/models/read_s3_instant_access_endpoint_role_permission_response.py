#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    s3_instant_access_endpoint_embedded as s3_instant_access_endpoint_embedded_
from clumioapi.models import s3_instant_access_endpoint_links as s3_instant_access_endpoint_links_
import requests

T = TypeVar('T', bound='ReadS3InstantAccessEndpointRolePermissionResponse')


@dataclasses.dataclass
class ReadS3InstantAccessEndpointRolePermissionResponse:
    """Implementation of the 'ReadS3InstantAccessEndpointRolePermissionResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Permissions:
            The permissions json string to be attached to the user's iam role to allow
            access to the
            instant access endpoint.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded | None = None
    Links: s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks | None = None
    Permissions: str | None = None
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
        val_embedded = (
            s3_instant_access_endpoint_embedded_.S3InstantAccessEndpointEmbedded.from_dictionary(
                val
            )
        )

        val = dictionary.get('_links', None)
        val_links = s3_instant_access_endpoint_links_.S3InstantAccessEndpointLinks.from_dictionary(
            val
        )

        val = dictionary.get('permissions', None)
        val_permissions = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_permissions,
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
