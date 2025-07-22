#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import time_unit_param as time_unit_param_

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
    _names: dict[str, str] = {
        'look_back_period': 'look_back_period',
        'minimum_retention_duration': 'minimum_retention_duration',
        'window_size': 'window_size',
    }

    def __init__(
        self,
        look_back_period: time_unit_param_.TimeUnitParam,
        minimum_retention_duration: time_unit_param_.TimeUnitParam,
        window_size: time_unit_param_.TimeUnitParam,
    ) -> None:
        """Constructor for the AssetBackupControl class."""

        # Initialize members of the class
        self.look_back_period: time_unit_param_.TimeUnitParam = look_back_period
        self.minimum_retention_duration: time_unit_param_.TimeUnitParam = minimum_retention_duration
        self.window_size: time_unit_param_.TimeUnitParam = window_size

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
        val = dictionary['look_back_period']
        val_look_back_period = time_unit_param_.TimeUnitParam.from_dictionary(val)

        val = dictionary['minimum_retention_duration']
        val_minimum_retention_duration = time_unit_param_.TimeUnitParam.from_dictionary(val)

        val = dictionary['window_size']
        val_window_size = time_unit_param_.TimeUnitParam.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_look_back_period,  # type: ignore
            val_minimum_retention_duration,  # type: ignore
            val_window_size,  # type: ignore
        )
