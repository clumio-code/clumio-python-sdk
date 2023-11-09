#
# Copyright 2023. Clumio, Inc.
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
    _names = {'notes': 'notes', 'status': 'status'}

    def __init__(self, notes: str = None, status: str = None) -> None:
        """Constructor for the UpdateIndividualAlertV1Request class."""

        # Initialize members of the class
        self.notes: str = notes

        if status not in StatusValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for status: { status }. Valid values are { StatusValues }.',
                None,
            )
        self.status: str = status

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        notes = dictionary.get('notes')
        status = dictionary.get('status')
        # Return an object of this model
        return cls(notes, status)
