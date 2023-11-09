#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model

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
            Option group name to be added to the restored RDS resource
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
    _names = {
        'environment_id': 'environment_id',
        'instance_class': 'instance_class',
        'is_publicly_accessible': 'is_publicly_accessible',
        'kms_key_native_id': 'kms_key_native_id',
        'name': 'name',
        'option_group_name': 'option_group_name',
        'security_group_native_ids': 'security_group_native_ids',
        'subnet_group_name': 'subnet_group_name',
        'tags': 'tags',
    }

    def __init__(
        self,
        environment_id: str = None,
        instance_class: str = None,
        is_publicly_accessible: bool = None,
        kms_key_native_id: str = None,
        name: str = None,
        option_group_name: str = None,
        security_group_native_ids: Sequence[str] = None,
        subnet_group_name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
    ) -> None:
        """Constructor for the RdsResourceRestoreTarget class."""

        # Initialize members of the class
        self.environment_id: str = environment_id
        self.instance_class: str = instance_class
        self.is_publicly_accessible: bool = is_publicly_accessible
        self.kms_key_native_id: str = kms_key_native_id
        self.name: str = name
        self.option_group_name: str = option_group_name
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.subnet_group_name: str = subnet_group_name
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
        environment_id = dictionary.get('environment_id')
        instance_class = dictionary.get('instance_class')
        is_publicly_accessible = dictionary.get('is_publicly_accessible')
        kms_key_native_id = dictionary.get('kms_key_native_id')
        name = dictionary.get('name')
        option_group_name = dictionary.get('option_group_name')
        security_group_native_ids = dictionary.get('security_group_native_ids')
        subnet_group_name = dictionary.get('subnet_group_name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        # Return an object of this model
        return cls(
            environment_id,
            instance_class,
            is_publicly_accessible,
            kms_key_native_id,
            name,
            option_group_name,
            security_group_native_ids,
            subnet_group_name,
            tags,
        )
