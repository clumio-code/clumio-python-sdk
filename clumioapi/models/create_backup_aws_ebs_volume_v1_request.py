#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting

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
    _names = {'settings': 'settings', 'volume_id': 'volume_id'}

    def __init__(
        self, settings: on_demand_setting.OnDemandSetting = None, volume_id: str = None
    ) -> None:
        """Constructor for the CreateBackupAwsEbsVolumeV1Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting.OnDemandSetting = settings
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

        volume_id = dictionary.get('volume_id')
        # Return an object of this model
        return cls(settings, volume_id)
