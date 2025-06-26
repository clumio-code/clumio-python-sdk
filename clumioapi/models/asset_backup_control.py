#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import time_unit_param

T = TypeVar('T', bound='AssetBackupControl')


class AssetBackupControl:
    """Implementation of the 'AssetBackupControl' model.

    The control for asset backup.

    Attributes:
        look_back_period:
            The time unit used in control definition.
        minimum_retention_duration:
            The time unit used in control definition.
        window_size:
            The time unit used in control definition.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'look_back_period': 'look_back_period',
        'minimum_retention_duration': 'minimum_retention_duration',
        'window_size': 'window_size',
    }

    def __init__(
        self,
        look_back_period: time_unit_param.TimeUnitParam = None,
        minimum_retention_duration: time_unit_param.TimeUnitParam = None,
        window_size: time_unit_param.TimeUnitParam = None,
    ) -> None:
        """Constructor for the AssetBackupControl class."""

        # Initialize members of the class
        self.look_back_period: time_unit_param.TimeUnitParam = look_back_period
        self.minimum_retention_duration: time_unit_param.TimeUnitParam = minimum_retention_duration
        self.window_size: time_unit_param.TimeUnitParam = window_size

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
        key = 'look_back_period'
        look_back_period = (
            time_unit_param.TimeUnitParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'minimum_retention_duration'
        minimum_retention_duration = (
            time_unit_param.TimeUnitParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'window_size'
        window_size = (
            time_unit_param.TimeUnitParam.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(look_back_period, minimum_retention_duration, window_size)
