#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

T = TypeVar('T', bound='EBSRestoreTargetV1')


class EBSRestoreTargetV1:
    """Implementation of the 'EBSRestoreTargetV1' model.

    The configuration of the EBS volume to be restored.

    Attributes:
        aws_az:
            The availability zone into which the EBS volume is restored. For example, `us-
            west-2a`.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint to fetch valid values.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination. Use the [GET /datasources/aws/environments](#operation/list-aws-
            environments) endpoint to fetch valid values.
        kms_key_native_id:
            The KMS encryption key ID used to encrypt the EBS volume data. The KMS
            encryption key ID is stored in the AWS cloud as part of your AWS account.
        tags:
            The AWS tags to be applied to the restored volume. The tags are stored in the
            AWS cloud as part of your AWS account.
            An EBS volume can be have multiple tags. The target volume will not inherit any
            tags that were applied
            to the original volume. To find the tags that were applied to the original
            volume,
            use the [GET /backups/aws/ebs-volumes](#operation/list-aws-ebs-volumes) endpoint
            to display the original volume's tag keys (`tags.key`) and tag values
            (`tags.value`).
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'aws_az': 'aws_az',
        'environment_id': 'environment_id',
        'kms_key_native_id': 'kms_key_native_id',
        'tags': 'tags',
    }

    def __init__(
        self,
        aws_az: str,
        environment_id: str,
        kms_key_native_id: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
    ) -> None:
        """Constructor for the EBSRestoreTargetV1 class."""

        # Initialize members of the class
        self.aws_az: str = aws_az
        self.environment_id: str = environment_id
        self.kms_key_native_id: str = kms_key_native_id
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
        val = dictionary['aws_az']
        val_aws_az = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['kms_key_native_id']
        val_kms_key_native_id = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_aws_az,  # type: ignore
            val_environment_id,  # type: ignore
            val_kms_key_native_id,  # type: ignore
            val_tags,  # type: ignore
        )
