#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import gcp_project_links as gcp_project_links_
import requests

T = TypeVar('T', bound='GCPProject')


@dataclasses.dataclass
class GCPProject:
    """Implementation of the 'GCPProject' model.

    Attributes:
        Embedded

        Links

        CreatedTimestamp:
            Creation time of the project in rfc-3339 format.

        DeletedTimestamp:
            Deletion time of the project in rfc-3339 format.

        Id:
            The clumio-assigned id of the project.

        IsDeleted:
            Indicates whether the project has been deleted (`true`) or is active (`false`).

        ProjectId:
            The gcp project id.

        ProjectNumber:
            The gcp project number.

        UpdatedTimestamp:
            Last update time of the project in rfc-3339 format.

        Version:
            Resource version of the project.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Embedded': '_embedded',
        'Links': '_links',
    }

    Embedded: object | None = None
    Links: gcp_project_links_.GCPProjectLinks | None = None
    CreatedTimestamp: str | None = None
    DeletedTimestamp: str | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    ProjectId: str | None = None
    ProjectNumber: str | None = None
    UpdatedTimestamp: str | None = None
    Version: int | None = None

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
        val_links = gcp_project_links_.GCPProjectLinks.from_dictionary(val)

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('deleted_timestamp', None)
        val_deleted_timestamp = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('project_id', None)
        val_project_id = val

        val = dictionary.get('project_number', None)
        val_project_number = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        val = dictionary.get('version', None)
        val_version = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_created_timestamp,
            val_deleted_timestamp,
            val_id,
            val_is_deleted,
            val_project_id,
            val_project_number,
            val_updated_timestamp,
            val_version,
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
