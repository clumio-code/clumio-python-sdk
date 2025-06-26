#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='NotificationSetting')


class NotificationSetting:
    """Implementation of the 'NotificationSetting' model.

    Notification channels to send the generated report runs.

    Attributes:
        email_list:
            Email list to send a generated report run.
    """

    # Create a mapping from Model property names to API property names
    _names = {'email_list': 'email_list'}

    def __init__(self, email_list: Sequence[str] = None) -> None:
        """Constructor for the NotificationSetting class."""

        # Initialize members of the class
        self.email_list: Sequence[str] = email_list

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
        email_list = dictionary.get('email_list')
        # Return an object of this model
        return cls(email_list)
