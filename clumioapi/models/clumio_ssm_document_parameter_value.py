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

    def __init__(self, allowedPattern: str, default: str, description: str, p_type: str) -> None:
        """Constructor for the ClumioSsmDocumentParameterValue class."""

        # Initialize members of the class
        self.allowedPattern: str = allowedPattern
        self.default: str = default
        self.description: str = description
        self.p_type: str = p_type

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
        val = dictionary['allowedPattern']
        val_allowedPattern = val

        val = dictionary['default']
        val_default = val

        val = dictionary['description']
        val_description = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_allowedPattern,  # type: ignore
            val_default,  # type: ignore
            val_description,  # type: ignore
            val_p_type,  # type: ignore
        )
