#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_ami_restore_target
from clumioapi.models import ec2_instance_restore_target
from clumioapi.models import ec2_volumes_restore_target

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
    _names = {
        'ami_restore_target': 'ami_restore_target',
        'instance_restore_target': 'instance_restore_target',
        'volumes_restore_target': 'volumes_restore_target',
    }

    def __init__(
        self,
        ami_restore_target: ec2_ami_restore_target.EC2AMIRestoreTarget = None,
        instance_restore_target: ec2_instance_restore_target.EC2InstanceRestoreTarget = None,
        volumes_restore_target: ec2_volumes_restore_target.EC2VolumesRestoreTarget = None,
    ) -> None:
        """Constructor for the EC2RestoreTarget class."""

        # Initialize members of the class
        self.ami_restore_target: ec2_ami_restore_target.EC2AMIRestoreTarget = ami_restore_target
        self.instance_restore_target: ec2_instance_restore_target.EC2InstanceRestoreTarget = (
            instance_restore_target
        )
        self.volumes_restore_target: ec2_volumes_restore_target.EC2VolumesRestoreTarget = (
            volumes_restore_target
        )

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
        key = 'ami_restore_target'
        ami_restore_target = (
            ec2_ami_restore_target.EC2AMIRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'instance_restore_target'
        instance_restore_target = (
            ec2_instance_restore_target.EC2InstanceRestoreTarget.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'volumes_restore_target'
        volumes_restore_target = (
            ec2_volumes_restore_target.EC2VolumesRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(ami_restore_target, instance_restore_target, volumes_restore_target)
