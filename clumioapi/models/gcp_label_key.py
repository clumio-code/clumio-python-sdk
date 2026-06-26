#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_label_key_links as gcp_label_key_links_
import requests

T = TypeVar('T', bound='GCPLabelKey')


@dataclasses.dataclass
class GCPLabelKey:
    """Implementation of the 'GCPLabelKey' model.

    Attributes:
        Embedded

        Links

        CreatedTimestamp

        Id

        IsDeleted

        ModifiedTimestamp

        Name

        ProjectUuid

        RegionUuid

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: object | None = None
    Links: gcp_label_key_links_.GCPLabelKeyLinks | None = None
    CreatedTimestamp: str | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    ModifiedTimestamp: str | None = None
    Name: str | None = None
    ProjectUuid: str | None = None
    RegionUuid: str | None = None

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
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = gcp_label_key_links_.GCPLabelKeyLinks.from_dictionary(val)

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('modified_timestamp', None)
        val_modified_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('project_uuid', None)
        val_project_uuid = val

        val = dictionary.get('region_uuid', None)
        val_region_uuid = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_created_timestamp,
            val_id,
            val_is_deleted,
            val_modified_timestamp,
            val_name,
            val_project_uuid,
            val_region_uuid,
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
