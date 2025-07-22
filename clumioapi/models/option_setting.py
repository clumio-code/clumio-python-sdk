#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OptionSetting')


class OptionSetting:
    """Implementation of the 'OptionSetting' model.

    OptionSetting denotes the Model for OptionSetting

    Attributes:
        description:
            The AWS-assigned description of the RDS option setting.
        name:
            The AWS-assigned name of the RDS option setting.
        value:
            Value of the option setting
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'description': 'description', 'name': 'name', 'value': 'value'}

    def __init__(self, description: str, name: str, value: str) -> None:
        """Constructor for the OptionSetting class."""

        # Initialize members of the class
        self.description: str = description
        self.name: str = name
        self.value: str = value

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
        val = dictionary['description']
        val_description = val

        val = dictionary['name']
        val_name = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_name,  # type: ignore
            val_value,  # type: ignore
        )
