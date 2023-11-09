#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import ec2_restore_ebs_block_device_mapping

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
    _names = {
        'description': 'description',
        'ebs_block_device_mappings': 'ebs_block_device_mappings',
        'environment_id': 'environment_id',
        'name': 'name',
        'tags': 'tags',
    }

    def __init__(
        self,
        description: str = None,
        ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = None,
        environment_id: str = None,
        name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
    ) -> None:
        """Constructor for the EC2AMIRestoreTarget class."""

        # Initialize members of the class
        self.description: str = description
        self.ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = ebs_block_device_mappings
        self.environment_id: str = environment_id
        self.name: str = name
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags

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
        description = dictionary.get('description')
        ebs_block_device_mappings = None
        if dictionary.get('ebs_block_device_mappings'):
            ebs_block_device_mappings = list()
            for value in dictionary.get('ebs_block_device_mappings'):
                ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        environment_id = dictionary.get('environment_id')
        name = dictionary.get('name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(description, ebs_block_device_mappings, environment_id, name, tags)
