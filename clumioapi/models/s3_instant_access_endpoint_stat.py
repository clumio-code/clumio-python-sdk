#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {'count': 'count', 'name': 'name', 'unit': 'unit'}

    def __init__(self, count: int, name: str, unit: str) -> None:
        """Constructor for the S3InstantAccessEndpointStat class."""

        # Initialize members of the class
        self.count: int = count
        self.name: str = name
        self.unit: str = unit

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
        val = dictionary['count']
        val_count = val

        val = dictionary['name']
        val_name = val

        val = dictionary['unit']
        val_unit = val

        # Return an object of this model
        return cls(
            val_count,  # type: ignore
            val_name,  # type: ignore
            val_unit,  # type: ignore
        )
