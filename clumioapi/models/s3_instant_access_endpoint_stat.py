#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='S3InstantAccessEndpointStat')


class S3InstantAccessEndpointStat:
    """Implementation of the 'S3InstantAccessEndpointStat' model.

    S3InstantAccessEndpointStatStatistical metric related to the instant access
    endpoint.S3InstantAccessEndpointStat swagger: model S3InstantAccessEndpointStat

    Attributes:
        count:
            The unit counts of the metric.
        name:
            The name of the metric.
        unit:
            Unit of the metric.
    """

    # Create a mapping from Model property names to API property names
    _names = {'count': 'count', 'name': 'name', 'unit': 'unit'}

    def __init__(self, count: int = None, name: str = None, unit: str = None) -> None:
        """Constructor for the S3InstantAccessEndpointStat class."""

        # Initialize members of the class
        self.count: int = count
        self.name: str = name
        self.unit: str = unit

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
        count = dictionary.get('count')
        name = dictionary.get('name')
        unit = dictionary.get('unit')
        # Return an object of this model
        return cls(count, name, unit)
