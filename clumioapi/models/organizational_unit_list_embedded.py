#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import organizational_unit_with_e_tag as organizational_unit_with_e_tag_
import requests

T = TypeVar('T', bound='OrganizationalUnitListEmbedded')


@dataclasses.dataclass
class OrganizationalUnitListEmbedded:
    """Implementation of the 'OrganizationalUnitListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        Items:
            A collection of requested items.

    """

    Items: Sequence[organizational_unit_with_e_tag_.OrganizationalUnitWithETag] | None = None

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
        val = dictionary.get('items', None)

        val_items = []
        if val:
            for value in val:
                val_items.append(
                    organizational_unit_with_e_tag_.OrganizationalUnitWithETag.from_dictionary(
                        value
                    )
                )

        # Return an object of this model
        return cls(
            val_items,
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
