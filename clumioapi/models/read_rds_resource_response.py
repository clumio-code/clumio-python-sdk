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
        embedded: rds_resource_embedded_.RdsResourceEmbedded | None = None,
        links: rds_resource_links_.RdsResourceLinks | None = None,
        account_native_id: str | None = None,
        aws_azs: Sequence[str] | None = None,
        aws_region: str | None = None,
        backup_status_info: backup_status_info_.BackupStatusInfo | None = None,
        deletion_timestamp: str | None = None,
        direct_assignment_policy_id: str | None = None,
        earliest_aws_snapshot_restorable_timestamp: str | None = None,
        engine: str | None = None,
        engine_mode: str | None = None,
        engine_version: str | None = None,
        environment_id: str | None = None,
        first_clumio_snapshot_timestamp: str | None = None,
        first_granular_backup_timestamp: str | None = None,
        has_direct_assignment: bool | None = None,
        p_id: str | None = None,
        is_deleted: bool | None = None,
        is_encrypted: bool | None = None,
        is_supported: bool | None = None,
        kms_key_native_id: str | None = None,
        last_clumio_snapshot_timestamp: str | None = None,
        last_granular_backup_timestamp: str | None = None,
        latest_aws_snapshot_restorable_timestamp: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = None,
        protection_status: str | None = None,
        resource_native_id: str | None = None,
        security_group_native_ids: Sequence[str] | None = None,
        size: int | None = None,
        subnet_group_name: str | None = None,
        tags: Sequence[aws_tag_model_.AwsTagModel] | None = None,
        p_type: str | None = None,
        unsupported_reason: str | None = None,
    ) -> None:
        """Constructor for the ReadRdsResourceResponse class."""

        # Initialize members of the class
        self.embedded: rds_resource_embedded_.RdsResourceEmbedded | None = embedded
        self.links: rds_resource_links_.RdsResourceLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_azs: Sequence[str] | None = aws_azs
        self.aws_region: str | None = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo | None = backup_status_info
        self.deletion_timestamp: str | None = deletion_timestamp
        self.direct_assignment_policy_id: str | None = direct_assignment_policy_id
        self.earliest_aws_snapshot_restorable_timestamp: str | None = (
            earliest_aws_snapshot_restorable_timestamp
        )
        self.engine: str | None = engine
        self.engine_mode: str | None = engine_mode
        self.engine_version: str | None = engine_version
        self.environment_id: str | None = environment_id
        self.first_clumio_snapshot_timestamp: str | None = first_clumio_snapshot_timestamp
        self.first_granular_backup_timestamp: str | None = first_granular_backup_timestamp
        self.has_direct_assignment: bool | None = has_direct_assignment
        self.p_id: str | None = p_id
        self.is_deleted: bool | None = is_deleted
        self.is_encrypted: bool | None = is_encrypted
        self.is_supported: bool | None = is_supported
        self.kms_key_native_id: str | None = kms_key_native_id
        self.last_clumio_snapshot_timestamp: str | None = last_clumio_snapshot_timestamp
        self.last_granular_backup_timestamp: str | None = last_granular_backup_timestamp
        self.latest_aws_snapshot_restorable_timestamp: str | None = (
            latest_aws_snapshot_restorable_timestamp
        )
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = (
            protection_info
        )
        self.protection_status: str | None = protection_status
        self.resource_native_id: str | None = resource_native_id
        self.security_group_native_ids: Sequence[str] | None = security_group_native_ids
        self.size: int | None = size
        self.subnet_group_name: str | None = subnet_group_name
        self.tags: Sequence[aws_tag_model_.AwsTagModel] | None = tags
        self.p_type: str | None = p_type
        self.unsupported_reason: str | None = unsupported_reason

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
        val = dictionary.get('_embedded', None)
        val_embedded = rds_resource_embedded_.RdsResourceEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = rds_resource_links_.RdsResourceLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_azs', None)
        val_aws_azs = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('deletion_timestamp', None)
        val_deletion_timestamp = val

        val = dictionary.get('direct_assignment_policy_id', None)
        val_direct_assignment_policy_id = val

        val = dictionary.get('earliest_aws_snapshot_restorable_timestamp', None)
        val_earliest_aws_snapshot_restorable_timestamp = val

        val = dictionary.get('engine', None)
        val_engine = val

        val = dictionary.get('engine_mode', None)
        val_engine_mode = val

        val = dictionary.get('engine_version', None)
        val_engine_version = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('first_clumio_snapshot_timestamp', None)
        val_first_clumio_snapshot_timestamp = val

        val = dictionary.get('first_granular_backup_timestamp', None)
        val_first_granular_backup_timestamp = val

        val = dictionary.get('has_direct_assignment', None)
        val_has_direct_assignment = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_encrypted', None)
        val_is_encrypted = val

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('last_clumio_snapshot_timestamp', None)
        val_last_clumio_snapshot_timestamp = val

        val = dictionary.get('last_granular_backup_timestamp', None)
        val_last_granular_backup_timestamp = val

        val = dictionary.get('latest_aws_snapshot_restorable_timestamp', None)
        val_latest_aws_snapshot_restorable_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('resource_native_id', None)
        val_resource_native_id = val

        val = dictionary.get('security_group_native_ids', None)
        val_security_group_native_ids = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('subnet_group_name', None)
        val_subnet_group_name = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_azs,
            val_aws_region,
            val_backup_status_info,
            val_deletion_timestamp,
            val_direct_assignment_policy_id,
            val_earliest_aws_snapshot_restorable_timestamp,
            val_engine,
            val_engine_mode,
            val_engine_version,
            val_environment_id,
            val_first_clumio_snapshot_timestamp,
            val_first_granular_backup_timestamp,
            val_has_direct_assignment,
            val_p_id,
            val_is_deleted,
            val_is_encrypted,
            val_is_supported,
            val_kms_key_native_id,
            val_last_clumio_snapshot_timestamp,
            val_last_granular_backup_timestamp,
            val_latest_aws_snapshot_restorable_timestamp,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_resource_native_id,
            val_security_group_native_ids,
            val_size,
            val_subnet_group_name,
            val_tags,
            val_p_type,
            val_unsupported_reason,
        )
