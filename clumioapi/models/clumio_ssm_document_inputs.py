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

    def __init__(
        self, runCommand: Sequence[str] | None = None, timeoutSeconds: str | None = None
    ) -> None:
        """Constructor for the ClumioSsmDocumentInputs class."""

        # Initialize members of the class
        self.runCommand: Sequence[str] | None = runCommand
        self.timeoutSeconds: str | None = timeoutSeconds

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
        val = dictionary.get('runCommand', None)
        val_runCommand = val

        val = dictionary.get('timeoutSeconds', None)
        val_timeoutSeconds = val

        # Return an object of this model
        return cls(
            val_runCommand,
            val_timeoutSeconds,
        )
