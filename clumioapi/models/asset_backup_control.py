#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import \
    time_unit_param_asset_backup_min_retention_duration as \
    time_unit_param_asset_backup_min_retention_duration_
from clumioapi.models import time_unit_param_lookback_period as time_unit_param_lookback_period_
from clumioapi.models import time_unit_param_window_size as time_unit_param_window_size_
import requests

T = TypeVar('T', bound='AssetBackupControl')


@dataclasses.dataclass
class AssetBackupControl:
    """Implementation of the 'AssetBackupControl' model.

    The control evaluating whether assets have at least one backup within each
    window of the specified look back period,with retention meeting the minimum
    required duration.For example, a look_back_period of 7 days, window_size of 1
    day, and retention_duration of 1 month means thatthere should be a backup every
    day for the past week and that the retention of that backup should be at least 1
    month.

    Attributes:
        LookBackPeriod:
            The duration prior to the compliance evaluation point to look back.

        MinimumRetentionDuration:
            The minimum required retention duration for a backup to be considered compliant.

        WindowSize:
            The size of each evaluation window within the look back period in which at least
            one compliant backup must exist.

    """

    LookBackPeriod: time_unit_param_lookback_period_.TimeUnitParamLookbackPeriod | None = None
    MinimumRetentionDuration: (
        time_unit_param_asset_backup_min_retention_duration_.TimeUnitParamAssetBackupMinRetentionDuration
        | None
    ) = None
    WindowSize: time_unit_param_window_size_.TimeUnitParamWindowSize | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('look_back_period', None)
        val_look_back_period = (
            time_unit_param_lookback_period_.TimeUnitParamLookbackPeriod.from_dictionary(val)
        )

        val = dictionary.get('minimum_retention_duration', None)
        val_minimum_retention_duration = time_unit_param_asset_backup_min_retention_duration_.TimeUnitParamAssetBackupMinRetentionDuration.from_dictionary(
            val
        )

        val = dictionary.get('window_size', None)
        val_window_size = time_unit_param_window_size_.TimeUnitParamWindowSize.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_look_back_period,
            val_minimum_retention_duration,
            val_window_size,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
