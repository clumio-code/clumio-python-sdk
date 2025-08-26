#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import read_task_hateoas_link as read_task_hateoas_link_
import requests

T = TypeVar('T', bound='CreateS3InstantAccessEndpointResponseLinks')


@dataclasses.dataclass
class CreateS3InstantAccessEndpointResponseLinks:
    """Implementation of the 'CreateS3InstantAccessEndpointResponseLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        ReadProtectionGroupInstantAccessEndpoint:
            Url to the detailed information of the instant access endpoint.

        ReadTask:
            A hateoas link to the task associated with this resource.

    """

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    ReadProtectionGroupInstantAccessEndpoint: object | None = None
    ReadTask: read_task_hateoas_link_.ReadTaskHateoasLink | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-protection-group-instant-access-endpoint', None)
        val_read_protection_group_instant_access_endpoint = val

        val = dictionary.get('read-task', None)
        val_read_task = read_task_hateoas_link_.ReadTaskHateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_read_protection_group_instant_access_endpoint,
            val_read_task,
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
