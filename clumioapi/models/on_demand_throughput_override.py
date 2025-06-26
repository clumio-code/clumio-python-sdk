#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='OnDemandThroughputOverride')


class OnDemandThroughputOverride:
    """Implementation of the 'OnDemandThroughputOverride' model.

    Replica-specific ondemand throughput settings. If not specified, uses the source
    table's ondemand throughput settings.

    Attributes:
        max_read_request_units:
            The maximum number of strongly consistent reads consumed per second.
    """

    # Create a mapping from Model property names to API property names
    _names = {'max_read_request_units': 'max_read_request_units'}

    def __init__(self, max_read_request_units: int = None) -> None:
        """Constructor for the OnDemandThroughputOverride class."""

        # Initialize members of the class
        self.max_read_request_units: int = max_read_request_units

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
        max_read_request_units = dictionary.get('max_read_request_units')
        # Return an object of this model
        return cls(max_read_request_units)
