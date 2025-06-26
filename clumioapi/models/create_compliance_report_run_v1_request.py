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
    _names = {'name': 'name'}

    def __init__(self, name: str = None) -> None:
        """Constructor for the CreateComplianceReportRunV1Request class."""

        # Initialize members of the class
        self.name: str = name

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
        name = dictionary.get('name')
        # Return an object of this model
        return cls(name)
