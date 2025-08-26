#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception

T = TypeVar('T', bound='UpdateIndividualAlertV1Request')

StatusValues = [
    'cleared',
]


class UpdateIndividualAlertV1Request:
    """Implementation of the 'UpdateIndividualAlertV1Request' model.

    Attributes:
        notes:
            A record of information about the alert. The note must be less than 1024
            characters in length. Adding a new note overwrites any existing notes.
        status:
            Manually clears an active alert. To clear the alert, set to "cleared"`". Once an
            alert is cleared,
            the status of the alert changes from "active" to "cleared".
            If the alert is already in "cleared" status, this action is ignored.
            An alert that is in "cleared" status cannot be changed to "active" status.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'notes': 'notes', 'status': 'status'}

    def __init__(self, notes: str | None = None, status: str | None = None) -> None:
        """Constructor for the UpdateIndividualAlertV1Request class."""

        # Initialize members of the class
        self.notes: str | None = notes

        if status not in StatusValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for status: { status }. Valid values are { StatusValues }.'
            )
        self.status: str | None = status

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
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
