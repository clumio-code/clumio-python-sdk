#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateComplianceReportRunV1Request')


class CreateComplianceReportRunV1Request:
    """Implementation of the 'CreateComplianceReportRunV1Request' model.

    Attributes:
        name:
            Name of the new compliance report run that will be created.
            If not given, default uses `{configuration ID} - {MM/DD/YYYY(Created time)}`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'name': 'name'}

    def __init__(self, name: str | None = None) -> None:
        """Constructor for the CreateComplianceReportRunV1Request class."""

        # Initialize members of the class
        self.name: str | None = name

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
        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_name,
        )
