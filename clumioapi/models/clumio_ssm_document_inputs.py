#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ClumioSsmDocumentInputs')


class ClumioSsmDocumentInputs:
    """Implementation of the 'ClumioSsmDocumentInputs' model.

    Attributes:
        runCommand:
            "runCommand" is an array of stringified commands.
        timeoutSeconds:
            "timeoutSeconds" is a stringified number denoting the timeout for command
            execution
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'runCommand': 'runCommand', 'timeoutSeconds': 'timeoutSeconds'}

    def __init__(self, runCommand: Sequence[str], timeoutSeconds: str) -> None:
        """Constructor for the ClumioSsmDocumentInputs class."""

        # Initialize members of the class
        self.runCommand: Sequence[str] = runCommand
        self.timeoutSeconds: str = timeoutSeconds

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
        val = dictionary['runCommand']
        val_runCommand = val

        val = dictionary['timeoutSeconds']
        val_timeoutSeconds = val

        # Return an object of this model
        return cls(
            val_runCommand,  # type: ignore
            val_timeoutSeconds,  # type: ignore
        )
