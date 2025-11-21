#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import management_group_links as management_group_links_
import requests

T = TypeVar('T', bound='UpdateManagementGroupResponse')


@dataclasses.dataclass
class UpdateManagementGroupResponse:
    """Implementation of the 'UpdateManagementGroupResponse' model.

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

    Links: management_group_links_.ManagementGroupLinks | None = None
    Id: str | None = None
    Name: str | None = None
    Type: str | None = None
    VcenterId: str | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        model_instance.raw_response = response
        return model_instance
