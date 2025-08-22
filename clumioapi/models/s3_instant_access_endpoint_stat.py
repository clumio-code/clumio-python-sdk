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

    def __init__(
        self, count: int | None = None, name: str | None = None, unit: str | None = None
    ) -> None:
        """Constructor for the S3InstantAccessEndpointStat class."""

        # Initialize members of the class
        self.count: int | None = count
        self.name: str | None = name
        self.unit: str | None = unit

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
        val = dictionary.get('count', None)
        val_count = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('unit', None)
        val_unit = val

        # Return an object of this model
        return cls(
            val_count,
            val_name,
            val_unit,
        )
