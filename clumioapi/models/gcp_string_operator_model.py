#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GCPStringOperatorModel')


@dataclasses.dataclass
class GCPStringOperatorModel:
    """Implementation of the 'GCPStringOperatorModel' model.

    Attributes:
        Eq

        In

        NotEq

        NotIn

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Eq': '$eq',
        'In': '$in',
        'NotEq': '$not_eq',
        'NotIn': '$not_in',
    }

    Eq: str | None = None
    In: Sequence[str] | None = None
    NotEq: str | None = None
    NotIn: Sequence[str] | None = None

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
        val = dictionary.get('$eq', None)
        val_eq = val

        val = dictionary.get('$in', None)
        val_in = val

        val = dictionary.get('$not_eq', None)
        val_not_eq = val

        val = dictionary.get('$not_in', None)
        val_not_in = val

        # Return an object of this model
        return cls(
            val_eq,
            val_in,
            val_not_eq,
            val_not_in,
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
