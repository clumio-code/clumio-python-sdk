#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting

T = TypeVar('T', bound='CreateBackupAwsEc2InstanceV1Request')


class CreateBackupAwsEc2InstanceV1Request:
    """Implementation of the 'CreateBackupAwsEc2InstanceV1Request' model.

    Attributes:
        instance_id:
            Performs the operation on the EC2 instance with the specified Clumio-assigned
            ID.
        settings:
            Settings for requesting on-demand backup directly.
        p_type:
            The type of the backup. Possible values - `clumio_backup`, `aws_snapshot`. The
            type will be assumed as `clumio_backup` if the field is left empty.
    """

    # Create a mapping from Model property names to API property names
    _names = {'instance_id': 'instance_id', 'settings': 'settings', 'p_type': 'type'}

    def __init__(
        self,
        instance_id: str = None,
        settings: on_demand_setting.OnDemandSetting = None,
        p_type: str = None,
    ) -> None:
        """Constructor for the CreateBackupAwsEc2InstanceV1Request class."""

        # Initialize members of the class
        self.instance_id: str = instance_id
        self.settings: on_demand_setting.OnDemandSetting = settings
        self.p_type: str = p_type

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
        instance_id = dictionary.get('instance_id')
        key = 'settings'
        settings = (
            on_demand_setting.OnDemandSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(instance_id, settings, p_type)
