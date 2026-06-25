#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GlueCompactionConfiguration')


@dataclasses.dataclass
class GlueCompactionConfiguration:
    """Implementation of the 'GlueCompactionConfiguration' model.

    Attributes:
        DeleteFileThreshold

        MinInputFiles

        Status

        Strategy

    """

    DeleteFileThreshold: int | None = None
    MinInputFiles: int | None = None
    Status: str | None = None
    Strategy: str | None = None

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
        val = dictionary.get('delete_file_threshold', None)
        val_delete_file_threshold = val

        val = dictionary.get('min_input_files', None)
        val_min_input_files = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('strategy', None)
        val_strategy = val

        # Return an object of this model
        return cls(
            val_delete_file_threshold,
            val_min_input_files,
            val_status,
            val_strategy,
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
