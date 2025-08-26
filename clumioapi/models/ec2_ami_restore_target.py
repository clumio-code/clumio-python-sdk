#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import \
    ec2_restore_ebs_block_device_mapping as ec2_restore_ebs_block_device_mapping_
import requests

T = TypeVar('T', bound='EC2AMIRestoreTarget')


@dataclasses.dataclass
class EC2AMIRestoreTarget:
    """Implementation of the 'EC2AMIRestoreTarget' model.

        The configuration for the restore to AMI.

        Attributes:
            Description:
                The description for the ami.

            EbsBlockDeviceMappings:
                Block device mappings chosen for the ebs volumes being restored.

            EnvironmentId:
                The clumio-assigned id of the aws environment to be used as the restore destination.
    use the [get /datasources/aws/environments](#operation/list-aws-environments) endpoint
    to fetch valid values.

            Name:
                The name for the ami.

            Tags:
                The aws tags to be applied to the restored ami.

    """

    Description: str | None = None
    EbsBlockDeviceMappings: (
        Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
    ) = None
    EnvironmentId: str | None = None
    Name: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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

        val_ebs_block_device_mappings = []
        if val:
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

        val_tags = []
        if val:
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

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
