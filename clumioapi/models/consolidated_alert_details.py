#
# Copyright 2023. Clumio, A Commvault Company.
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
        p_type:
            The general alert category. Examples include "Policy Violated" and "Restore
            Failed".
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'cause': 'cause', 'p_type': 'type'}

    def __init__(self, cause: str | None = None, p_type: str | None = None) -> None:
        """Constructor for the ConsolidatedAlertDetails class."""

        # Initialize members of the class
        self.cause: str | None = cause
        self.p_type: str | None = p_type

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
        val = dictionary.get('cause', None)
        val_cause = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_cause,
            val_p_type,
        )
