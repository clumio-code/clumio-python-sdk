#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AwsTagEmbedded')


class AwsTagEmbedded:
    """Implementation of the 'AwsTagEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_aws_environment_tag_backup_status_stats:
            Backup statistics for each tag.
        read_aws_environment_tag_ebs_volumes_protection_stats:

        read_policy_definition:
            Embeds the associated policy of a protected resource in the response if
            requested using the `embed` query parameter. Unprotected resources will not have
            an associated policy.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_aws_environment_tag_backup_status_stats': 'read-aws-environment-tag-backup-status-stats',
        'read_aws_environment_tag_ebs_volumes_protection_stats': 'read-aws-environment-tag-ebs-volumes-protection-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        read_aws_environment_tag_backup_status_stats: object | None = None,
        read_aws_environment_tag_ebs_volumes_protection_stats: object | None = None,
        read_policy_definition: object | None = None,
    ) -> None:
        """Constructor for the AwsTagEmbedded class."""

        # Initialize members of the class
        self.read_aws_environment_tag_backup_status_stats: object | None = (
            read_aws_environment_tag_backup_status_stats
        )
        self.read_aws_environment_tag_ebs_volumes_protection_stats: object | None = (
            read_aws_environment_tag_ebs_volumes_protection_stats
        )
        self.read_policy_definition: object | None = read_policy_definition

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
        val = dictionary.get('read-aws-environment-tag-backup-status-stats', None)
        val_read_aws_environment_tag_backup_status_stats = val

        val = dictionary.get('read-aws-environment-tag-ebs-volumes-protection-stats', None)
        val_read_aws_environment_tag_ebs_volumes_protection_stats = val

        val = dictionary.get('read-policy-definition', None)
        val_read_policy_definition = val

        # Return an object of this model
        return cls(
            val_read_aws_environment_tag_backup_status_stats,
            val_read_aws_environment_tag_ebs_volumes_protection_stats,
            val_read_policy_definition,
        )
