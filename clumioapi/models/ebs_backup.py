#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import ebs_backup_links

T = TypeVar('T', bound='EBSBackup')


class EBSBackup:
    """Implementation of the 'EBSBackup' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the backup.
        aws_az:
            The availability zone associated with the volume backup. For example, `us-
            west-2a`.
        aws_region:
            The AWS region in which the volume backup resides. For example, `us-west-2`.
        backup_tier:
            Backup Tier
        browsing_failed_reason:
            The reason that browsing is unavailable for the backup. Possible values include
            "file_limit_exceeded" and
            "browsing_unavailable". If browse indexing is successful, then this field has a
            value of `null`.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        p_id:
            The Clumio-assigned ID of the volume backup.
        iops:
            Iops of the volume.
        is_browsable:
            Determines whether browsing is available for the backup. If `true`, then
            browsing is available for the backup.
        is_encrypted:
            Determines whether the EBS volume backup is encrypted. If `true`, the volume
            backup is encrypted.
        kms_key_native_id:
            The AWS-assigned ID of the KMS key encrypting this EBS volume backup. If the
            volume is not encrypted, this field has a value of `null`.
        migration_timestamp:
            The timestamp of when the migration was triggered. This field will be set only
            for
            migration backups. Represented in RFC-3339 format.
        size:
            The size of the volume backup. Measured in gigabytes (GB).
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        tags:
            The volume tags applied to the original EBS volume before backup.
        p_type:
            The type of the backup. Possible values - `clumio_backup`, `aws_snapshot`.
        utilized_size_in_bytes:
            Utilized size
        volume_id:
            The Clumio-assigned ID of the EBS volume associated with the volume backup.
        volume_native_id:
            The AWS-assigned ID of the EBS volume associated with the volume backup.
        volume_type:
            The volume type of the original EBS volume before backup. Possible values
            include `gp2`, `io1`, `st1`, `sc1`, `standard`.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'backup_tier': 'backup_tier',
        'browsing_failed_reason': 'browsing_failed_reason',
        'expiration_timestamp': 'expiration_timestamp',
        'p_id': 'id',
        'iops': 'iops',
        'is_browsable': 'is_browsable',
        'is_encrypted': 'is_encrypted',
        'kms_key_native_id': 'kms_key_native_id',
        'migration_timestamp': 'migration_timestamp',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
        'tags': 'tags',
        'p_type': 'type',
        'utilized_size_in_bytes': 'utilized_size_in_bytes',
        'volume_id': 'volume_id',
        'volume_native_id': 'volume_native_id',
        'volume_type': 'volume_type',
    }

    def __init__(
        self,
        links: ebs_backup_links.EBSBackupLinks = None,
        account_native_id: str = None,
        aws_az: str = None,
        aws_region: str = None,
        backup_tier: str = None,
        browsing_failed_reason: str = None,
        expiration_timestamp: str = None,
        p_id: str = None,
        iops: int = None,
        is_browsable: bool = None,
        is_encrypted: bool = None,
        kms_key_native_id: str = None,
        migration_timestamp: str = None,
        size: int = None,
        start_timestamp: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        p_type: str = None,
        utilized_size_in_bytes: int = None,
        volume_id: str = None,
        volume_native_id: str = None,
        volume_type: str = None,
    ) -> None:
        """Constructor for the EBSBackup class."""

        # Initialize members of the class
        self.links: ebs_backup_links.EBSBackupLinks = links
        self.account_native_id: str = account_native_id
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.backup_tier: str = backup_tier
        self.browsing_failed_reason: str = browsing_failed_reason
        self.expiration_timestamp: str = expiration_timestamp
        self.p_id: str = p_id
        self.iops: int = iops
        self.is_browsable: bool = is_browsable
        self.is_encrypted: bool = is_encrypted
        self.kms_key_native_id: str = kms_key_native_id
        self.migration_timestamp: str = migration_timestamp
        self.size: int = size
        self.start_timestamp: str = start_timestamp
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.p_type: str = p_type
        self.utilized_size_in_bytes: int = utilized_size_in_bytes
        self.volume_id: str = volume_id
        self.volume_native_id: str = volume_native_id
        self.volume_type: str = volume_type

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
        key = '_links'
        links = (
            ebs_backup_links.EBSBackupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_az = dictionary.get('aws_az')
        aws_region = dictionary.get('aws_region')
        backup_tier = dictionary.get('backup_tier')
        browsing_failed_reason = dictionary.get('browsing_failed_reason')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        p_id = dictionary.get('id')
        iops = dictionary.get('iops')
        is_browsable = dictionary.get('is_browsable')
        is_encrypted = dictionary.get('is_encrypted')
        kms_key_native_id = dictionary.get('kms_key_native_id')
        migration_timestamp = dictionary.get('migration_timestamp')
        size = dictionary.get('size')
        start_timestamp = dictionary.get('start_timestamp')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        p_type = dictionary.get('type')
        utilized_size_in_bytes = dictionary.get('utilized_size_in_bytes')
        volume_id = dictionary.get('volume_id')
        volume_native_id = dictionary.get('volume_native_id')
        volume_type = dictionary.get('volume_type')
        # Return an object of this model
        return cls(
            links,
            account_native_id,
            aws_az,
            aws_region,
            backup_tier,
            browsing_failed_reason,
            expiration_timestamp,
            p_id,
            iops,
            is_browsable,
            is_encrypted,
            kms_key_native_id,
            migration_timestamp,
            size,
            start_timestamp,
            tags,
            p_type,
            utilized_size_in_bytes,
            volume_id,
            volume_native_id,
            volume_type,
        )
