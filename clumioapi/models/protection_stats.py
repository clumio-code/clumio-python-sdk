#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='ProtectionStats')


@dataclasses.dataclass
class ProtectionStats:
    """Implementation of the 'ProtectionStats' model.

    Attributes:
        DeactivatedCount:
            The total number of entities associated with deactivated policies.

        ProtectedCount:
            The number of entities with protection applied.

        UnprotectedCount:
            The number of entities without protection applied.

    """

    DeactivatedCount: int | None = None
    ProtectedCount: int | None = None
    UnprotectedCount: int | None = None

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
        val = dictionary.get('deactivated_count', None)
        val_deactivated_count = val

        val = dictionary.get('protected_count', None)
        val_protected_count = val

        val = dictionary.get('unprotected_count', None)
        val_unprotected_count = val

        # Return an object of this model
        return cls(
            val_deactivated_count,
            val_protected_count,
            val_unprotected_count,
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
