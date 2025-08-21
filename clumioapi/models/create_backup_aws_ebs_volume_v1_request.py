#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting as on_demand_setting_

T = TypeVar('T', bound='CreateBackupAwsEbsVolumeV1Request')


class CreateBackupAwsEbsVolumeV1Request:
    """Implementation of the 'CreateBackupAwsEbsVolumeV1Request' model.

    Attributes:
        settings:
            Settings for requesting on-demand backup directly.
        volume_id:
            Performs the operation on the EBS volume with the specified Clumio-assigned ID.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'settings': 'settings', 'volume_id': 'volume_id'}

    def __init__(
        self,
        settings: on_demand_setting_.OnDemandSetting | None = None,
        volume_id: str | None = None,
    ) -> None:
        """Constructor for the CreateBackupAwsEbsVolumeV1Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting_.OnDemandSetting | None = settings
        self.volume_id: str | None = volume_id

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
        val = dictionary.get('settings', None)
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary.get('volume_id', None)
        val_volume_id = val

        # Return an object of this model
        return cls(
            val_settings,
            val_volume_id,
        )
