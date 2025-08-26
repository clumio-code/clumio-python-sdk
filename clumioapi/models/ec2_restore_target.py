#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ec2_ami_restore_target as ec2_ami_restore_target_
from clumioapi.models import ec2_instance_restore_target as ec2_instance_restore_target_
from clumioapi.models import ec2_volumes_restore_target as ec2_volumes_restore_target_
import requests

T = TypeVar('T', bound='EC2RestoreTarget')


@dataclasses.dataclass
class EC2RestoreTarget:
    """Implementation of the 'EC2RestoreTarget' model.

    The target configuration per EC2 restore type. Only one of these fields should
    be set.

    Attributes:
        AmiRestoreTarget:
            The configuration for the restore to ami.

        InstanceRestoreTarget:
            The configuration of an ec2 instance to be restored.

        VolumesRestoreTarget:
            The target configuration for the volumes to be restored.

    """

    AmiRestoreTarget: ec2_ami_restore_target_.EC2AMIRestoreTarget | None = None
    InstanceRestoreTarget: ec2_instance_restore_target_.EC2InstanceRestoreTarget | None = None
    VolumesRestoreTarget: ec2_volumes_restore_target_.EC2VolumesRestoreTarget | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('ami_restore_target', None)
        val_ami_restore_target = ec2_ami_restore_target_.EC2AMIRestoreTarget.from_dictionary(val)

        val = dictionary.get('instance_restore_target', None)
        val_instance_restore_target = (
            ec2_instance_restore_target_.EC2InstanceRestoreTarget.from_dictionary(val)
        )

        val = dictionary.get('volumes_restore_target', None)
        val_volumes_restore_target = (
            ec2_volumes_restore_target_.EC2VolumesRestoreTarget.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_ami_restore_target,
            val_instance_restore_target,
            val_volumes_restore_target,
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
