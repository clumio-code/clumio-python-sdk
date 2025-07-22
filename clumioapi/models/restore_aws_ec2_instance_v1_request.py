#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_restore_source as ec2_restore_source_
from clumioapi.models import ec2_restore_target as ec2_restore_target_

T = TypeVar('T', bound='RestoreAwsEc2InstanceV1Request')


class RestoreAwsEc2InstanceV1Request:
    """Implementation of the 'RestoreAwsEc2InstanceV1Request' model.

    Attributes:
        source:
            The EC2 instance backup to be restored.
        target:
            The target configuration per EC2 restore type. Only one of these fields should
            be set.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ec2_restore_source_.EC2RestoreSource,
        target: ec2_restore_target_.EC2RestoreTarget,
    ) -> None:
        """Constructor for the RestoreAwsEc2InstanceV1Request class."""

        # Initialize members of the class
        self.source: ec2_restore_source_.EC2RestoreSource = source
        self.target: ec2_restore_target_.EC2RestoreTarget = target

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
        val = dictionary['source']
        val_source = ec2_restore_source_.EC2RestoreSource.from_dictionary(val)

        val = dictionary['target']
        val_target = ec2_restore_target_.EC2RestoreTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,  # type: ignore
            val_target,  # type: ignore
        )
