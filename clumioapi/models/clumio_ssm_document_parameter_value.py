#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ClumioSsmDocumentParameterValue')


class ClumioSsmDocumentParameterValue:
    """Implementation of the 'ClumioSsmDocumentParameterValue' model.

    Details for each parameters of the ssm document

    Attributes:
        allowedPattern:
            "allowedPattern" refers to the pattern that must be satisfied by the parameter
        default:
            "default" refers to the default value for that paramter
        description:
            "description" is optional
        p_type:
            "type" refers to the parameter type
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'allowedPattern': 'allowedPattern',
        'default': 'default',
        'description': 'description',
        'p_type': 'type',
    }

    def __init__(
        self,
        allowedPattern: str | None = None,
        default: str | None = None,
        description: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the ClumioSsmDocumentParameterValue class."""

        # Initialize members of the class
        self.allowedPattern: str | None = allowedPattern
        self.default: str | None = default
        self.description: str | None = description
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
        val = dictionary.get('allowedPattern', None)
        val_allowedPattern = val

        val = dictionary.get('default', None)
        val_default = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_allowedPattern,
            val_default,
            val_description,
            val_p_type,
        )
