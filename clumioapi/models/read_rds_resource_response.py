#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
from clumioapi.models import rds_resource_embedded as rds_resource_embedded_
from clumioapi.models import rds_resource_links as rds_resource_links_

T = TypeVar('T', bound='ReadRdsResourceResponse')


class ReadRdsResourceResponse:
    """Implementation of the 'ReadRdsResourceResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with this resource.
        aws_azs:
            The AWS availability zone(s) associated with the resource. For example, `us-
            west-2a`.
        aws_region:
            The AWS region associated with this resource.
        backup_status_info:
            The backup status information applied to this resource.
        deletion_timestamp:
            The timestamp of when the RDS resource was deleted. Represented in RFC-3339
            format.
            If the resource was not deleted, then this field has a value of `null`.
        direct_assignment_policy_id:
            The Clumio-assigned ID of the policy directly assigned to the entity.
        earliest_aws_snapshot_restorable_timestamp:
            The timestamp of the oldest AWS snapshot of the RDS resource. Represented in
            RFC-3339
            format. If the resource has no available snapshots, then this field has a value
            of `null`.
        engine:
            The database engine of the RDS resource. Possible values include `postgres` and
            `mysql`.
            For a full list of possible values, please refer to the AWS documentation at
            https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-
            versions.html
        engine_mode:
            The database engine mode of the RDS resource. Possible values include
            `provisioned`
            and `serverless`.
        engine_version:
            The database engine version of the RDS resource. For example, `10.12`.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with this resource.
        first_clumio_snapshot_timestamp:
            The timestamp of the first active backup of the database to Clumio. Represented
            in RFC-3339 format.
        first_granular_backup_timestamp:
            The timestamp of the first active granular backup for the database. Represented
            in
            RFC-3339 format.
        has_direct_assignment:
            Determines whether the table has a direct assignment.
        p_id:
            The Clumio-assigned ID of the resource.
        is_deleted:
            Determines whether an RDS resource is deleted.
        is_encrypted:
            Determines whether an RDS resource is encrypted.
        is_supported:
            Determines whether the RDS resource is supported for backups.
        kms_key_native_id:
            The AWS-assigned ID of the KMS key encrypting this resource. If the resource is
            unencrypted, then this field has a value of `null`.
        last_clumio_snapshot_timestamp:
            The timestamp of the last time this database was backed up to Clumio.
            Represented
            in RFC-3339 format.
        last_granular_backup_timestamp:
            The timestamp of the last time this database had granular backup performed.
            Represented in RFC-3339 format.
        latest_aws_snapshot_restorable_timestamp:
            The timestamp of the newest AWS snapshot of the RDS resource. Represented in
            RFC-3339
            format. If the resource has no available snapshots, then this field has a value
            of `null`.
        name:
            The AWS-assigned name of the RDS resource. For example, `clumio-aurora-dev`.
        organizational_unit_id:
            The organizational unit to which this resource belongs.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the RDS resource. Possible values include `protected`,
            `unprotected`, and `unsupported`. If the RDS resource does not support backups,
            then
            this field has a value of `unsupported`. If the resource has been deleted, then
            this
            field has a value of `null`.
        resource_native_id:
            The AWS-assigned ID of the RDS resource. For example,
            `cluster-3WW6IXRWO5ZS4PTUIKGZEACISY`.
        security_group_native_ids:
            The AWS-assigned IDs of the security groups associated with this resource
        size:
            The size of the RDS resource. Measured in bytes (B).
        subnet_group_name:
            The RDS subnet group name associated with this resource.
        tags:
            The AWS tags associated with this RDS resource.
        p_type:
            The RDS resource type. Possible values include `aws_rds_cluster` and
            `aws_rds_instance`.
        unsupported_reason:
            The reason why protection is not available on this RDS resource, if any.
            Possible values include `rds_engine_oracle` and `rds_postgres_9_4`.
            If the resource is supported, then this field has a value of `null`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_azs': 'aws_azs',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'deletion_timestamp': 'deletion_timestamp',
        'direct_assignment_policy_id': 'direct_assignment_policy_id',
        'earliest_aws_snapshot_restorable_timestamp': 'earliest_aws_snapshot_restorable_timestamp',
        'engine': 'engine',
        'engine_mode': 'engine_mode',
        'engine_version': 'engine_version',
        'environment_id': 'environment_id',
        'first_clumio_snapshot_timestamp': 'first_clumio_snapshot_timestamp',
        'first_granular_backup_timestamp': 'first_granular_backup_timestamp',
        'has_direct_assignment': 'has_direct_assignment',
        'p_id': 'id',
        'is_deleted': 'is_deleted',
        'is_encrypted': 'is_encrypted',
        'is_supported': 'is_supported',
        'kms_key_native_id': 'kms_key_native_id',
        'last_clumio_snapshot_timestamp': 'last_clumio_snapshot_timestamp',
        'last_granular_backup_timestamp': 'last_granular_backup_timestamp',
        'latest_aws_snapshot_restorable_timestamp': 'latest_aws_snapshot_restorable_timestamp',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'resource_native_id': 'resource_native_id',
        'security_group_native_ids': 'security_group_native_ids',
        'size': 'size',
        'subnet_group_name': 'subnet_group_name',
        'tags': 'tags',
        'p_type': 'type',
        'unsupported_reason': 'unsupported_reason',
    }

    def __init__(
        self,
        embedded: rds_resource_embedded_.RdsResourceEmbedded,
        links: rds_resource_links_.RdsResourceLinks,
        account_native_id: str,
        aws_azs: Sequence[str],
        aws_region: str,
        backup_status_info: backup_status_info_.BackupStatusInfo,
        deletion_timestamp: str,
        direct_assignment_policy_id: str,
        earliest_aws_snapshot_restorable_timestamp: str,
        engine: str,
        engine_mode: str,
        engine_version: str,
        environment_id: str,
        first_clumio_snapshot_timestamp: str,
        first_granular_backup_timestamp: str,
        has_direct_assignment: bool,
        p_id: str,
        is_deleted: bool,
        is_encrypted: bool,
        is_supported: bool,
        kms_key_native_id: str,
        last_clumio_snapshot_timestamp: str,
        last_granular_backup_timestamp: str,
        latest_aws_snapshot_restorable_timestamp: str,
        name: str,
        organizational_unit_id: str,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule,
        protection_status: str,
        resource_native_id: str,
        security_group_native_ids: Sequence[str],
        size: int,
        subnet_group_name: str,
        tags: Sequence[aws_tag_model_.AwsTagModel],
        p_type: str,
        unsupported_reason: str,
    ) -> None:
        """Constructor for the ReadRdsResourceResponse class."""

        # Initialize members of the class
        self.embedded: rds_resource_embedded_.RdsResourceEmbedded = embedded
        self.links: rds_resource_links_.RdsResourceLinks = links
        self.account_native_id: str = account_native_id
        self.aws_azs: Sequence[str] = aws_azs
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo = backup_status_info
        self.deletion_timestamp: str = deletion_timestamp
        self.direct_assignment_policy_id: str = direct_assignment_policy_id
        self.earliest_aws_snapshot_restorable_timestamp: str = (
            earliest_aws_snapshot_restorable_timestamp
        )
        self.engine: str = engine
        self.engine_mode: str = engine_mode
        self.engine_version: str = engine_version
        self.environment_id: str = environment_id
        self.first_clumio_snapshot_timestamp: str = first_clumio_snapshot_timestamp
        self.first_granular_backup_timestamp: str = first_granular_backup_timestamp
        self.has_direct_assignment: bool = has_direct_assignment
        self.p_id: str = p_id
        self.is_deleted: bool = is_deleted
        self.is_encrypted: bool = is_encrypted
        self.is_supported: bool = is_supported
        self.kms_key_native_id: str = kms_key_native_id
        self.last_clumio_snapshot_timestamp: str = last_clumio_snapshot_timestamp
        self.last_granular_backup_timestamp: str = last_granular_backup_timestamp
        self.latest_aws_snapshot_restorable_timestamp: str = (
            latest_aws_snapshot_restorable_timestamp
        )
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.resource_native_id: str = resource_native_id
        self.security_group_native_ids: Sequence[str] = security_group_native_ids
        self.size: int = size
        self.subnet_group_name: str = subnet_group_name
        self.tags: Sequence[aws_tag_model_.AwsTagModel] = tags
        self.p_type: str = p_type
        self.unsupported_reason: str = unsupported_reason

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
        val = dictionary['_embedded']
        val_embedded = rds_resource_embedded_.RdsResourceEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = rds_resource_links_.RdsResourceLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_azs']
        val_aws_azs = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_status_info']
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary['deletion_timestamp']
        val_deletion_timestamp = val

        val = dictionary['direct_assignment_policy_id']
        val_direct_assignment_policy_id = val

        val = dictionary['earliest_aws_snapshot_restorable_timestamp']
        val_earliest_aws_snapshot_restorable_timestamp = val

        val = dictionary['engine']
        val_engine = val

        val = dictionary['engine_mode']
        val_engine_mode = val

        val = dictionary['engine_version']
        val_engine_version = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['first_clumio_snapshot_timestamp']
        val_first_clumio_snapshot_timestamp = val

        val = dictionary['first_granular_backup_timestamp']
        val_first_granular_backup_timestamp = val

        val = dictionary['has_direct_assignment']
        val_has_direct_assignment = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_deleted']
        val_is_deleted = val

        val = dictionary['is_encrypted']
        val_is_encrypted = val

        val = dictionary['is_supported']
        val_is_supported = val

        val = dictionary['kms_key_native_id']
        val_kms_key_native_id = val

        val = dictionary['last_clumio_snapshot_timestamp']
        val_last_clumio_snapshot_timestamp = val

        val = dictionary['last_granular_backup_timestamp']
        val_last_granular_backup_timestamp = val

        val = dictionary['latest_aws_snapshot_restorable_timestamp']
        val_latest_aws_snapshot_restorable_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary['protection_status']
        val_protection_status = val

        val = dictionary['resource_native_id']
        val_resource_native_id = val

        val = dictionary['security_group_native_ids']
        val_security_group_native_ids = val

        val = dictionary['size']
        val_size = val

        val = dictionary['subnet_group_name']
        val_subnet_group_name = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary['type']
        val_p_type = val

        val = dictionary['unsupported_reason']
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_azs,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_status_info,  # type: ignore
            val_deletion_timestamp,  # type: ignore
            val_direct_assignment_policy_id,  # type: ignore
            val_earliest_aws_snapshot_restorable_timestamp,  # type: ignore
            val_engine,  # type: ignore
            val_engine_mode,  # type: ignore
            val_engine_version,  # type: ignore
            val_environment_id,  # type: ignore
            val_first_clumio_snapshot_timestamp,  # type: ignore
            val_first_granular_backup_timestamp,  # type: ignore
            val_has_direct_assignment,  # type: ignore
            val_p_id,  # type: ignore
            val_is_deleted,  # type: ignore
            val_is_encrypted,  # type: ignore
            val_is_supported,  # type: ignore
            val_kms_key_native_id,  # type: ignore
            val_last_clumio_snapshot_timestamp,  # type: ignore
            val_last_granular_backup_timestamp,  # type: ignore
            val_latest_aws_snapshot_restorable_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_protection_status,  # type: ignore
            val_resource_native_id,  # type: ignore
            val_security_group_native_ids,  # type: ignore
            val_size,  # type: ignore
            val_subnet_group_name,  # type: ignore
            val_tags,  # type: ignore
            val_p_type,  # type: ignore
            val_unsupported_reason,  # type: ignore
        )
