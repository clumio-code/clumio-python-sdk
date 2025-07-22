#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

T = TypeVar('T', bound='RdsResourceRestoreTarget')


class RdsResourceRestoreTarget:
    """Implementation of the 'RdsResourceRestoreTarget' model.

    The configuration of the RDS resource to be restored.

    Attributes:
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint to fetch valid values.
        instance_class:
            The instance class of the RDS resources to be created. Possible values include
            `db.r5.2xlarge` and `db.t2.small`.
        is_publicly_accessible:
            Designates whether the restored RDS resource also has a public IP address in
            addition to the private IP address.
        kms_key_native_id:
            The AWS-assigned ID of the KMS encryption key used to encrypt data in this RDS
            resource.
        name:
            The name given to the restored RDS resource.
            The name must follow AWS RDS naming conventions:
            https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limi
            ts.Constraints
        option_group_name:
            Option group name to be added to the restored RDS resource.
        parameter_group_name:
            The name of the parameter group to be associated with the restored RDS resource.
        security_group_native_ids:
            The AWS-assigned IDs of the security groups to be associated with the restored
            RDS resource.
        subnet_group_name:
            The AWS-assigned name of the subnet group to be associated with the restored RDS
            resource.
        tags:
            The AWS tags to be applied to the restored instance.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'environment_id': 'environment_id',
        'instance_class': 'instance_class',
        'is_publicly_accessible': 'is_publicly_accessible',
        'kms_key_native_id': 'kms_key_native_id',
        'name': 'name',
        'option_group_name': 'option_group_name',
        'parameter_group_name': 'parameter_group_name',
        'security_group_native_ids': 'security_group_native_ids',
        'subnet_group_name': 'subnet_group_name',
        'tags': 'tags',
    }

    def __init__(
        self,
        environment_id: str,
        instance_class: str,
        is_publicly_accessible: bool,
        kms_key_native_id: str,
        name: str,
        option_group_name: str,
        parameter_group_name: str,
        security_group_native_ids: Sequence[str],
        subnet_group_name: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
    ) -> None:
        """Constructor for the RdsResourceRestoreTarget class."""

        # Initialize members of the class
        self.environment_id: str = environment_id
        self.instance_class: str = instance_class
        self.is_publicly_accessible: bool = is_publicly_accessible
        self.kms_key_native_id: str = kms_key_native_id
        self.name: str = name
        self.option_group_name: str = option_group_name
        self.parameter_group_name: str = parameter_group_name
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.subnet_group_name: str = subnet_group_name
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
        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['instance_class']
        val_instance_class = val

        val = dictionary['is_publicly_accessible']
        val_is_publicly_accessible = val

        val = dictionary['kms_key_native_id']
        val_kms_key_native_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['option_group_name']
        val_option_group_name = val

        val = dictionary['parameter_group_name']
        val_parameter_group_name = val

        val = dictionary['security_group_native_ids']
        val_security_group_native_ids = val

        val = dictionary['subnet_group_name']
        val_subnet_group_name = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            val_environment_id,  # type: ignore
            val_instance_class,  # type: ignore
            val_is_publicly_accessible,  # type: ignore
            val_kms_key_native_id,  # type: ignore
            val_name,  # type: ignore
            val_option_group_name,  # type: ignore
            val_parameter_group_name,  # type: ignore
            val_security_group_native_ids,  # type: ignore
            val_subnet_group_name,  # type: ignore
            val_tags,  # type: ignore
        )
