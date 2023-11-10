#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AWSEnvironmentEmbedded')


class AWSEnvironmentEmbedded:
    """Implementation of the 'AWSEnvironmentEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_aws_environment_ebs_volumes_compliance_stats:

    """

    # Create a mapping from Model property names to API property names
    _names = {
        'read_aws_environment_ebs_volumes_compliance_stats': 'read-aws-environment-ebs-volumes-compliance-stats'
    }

    def __init__(self, read_aws_environment_ebs_volumes_compliance_stats: object = None) -> None:
        """Constructor for the AWSEnvironmentEmbedded class."""

        # Initialize members of the class
        self.read_aws_environment_ebs_volumes_compliance_stats: object = (
            read_aws_environment_ebs_volumes_compliance_stats
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
        read_aws_environment_ebs_volumes_compliance_stats = dictionary.get(
            'read-aws-environment-ebs-volumes-compliance-stats'
        )
        # Return an object of this model
        return cls(read_aws_environment_ebs_volumes_compliance_stats)
