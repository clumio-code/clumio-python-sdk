#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ebs_volume_embedded as ebs_volume_embedded_
from clumioapi.models import ebs_volume_links as ebs_volume_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_

T = TypeVar('T', bound='ReadEbsVolumeResponse')


class ReadEbsVolumeResponse:
    """Implementation of the 'ReadEbsVolumeResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the EBS volume.
        aws_az:
            The AWS availability zone in which the EBS volume resides. For example,
            `us-west-2a`.
        aws_region:
            The AWS region associated with the EBS volume.
        backup_status_info:
            The backup status information applied to this resource.
        deletion_timestamp:
            The timestamp of when the volume was deleted. Represented in RFC-3339 format. If
            this volume has not been deleted, then this field has a value of `null`.
        direct_assignment_policy_id:
            The Clumio-assigned ID of the policy directly assigned to the entity.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the EBS volume.
        has_direct_assignment:
            Determines whether the table has a direct assignment.
        p_id:
            The Clumio-assigned ID of the EBS volume.
        iops:
            Iops of the volume.
        is_deleted:
            Determines whether the EBS volume has been deleted. If `true`, the volume has
            been
            deleted.
        is_encrypted:
            Determines whether the EBS volume is encrypted. If `true`, the volume is
            encrypted.
        is_supported:
            Determines whether the EBS volume is supported for backups.
        kms_key_native_id:
            The AWS-assigned ID of the KMS key encrypting the EBS volume. If the volume is
            unencrypted, then this field has a value of `null`.
        last_backup_timestamp:
            The timestamp of the most recent backup of the EBS volume. Represented in
            RFC-3339
            format. If the volume has never been backed up, then this field has a value of
            `null`.
        last_snapshot_timestamp:
            The timestamp of the most recent snapshot of the EBS volume taken as part of
            Snapshot Manager. Represented in RFC-3339 format. If the volume has never been
            snapshotted, then this field has a value of `null`.
        name:
            The AWS-assigned name of the EBS volume.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the EBS
            volume.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the EBS volume. Possible values include "protected",
            "unprotected", and "unsupported". If the EBS volume does not support backups,
            then
            this field has a value of `unsupported`. If the volume has been deleted, then
            this
            field has a value of `null`.
        size:
            The size of the EBS volume. Measured in bytes (B).
        tags:
            The AWS tags applied to the EBS volume.
        p_type:
            The type of EBS volume. Possible values include "gp2", "io1", "st1", "sc1", and
            "standard".
        unsupported_reason:
            The reason why protection is not available. If the volume is supported, then
            this
            field has a value of `null`.
        volume_native_id:
            The AWS-assigned ID of the EBS volume.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'deletion_timestamp': 'deletion_timestamp',
        'direct_assignment_policy_id': 'direct_assignment_policy_id',
        'environment_id': 'environment_id',
        'has_direct_assignment': 'has_direct_assignment',
        'p_id': 'id',
        'iops': 'iops',
        'is_deleted': 'is_deleted',
        'is_encrypted': 'is_encrypted',
        'is_supported': 'is_supported',
        'kms_key_native_id': 'kms_key_native_id',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_snapshot_timestamp': 'last_snapshot_timestamp',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'size': 'size',
        'tags': 'tags',
        'p_type': 'type',
        'unsupported_reason': 'unsupported_reason',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        embedded: ebs_volume_embedded_.EbsVolumeEmbedded | None = None,
        links: ebs_volume_links_.EbsVolumeLinks | None = None,
        account_native_id: str | None = None,
        aws_az: str | None = None,
        aws_region: str | None = None,
        backup_status_info: backup_status_info_.BackupStatusInfo | None = None,
        deletion_timestamp: str | None = None,
        direct_assignment_policy_id: str | None = None,
        environment_id: str | None = None,
        has_direct_assignment: bool | None = None,
        p_id: str | None = None,
        iops: int | None = None,
        is_deleted: bool | None = None,
        is_encrypted: bool | None = None,
        is_supported: bool | None = None,
        kms_key_native_id: str | None = None,
        last_backup_timestamp: str | None = None,
        last_snapshot_timestamp: str | None = None,
        name: str | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = None,
        protection_status: str | None = None,
        size: int | None = None,
        tags: Sequence[aws_tag_model_.AwsTagModel] | None = None,
        p_type: str | None = None,
        unsupported_reason: str | None = None,
        volume_native_id: str | None = None,
    ) -> None:
        """Constructor for the ReadEbsVolumeResponse class."""

        # Initialize members of the class
        self.embedded: ebs_volume_embedded_.EbsVolumeEmbedded | None = embedded
        self.links: ebs_volume_links_.EbsVolumeLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_az: str | None = aws_az
        self.aws_region: str | None = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo | None = backup_status_info
        self.deletion_timestamp: str | None = deletion_timestamp
        self.direct_assignment_policy_id: str | None = direct_assignment_policy_id
        self.environment_id: str | None = environment_id
        self.has_direct_assignment: bool | None = has_direct_assignment
        self.p_id: str | None = p_id
        self.iops: int | None = iops
        self.is_deleted: bool | None = is_deleted
        self.is_encrypted: bool | None = is_encrypted
        self.is_supported: bool | None = is_supported
        self.kms_key_native_id: str | None = kms_key_native_id
        self.last_backup_timestamp: str | None = last_backup_timestamp
        self.last_snapshot_timestamp: str | None = last_snapshot_timestamp
        self.name: str | None = name
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule | None = (
            protection_info
        )
        self.protection_status: str | None = protection_status
        self.size: int | None = size
        self.tags: Sequence[aws_tag_model_.AwsTagModel] | None = tags
        self.p_type: str | None = p_type
        self.unsupported_reason: str | None = unsupported_reason
        self.volume_native_id: str | None = volume_native_id

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
        val_embedded = ebs_volume_embedded_.EbsVolumeEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ebs_volume_links_.EbsVolumeLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('deletion_timestamp', None)
        val_deletion_timestamp = val

        val = dictionary.get('direct_assignment_policy_id', None)
        val_direct_assignment_policy_id = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('has_direct_assignment', None)
        val_has_direct_assignment = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('iops', None)
        val_iops = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_encrypted', None)
        val_is_encrypted = val

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_snapshot_timestamp', None)
        val_last_snapshot_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('size', None)
        val_size = val

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

        val = dictionary.get('volume_native_id', None)
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_az,
            val_aws_region,
            val_backup_status_info,
            val_deletion_timestamp,
            val_direct_assignment_policy_id,
            val_environment_id,
            val_has_direct_assignment,
            val_p_id,
            val_iops,
            val_is_deleted,
            val_is_encrypted,
            val_is_supported,
            val_kms_key_native_id,
            val_last_backup_timestamp,
            val_last_snapshot_timestamp,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_size,
            val_tags,
            val_p_type,
            val_unsupported_reason,
            val_volume_native_id,
        )
