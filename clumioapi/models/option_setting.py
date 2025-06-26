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
    _names = {'description': 'description', 'name': 'name', 'value': 'value'}

    def __init__(self, description: str = None, name: str = None, value: str = None) -> None:
        """Constructor for the OptionSetting class."""

        # Initialize members of the class
        self.description: str = description
        self.name: str = name
        self.value: str = value

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
        description = dictionary.get('description')
        name = dictionary.get('name')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(description, name, value)
