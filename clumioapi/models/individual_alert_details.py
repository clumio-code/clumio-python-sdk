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
        self, cause: str, description: str, p_type: str, variables: Mapping[str, str]
    ) -> None:
        """Constructor for the IndividualAlertDetails class."""

        # Initialize members of the class
        self.cause: str = cause
        self.description: str = description
        self.p_type: str = p_type
        self.variables: Mapping[str, str] = variables

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

        # Extract variables from the dictionary
        val = dictionary['cause']
        val_cause = val

        val = dictionary['description']
        val_description = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['variables']
        val_variables = val

        # Return an object of this model
        return cls(
            val_cause,  # type: ignore
            val_description,  # type: ignore
            val_p_type,  # type: ignore
            val_variables,  # type: ignore
        )
