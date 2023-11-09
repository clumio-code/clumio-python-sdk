#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_restore_source
from clumioapi.models import ec2_restore_target

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
    _names = {'source': 'source', 'target': 'target'}

    def __init__(
        self,
        source: ec2_restore_source.EC2RestoreSource = None,
        target: ec2_restore_target.EC2RestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreAwsEc2InstanceV1Request class."""

        # Initialize members of the class
        self.source: ec2_restore_source.EC2RestoreSource = source
        self.target: ec2_restore_target.EC2RestoreTarget = target

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
        key = 'source'
        source = (
            ec2_restore_source.EC2RestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            ec2_restore_target.EC2RestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(source, target)
