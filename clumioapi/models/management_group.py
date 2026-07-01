#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import management_group_links as management_group_links_
import requests

T = TypeVar('T', bound='ManagementGroup')


@dataclasses.dataclass
class ManagementGroup:
    """Implementation of the 'ManagementGroup' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        Id:
            The clumio-assigned id of the management group.

        Name:
            The name of the management group.

        Type:
            The type of the management group. possible values include `on_prem`.

        VcenterId:
            The clumio-assigned id of the vcenter server associated with the management
            group.
            all management groups are associated with a vcenter server.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: management_group_links_.ManagementGroupLinks | None = None
    Id: str | None = None
    Name: str | None = None
    Type: str | None = None
    VcenterId: str | None = None

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
        val = dictionary.get('_links', None)
        val_links = management_group_links_.ManagementGroupLinks.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('vcenter_id', None)
        val_vcenter_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_id,
            val_name,
            val_type,
            val_vcenter_id,
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
