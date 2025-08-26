#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='UpdateConsolidatedAlertV1Request')

StatusValues = [
    'cleared',
]


@dataclasses.dataclass
class UpdateConsolidatedAlertV1Request:
    """Implementation of the 'UpdateConsolidatedAlertV1Request' model.

        Attributes:
            Notes:
                A record of user-provided information about the alert. the note must be less than 1024 characters in length. adding a new note overwrites any existing notes.

            Status:
                Manually clears an active alert. to clear the active alert, set the parameter to "cleared". once an alert is cleared,
    the status of the alert changes from "active" to "cleared".
    if the alert is already in "cleared" status, this action is ignored.
    an alert that is in "cleared" status cannot be changed to "active" status.

    """

    Notes: str | None = None

    Status: str | None = None

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
        val = dictionary.get('notes', None)
        val_notes = val

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_notes,
            val_status,
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
