#
# Copyright 2021. Clumio, Inc.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import on_demand_setting

T = TypeVar('T', bound='CreateBackupAwsEbsVolumeV2Request')

TypeValues = [
    '',
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
    _names = {'settings': 'settings', 'p_type': 'type', 'volume_id': 'volume_id'}

    def __init__(
        self,
        settings: on_demand_setting.OnDemandSetting = None,
        p_type: str = None,
        volume_id: str = None,
    ) -> None:
        """Constructor for the CreateBackupAwsEbsVolumeV2Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting.OnDemandSetting = settings

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.',
                None,
            )
        self.p_type: str = p_type
        self.volume_id: str = volume_id

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
        key = 'settings'
        settings = (
            on_demand_setting.OnDemandSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_type = dictionary.get('type')
        volume_id = dictionary.get('volume_id')
        # Return an object of this model
        return cls(settings, p_type, volume_id)
