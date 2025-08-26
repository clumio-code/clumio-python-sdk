#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
import requests

T = TypeVar('T', bound='RdsResourceRestoreTarget')


@dataclasses.dataclass
class RdsResourceRestoreTarget:
    """Implementation of the 'RdsResourceRestoreTarget' model.

        The configuration of the RDS resource to be restored.

        Attributes:
            EnvironmentId:
                The clumio-assigned id of the aws environment to be used as the restore destination.
    use the [get /datasources/aws/environments](#operation/list-aws-environments) endpoint to fetch valid values.

            InstanceClass:
                The instance class of the rds resources to be created. possible values include `db.r5.2xlarge` and `db.t2.small`.

            IsPubliclyAccessible:
                Designates whether the restored rds resource also has a public ip address in addition to the private ip address.

            KmsKeyNativeId:
                The aws-assigned id of the kms encryption key used to encrypt data in this rds resource.

            Name:
                The name given to the restored rds resource.
    the name must follow aws rds naming conventions:
    https://docs.aws.amazon.com/amazonrds/latest/userguide/chap_limits.html#rds_limits.constraints.

            OptionGroupName:
                Option group name to be added to the restored rds resource.

            ParameterGroupName:
                The name of the parameter group to be associated with the restored rds resource.

            SecurityGroupNativeIds:
                The aws-assigned ids of the security groups to be associated with the restored rds resource.

            SubnetGroupName:
                The aws-assigned name of the subnet group to be associated with the restored rds resource.

            Tags:
                The aws tags to be applied to the restored instance.

    """

    EnvironmentId: str | None = None
    InstanceClass: str | None = None
    IsPubliclyAccessible: bool | None = None
    KmsKeyNativeId: str | None = None
    Name: str | None = None
    OptionGroupName: str | None = None
    ParameterGroupName: str | None = None
    SecurityGroupNativeIds: Sequence[str] | None = None
    SubnetGroupName: str | None = None
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
        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('instance_class', None)
        val_instance_class = val

        val = dictionary.get('is_publicly_accessible', None)
        val_is_publicly_accessible = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('option_group_name', None)
        val_option_group_name = val

        val = dictionary.get('parameter_group_name', None)
        val_parameter_group_name = val

        val = dictionary.get('security_group_native_ids', None)
        val_security_group_native_ids = val

        val = dictionary.get('subnet_group_name', None)
        val_subnet_group_name = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_environment_id,
            val_instance_class,
            val_is_publicly_accessible,
            val_kms_key_native_id,
            val_name,
            val_option_group_name,
            val_parameter_group_name,
            val_security_group_native_ids,
            val_subnet_group_name,
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
