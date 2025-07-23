#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_ami_restore_target as ec2_ami_restore_target_
from clumioapi.models import ec2_instance_restore_target as ec2_instance_restore_target_
from clumioapi.models import ec2_volumes_restore_target as ec2_volumes_restore_target_

T = TypeVar('T', bound='EC2RestoreTarget')


class EC2RestoreTarget:
    """Implementation of the 'EC2RestoreTarget' model.

    The target configuration per EC2 restore type. Only one of these fields should
    be set.

    Attributes:
        ami_restore_target:
            The configuration for the restore to AMI.
        instance_restore_target:
            The configuration of an EC2 instance to be restored.
        volumes_restore_target:
            The target configuration for the volumes to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'ami_restore_target': 'ami_restore_target',
        'instance_restore_target': 'instance_restore_target',
        'volumes_restore_target': 'volumes_restore_target',
    }

    def __init__(
        self,
        ami_restore_target: ec2_ami_restore_target_.EC2AMIRestoreTarget | None = None,
        instance_restore_target: (
            ec2_instance_restore_target_.EC2InstanceRestoreTarget | None
        ) = None,
        volumes_restore_target: ec2_volumes_restore_target_.EC2VolumesRestoreTarget | None = None,
    ) -> None:
        """Constructor for the EC2RestoreTarget class."""

        # Initialize members of the class
        self.ami_restore_target: ec2_ami_restore_target_.EC2AMIRestoreTarget | None = (
            ami_restore_target
        )
        self.instance_restore_target: (
            ec2_instance_restore_target_.EC2InstanceRestoreTarget | None
        ) = instance_restore_target
        self.volumes_restore_target: ec2_volumes_restore_target_.EC2VolumesRestoreTarget | None = (
            volumes_restore_target
        )

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
