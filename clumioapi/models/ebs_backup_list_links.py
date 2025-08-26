#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import hateoas_first_link as hateoas_first_link_
from clumioapi.models import hateoas_last_link as hateoas_last_link_
from clumioapi.models import hateoas_next_link as hateoas_next_link_
from clumioapi.models import hateoas_prev_link as hateoas_prev_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='EBSBackupListLinks')


@dataclasses.dataclass
class EBSBackupListLinks:
    """Implementation of the 'EBSBackupListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        First:
            The hateoas link to the first page of results.

        Last:
            The hateoas link to the last page of results.

        Next:
            The hateoas link to the next page of results.

        Prev:
            The hateoas link to the previous page of results.

        Self:
            The hateoas link to this resource.

    """

    First: hateoas_first_link_.HateoasFirstLink | None = None
    Last: hateoas_last_link_.HateoasLastLink | None = None
    Next: hateoas_next_link_.HateoasNextLink | None = None
    Prev: hateoas_prev_link_.HateoasPrevLink | None = None
    Self: hateoas_self_link_.HateoasSelfLink | None = None

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
        val = dictionary.get('_first', None)
        val_first = hateoas_first_link_.HateoasFirstLink.from_dictionary(val)

        val = dictionary.get('_last', None)
        val_last = hateoas_last_link_.HateoasLastLink.from_dictionary(val)

        val = dictionary.get('_next', None)
        val_next = hateoas_next_link_.HateoasNextLink.from_dictionary(val)

        val = dictionary.get('_prev', None)
        val_prev = hateoas_prev_link_.HateoasPrevLink.from_dictionary(val)

        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_first,
            val_last,
            val_next,
            val_prev,
            val_self,
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
