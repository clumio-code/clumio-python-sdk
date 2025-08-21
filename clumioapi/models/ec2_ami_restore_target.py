#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import \
    ec2_restore_ebs_block_device_mapping as ec2_restore_ebs_block_device_mapping_

T = TypeVar('T', bound='EC2AMIRestoreTarget')


class EC2AMIRestoreTarget:
    """Implementation of the 'EC2AMIRestoreTarget' model.

    The configuration for the restore to AMI.

    Attributes:
        description:
            The description for the AMI.
        ebs_block_device_mappings:
            Block device mappings chosen for the EBS volumes being restored.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint
            to fetch valid values.
        name:
            The name for the AMI.
        tags:
            The AWS tags to be applied to the restored AMI.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'description': 'description',
        'ebs_block_device_mappings': 'ebs_block_device_mappings',
        'environment_id': 'environment_id',
        'name': 'name',
        'tags': 'tags',
    }

    def __init__(
        self,
        description: str | None = None,
        ebs_block_device_mappings: (
            Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
        ) = None,
        environment_id: str | None = None,
        name: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
    ) -> None:
        """Constructor for the EC2AMIRestoreTarget class."""

        # Initialize members of the class
        self.description: str | None = description
        self.ebs_block_device_mappings: (
            Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
        ) = ebs_block_device_mappings
        self.environment_id: str | None = environment_id
        self.name: str | None = name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags

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
        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('ebs_block_device_mappings', None)

        val_ebs_block_device_mappings = None
        if val:
            val_ebs_block_device_mappings = list()
            for value in val:
                val_ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_description,
            val_ebs_block_device_mappings,
            val_environment_id,
            val_name,
            val_tags,
        )
