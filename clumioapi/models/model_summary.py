#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='ModelSummary')


@dataclasses.dataclass
class ModelSummary:
    """Implementation of the 'ModelSummary' model.

    Attributes:
        AddedRecords

        Operation

        TotalFilesSize

        TotalRecords

    """

    AddedRecords: str | None = None
    Operation: str | None = None
    TotalFilesSize: str | None = None
    TotalRecords: str | None = None

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
        val = dictionary.get('added_records', None)
        val_added_records = val

        val = dictionary.get('operation', None)
        val_operation = val

        val = dictionary.get('total_files_size', None)
        val_total_files_size = val

        val = dictionary.get('total_records', None)
        val_total_records = val

        # Return an object of this model
        return cls(
            val_added_records,
            val_operation,
            val_total_files_size,
            val_total_records,
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
