#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import on_demand_setting as on_demand_setting_

T = TypeVar('T', bound='CreateBackupAwsEbsVolumeV2Request')

TypeValues = [
    'clumio_backup',
    'aws_snapshot',
]


class CreateBackupAwsEbsVolumeV2Request:
    """Implementation of the 'CreateBackupAwsEbsVolumeV2Request' model.

    Attributes:
        settings:
            Settings for requesting on-demand backup directly.
        p_type:
            The type of the backup. Possible values - `clumio_backup`, `aws_snapshot`. The
            type will be assumed as `clumio_backup` if the field is left empty.
        volume_id:
            Performs the operation on the EBS volume with the specified Clumio-assigned ID.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'settings': 'settings', 'p_type': 'type', 'volume_id': 'volume_id'}

    def __init__(
        self,
        settings: on_demand_setting_.OnDemandSetting | None = None,
        p_type: str | None = None,
        volume_id: str | None = None,
    ) -> None:
        """Constructor for the CreateBackupAwsEbsVolumeV2Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting_.OnDemandSetting | None = settings

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.',
                None,
            )
        self.p_type: str | None = p_type
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

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('volume_id', None)
        val_volume_id = val

        # Return an object of this model
        return cls(
            val_settings,
            val_p_type,
            val_volume_id,
        )
