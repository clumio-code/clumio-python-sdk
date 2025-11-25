#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
import requests

T = TypeVar('T', bound='EBSRestoreTargetV1')


@dataclasses.dataclass
class EBSRestoreTargetV1:
    """Implementation of the 'EBSRestoreTargetV1' model.

    The configuration of the EBS volume to be restored.

    Attributes:
        AwsAz:
            The availability zone into which the ebs volume is restored. for example, `us-
            west-2a`.
            use the [get /datasources/aws/environments](#operation/list-aws-environments)
            endpoint to fetch valid values.

        EnvironmentId:
            The clumio-assigned id of the aws environment to be used as the restore
            destination. use the [get /datasources/aws/environments](#operation/list-aws-
            environments) endpoint to fetch valid values.

        KmsKeyNativeId:
            The kms encryption key id used to encrypt the ebs volume data. the kms
            encryption key id is stored in the aws cloud as part of your aws account.

        Tags:
            The aws tags to be applied to the restored volume. the tags are stored in the
            aws cloud as part of your aws account.
            an ebs volume can be have multiple tags. the target volume will not inherit any
            tags that were applied
            to the original volume. to find the tags that were applied to the original
            volume,
            use the [get /backups/aws/ebs-volumes](#operation/list-aws-ebs-volumes) endpoint
            to display the original volume's tag keys (`tags.key`) and tag values
            (`tags.value`).

    """

    AwsAz: str | None = None
    EnvironmentId: str | None = None
    KmsKeyNativeId: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_aws_az,
            val_environment_id,
            val_kms_key_native_id,
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
