#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
from clumioapi.models import rds_resource_embedded as rds_resource_embedded_
from clumioapi.models import rds_resource_links as rds_resource_links_
import requests

T = TypeVar('T', bound='ReadRdsResourceResponse')


@dataclasses.dataclass
class ReadRdsResourceResponse:
    """Implementation of the 'ReadRdsResourceResponse' model.

        Attributes:
            Embedded:
                Embedded responses related to the resource.

            Links:
                Urls to pages related to the resource.

            AccountNativeId:
                The aws-assigned id of the account associated with this resource.

            AwsAzs:
                The aws availability zone(s) associated with the resource. for example, `us-west-2a`.

            AwsRegion:
                The aws region associated with this resource.

            BackupStatusInfo:
                The backup status information applied to this resource.

            DeletionTimestamp:
                The timestamp of when the rds resource was deleted. represented in rfc-3339 format.
    if the resource was not deleted, then this field has a value of `null`.

            DirectAssignmentPolicyId:
                The clumio-assigned id of the policy directly assigned to the entity.

            EarliestAwsSnapshotRestorableTimestamp:
                The timestamp of the oldest aws snapshot of the rds resource. represented in rfc-3339
    format. if the resource has no available snapshots, then this field has a value of `null`.

            Engine:
                The database engine of the rds resource. possible values include `postgres` and `mysql`.
    for a full list of possible values, please refer to the aws documentation at
    https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html.

            EngineMode:
                The database engine mode of the rds resource. possible values include `provisioned`
    and `serverless`.

            EngineVersion:
                The database engine version of the rds resource. for example, `10.12`.

            EnvironmentId:
                The clumio-assigned id of the aws environment associated with this resource.

            FirstClumioSnapshotTimestamp:
                The timestamp of the first active backup of the database to clumio. represented
    in rfc-3339 format.

            FirstGranularBackupTimestamp:
                The timestamp of the first active granular backup for the database. represented in
    rfc-3339 format.

            HasDirectAssignment:
                Determines whether the table has a direct assignment.

            Id:
                The clumio-assigned id of the resource.

            IsDeleted:
                Determines whether an rds resource is deleted.

            IsEncrypted:
                Determines whether an rds resource is encrypted.

            IsSupported:
                Determines whether the rds resource is supported for backups.

            KmsKeyNativeId:
                The aws-assigned id of the kms key encrypting this resource. if the resource is
    unencrypted, then this field has a value of `null`.

            LastClumioSnapshotTimestamp:
                The timestamp of the last time this database was backed up to clumio. represented
    in rfc-3339 format.

            LastGranularBackupTimestamp:
                The timestamp of the last time this database had granular backup performed.
    represented in rfc-3339 format.

            LatestAwsSnapshotRestorableTimestamp:
                The timestamp of the newest aws snapshot of the rds resource. represented in rfc-3339
    format. if the resource has no available snapshots, then this field has a value of `null`.

            Name:
                The aws-assigned name of the rds resource. for example, `clumio-aurora-dev`.

            OrganizationalUnitId:
                The organizational unit to which this resource belongs.

            ProtectionInfo:
                The protection policy applied to this resource. if the resource is not protected, then this field has a value of `null`.

            ProtectionStatus:
                The protection status of the rds resource. possible values include `protected`,
    `unprotected`, and `unsupported`. if the rds resource does not support backups, then
    this field has a value of `unsupported`. if the resource has been deleted, then this
    field has a value of `null`.

            ResourceNativeId:
                The aws-assigned id of the rds resource. for example, `cluster-3ww6ixrwo5zs4ptuikgzeacisy`.

            SecurityGroupNativeIds:
                The aws-assigned ids of the security groups associated with this resource.

            Size:
                The size of the rds resource. measured in bytes (b).

            SubnetGroupName:
                The rds subnet group name associated with this resource.

            Tags:
                The aws tags associated with this rds resource.

            Type:
                The rds resource type. possible values include `aws_rds_cluster` and `aws_rds_instance`.

            UnsupportedReason:
                The reason why protection is not available on this rds resource, if any.
    possible values include `rds_engine_oracle` and `rds_postgres_9_4`.
    if the resource is supported, then this field has a value of `null`.

    """

    Embedded: rds_resource_embedded_.RdsResourceEmbedded | None = None
    Links: rds_resource_links_.RdsResourceLinks | None = None
    AccountNativeId: str | None = None
    AwsAzs: Sequence[str] | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    DeletionTimestamp: str | None = None
    DirectAssignmentPolicyId: str | None = None
    EarliestAwsSnapshotRestorableTimestamp: str | None = None
    Engine: str | None = None
    EngineMode: str | None = None
    EngineVersion: str | None = None
    EnvironmentId: str | None = None
    FirstClumioSnapshotTimestamp: str | None = None
    FirstGranularBackupTimestamp: str | None = None
    HasDirectAssignment: bool | None = None
    Id: str | None = None
    IsDeleted: bool | None = None
    IsEncrypted: bool | None = None
    IsSupported: bool | None = None
    KmsKeyNativeId: str | None = None
    LastClumioSnapshotTimestamp: str | None = None
    LastGranularBackupTimestamp: str | None = None
    LatestAwsSnapshotRestorableTimestamp: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStatus: str | None = None
    ResourceNativeId: str | None = None
    SecurityGroupNativeIds: Sequence[str] | None = None
    Size: int | None = None
    SubnetGroupName: str | None = None
    Tags: Sequence[aws_tag_model_.AwsTagModel] | None = None
    Type: str | None = None
    UnsupportedReason: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val_id = val

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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
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
            val_type,
            val_unsupported_reason,
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
        model_instance.raw_response = response
        return model_instance
