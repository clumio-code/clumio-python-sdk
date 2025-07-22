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
        description: str,
        ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping
        ],
        environment_id: str,
        name: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
    ) -> None:
        """Constructor for the EC2AMIRestoreTarget class."""

        # Initialize members of the class
        self.description: str = description
        self.ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping
        ] = ebs_block_device_mappings
        self.environment_id: str = environment_id
        self.name: str = name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] = tags

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
        val = dictionary['description']
        val_description = val

        val = dictionary['ebs_block_device_mappings']

        val_ebs_block_device_mappings = None
        if val:
            val_ebs_block_device_mappings = list()
            for value in val:
                val_ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_description,  # type: ignore
            val_ebs_block_device_mappings,  # type: ignore
            val_environment_id,  # type: ignore
            val_name,  # type: ignore
            val_tags,  # type: ignore
        )
