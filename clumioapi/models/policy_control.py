#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import time_unit_param as time_unit_param_

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
    _names: dict[str, str] = {
        'minimum_retention_duration': 'minimum_retention_duration',
        'minimum_rpo_frequency': 'minimum_rpo_frequency',
    }

    def __init__(
        self,
        minimum_retention_duration: time_unit_param_.TimeUnitParam | None = None,
        minimum_rpo_frequency: time_unit_param_.TimeUnitParam | None = None,
    ) -> None:
        """Constructor for the PolicyControl class."""

        # Initialize members of the class
        self.minimum_retention_duration: time_unit_param_.TimeUnitParam | None = (
            minimum_retention_duration
        )
        self.minimum_rpo_frequency: time_unit_param_.TimeUnitParam | None = minimum_rpo_frequency

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
        val = dictionary.get('minimum_retention_duration', None)
        val_minimum_retention_duration = time_unit_param_.TimeUnitParam.from_dictionary(val)

        val = dictionary.get('minimum_rpo_frequency', None)
        val_minimum_rpo_frequency = time_unit_param_.TimeUnitParam.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_minimum_retention_duration,
            val_minimum_rpo_frequency,
        )
