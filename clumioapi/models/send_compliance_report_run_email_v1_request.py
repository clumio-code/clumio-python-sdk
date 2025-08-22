#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='SendComplianceReportRunEmailV1Request')


class SendComplianceReportRunEmailV1Request:
    """Implementation of the 'SendComplianceReportRunEmailV1Request' model.

    Attributes:
        email_list:
            List of emails to be notified.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'email_list': 'email_list'}

    def __init__(self, email_list: Sequence[str] | None = None) -> None:
        """Constructor for the SendComplianceReportRunEmailV1Request class."""

        # Initialize members of the class
        self.email_list: Sequence[str] | None = email_list

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
        val = dictionary.get('email_list', None)
        val_email_list = val

        # Return an object of this model
        return cls(
            val_email_list,
        )
