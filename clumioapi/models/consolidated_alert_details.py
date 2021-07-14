#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ConsolidatedAlertDetails')


class ConsolidatedAlertDetails:
    """Implementation of the 'ConsolidatedAlertDetails' model.

    Additional information about the consolidated alert.

    Attributes:
        cause:
            A brief description of the condition that caused the alert. Examples include
            "Size Limit Exceeded" and "Insufficient Cloud Connector Capacity".
        type:
            The general alert category. Examples include "Policy Violated" and "Restore
            Failed".
    """

    # Create a mapping from Model property names to API property names
    _names = {'cause': 'cause', 'type': 'type'}

    def __init__(self, cause: str = None, type: str = None) -> None:
        """Constructor for the ConsolidatedAlertDetails class."""

        # Initialize members of the class
        self.cause: str = cause
        self.type: str = type

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
        cause = dictionary.get('cause')
        type = dictionary.get('type')
        # Return an object of this model
        return cls(cause, type)
