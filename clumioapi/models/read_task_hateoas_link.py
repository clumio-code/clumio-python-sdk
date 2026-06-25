#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='ReadTaskHateoasLink')


@dataclasses.dataclass
class ReadTaskHateoasLink:
    """Implementation of the 'ReadTaskHateoasLink' model.

    A HATEOAS link to the task associated with this resource.

    Attributes:
        Href:
            The uri for the referenced operation.

        Templated:
            Determines whether the "href" link is a uri template. if set to `true`, the
            "href" link is a uri template.

        Type:
            The http method to be used with the "href" link for the referenced operation.

    """

    Href: str | None = None
    Templated: bool | None = None
    Type: str | None = None

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
        val = dictionary.get('href', None)
        val_href = val

        val = dictionary.get('templated', None)
        val_templated = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_href,
            val_templated,
            val_type,
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
