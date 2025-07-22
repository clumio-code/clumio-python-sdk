#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='Ec2TemplateInfo')


class Ec2TemplateInfo:
    """Implementation of the 'Ec2TemplateInfo' model.

    Attributes:
        available_template_version:
            The latest available feature version for the asset.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'available_template_version': 'available_template_version'}

    def __init__(self, available_template_version: str) -> None:
        """Constructor for the Ec2TemplateInfo class."""

        # Initialize members of the class
        self.available_template_version: str = available_template_version

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
        val = dictionary['available_template_version']
        val_available_template_version = val

        # Return an object of this model
        return cls(
            val_available_template_version,  # type: ignore
        )
