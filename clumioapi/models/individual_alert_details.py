#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='IndividualAlertDetails')


class IndividualAlertDetails:
    """Implementation of the 'IndividualAlertDetails' model.

    Additional information about the alert.

    Attributes:
        cause:
            A brief description of the condition that caused the alert. Examples include
            "Size Limit Exceeded" and "Insufficient Cloud Connector Capacity".
        description:
            A detailed description of the alert, including the reason why the alert occurred
            and the steps you must take to resolve the issue.
        p_type:
            The general alert category. Examples include "Policy Violated" and "Restore
            Failed".
        variables:
            Data specific to the alert generated. If the alert has no variables, then this
            field has a value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'cause': 'cause',
        'description': 'description',
        'p_type': 'type',
        'variables': 'variables',
    }

    def __init__(
        self,
        cause: str | None = None,
        description: str | None = None,
        p_type: str | None = None,
        variables: Mapping[str, str] | None = None,
    ) -> None:
        """Constructor for the IndividualAlertDetails class."""

        # Initialize members of the class
        self.cause: str | None = cause
        self.description: str | None = description
        self.p_type: str | None = p_type
        self.variables: Mapping[str, str] | None = variables

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

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('variables', None)
        val_variables = val

        # Return an object of this model
        return cls(
            val_cause,
            val_description,
            val_p_type,
            val_variables,
        )
