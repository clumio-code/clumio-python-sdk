#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import asset_backup_control as asset_backup_control_
from clumioapi.models import asset_protection_control as asset_protection_control_
from clumioapi.models import policy_control as policy_control_
import requests

T = TypeVar('T', bound='ComplianceControls')


@dataclasses.dataclass
class ComplianceControls:
    """Implementation of the 'ComplianceControls' model.

    Compliance controls to evaluate policy or assets for compliance.

    Attributes:
        AssetBackup:
            The control evaluating whether assets have at least one backup within each
            window of the specified look back period,
            with retention meeting the minimum required duration.
            for example, a look_back_period of 7 days, window_size of 1 day, and
            retention_duration of 1 month means that
            there should be a backup every day for the past week and that the retention of
            that backup should be at least 1 month.

        AssetProtection:
            The control evaluating if all assets are protected with a policy or not.

        Policy:
            The control evaluating if policies have a minimum backup retention and
            frequency.

    """

    AssetBackup: asset_backup_control_.AssetBackupControl | None = None
    AssetProtection: asset_protection_control_.AssetProtectionControl | None = None
    Policy: policy_control_.PolicyControl | None = None

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
        val = dictionary.get('asset_backup', None)
        val_asset_backup = asset_backup_control_.AssetBackupControl.from_dictionary(val)

        val = dictionary.get('asset_protection', None)
        val_asset_protection = asset_protection_control_.AssetProtectionControl.from_dictionary(val)

        val = dictionary.get('policy', None)
        val_policy = policy_control_.PolicyControl.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_backup,
            val_asset_protection,
            val_policy,
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
