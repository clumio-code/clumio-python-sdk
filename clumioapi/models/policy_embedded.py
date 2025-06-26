#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='PolicyEmbedded')


class PolicyEmbedded:
    """Implementation of the 'PolicyEmbedded' model.

    If the `embed` query parameter is set, displays the responses of the related
    resource,as defined by the embeddable link specified.

    Attributes:
        read_policy_aws_ebs_volumes_protection_stats:
            Embeds the EBS protection statistics into the response.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'read_policy_aws_ebs_volumes_protection_stats': 'read-policy-aws-ebs-volumes-protection-stats'
    }

    def __init__(self, read_policy_aws_ebs_volumes_protection_stats: object = None) -> None:
        """Constructor for the PolicyEmbedded class."""

        # Initialize members of the class
        self.read_policy_aws_ebs_volumes_protection_stats: object = (
            read_policy_aws_ebs_volumes_protection_stats
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
        read_policy_aws_ebs_volumes_protection_stats = dictionary.get(
            'read-policy-aws-ebs-volumes-protection-stats'
        )
        # Return an object of this model
        return cls(read_policy_aws_ebs_volumes_protection_stats)
