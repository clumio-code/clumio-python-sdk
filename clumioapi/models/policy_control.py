#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import time_unit_param

T = TypeVar('T', bound='PolicyControl')


class PolicyControl:
    """Implementation of the 'PolicyControl' model.

    The control for policy.

    Attributes:
        minimum_retention_duration:
            The time unit used in control definition.
        minimum_rpo_frequency:
            The time unit used in control definition.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'minimum_retention_duration': 'minimum_retention_duration',
        'minimum_rpo_frequency': 'minimum_rpo_frequency',
    }

    def __init__(
        self,
        minimum_retention_duration: time_unit_param.TimeUnitParam = None,
        minimum_rpo_frequency: time_unit_param.TimeUnitParam = None,
    ) -> None:
        """Constructor for the PolicyControl class."""

        # Initialize members of the class
        self.minimum_retention_duration: time_unit_param.TimeUnitParam = minimum_retention_duration
        self.minimum_rpo_frequency: time_unit_param.TimeUnitParam = minimum_rpo_frequency

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
        key = 'minimum_retention_duration'
        minimum_retention_duration = (
            time_unit_param.TimeUnitParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'minimum_rpo_frequency'
        minimum_rpo_frequency = (
            time_unit_param.TimeUnitParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(minimum_retention_duration, minimum_rpo_frequency)
