#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting as on_demand_setting_

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
    _names: dict[str, str] = {
        'instance_id': 'instance_id',
        'settings': 'settings',
        'p_type': 'type',
    }

    def __init__(
        self, instance_id: str, settings: on_demand_setting_.OnDemandSetting, p_type: str
    ) -> None:
        """Constructor for the CreateBackupAwsEc2InstanceV1Request class."""

        # Initialize members of the class
        self.instance_id: str = instance_id
        self.settings: on_demand_setting_.OnDemandSetting = settings
        self.p_type: str = p_type

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
        val = dictionary['instance_id']
        val_instance_id = val

        val = dictionary['settings']
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_instance_id,  # type: ignore
            val_settings,  # type: ignore
            val_p_type,  # type: ignore
        )
