#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import ebs_backup_links_v1 as ebs_backup_links_v1_

T = TypeVar('T', bound='EBSBackupV1')


class EBSBackupV1:
    """Implementation of the 'EBSBackupV1' model.

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
        browsing_failed_reason:
            The reason that browsing is unavailable for the backup. Possible values include
            "file_limit_exceeded" and
            "browsing_unavailable". If browse indexing is successful, then this field has a
            value of `null`.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        p_id:
            The Clumio-assigned ID of the volume backup.
        is_browsable:
            Determines whether browsing is available for the backup. If `true`, then
            browsing is available for the backup.
        is_encrypted:
            Determines whether the EBS volume backup is encrypted. If `true`, the volume
            backup is encrypted.
        kms_key_native_id:
            The AWS-assigned ID of the KMS key encrypting this EBS volume backup. If the
            volume is not encrypted, this field has a value of `null`.
        size:
            The size of the volume backup. Measured in gigabytes (GB).
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        tags:
            The volume tags applied to the original EBS volume before backup.
        p_type:
            The volume type of the original EBS volume before backup. Possible values
            include `gp2`, `io1`, `st1`, `sc1`, `standard`.
        volume_id:
            The Clumio-assigned ID of the EBS volume associated with the volume backup.
        volume_native_id:
            The AWS-assigned ID of the EBS volume associated with the volume backup.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'browsing_failed_reason': 'browsing_failed_reason',
        'expiration_timestamp': 'expiration_timestamp',
        'p_id': 'id',
        'is_browsable': 'is_browsable',
        'is_encrypted': 'is_encrypted',
        'kms_key_native_id': 'kms_key_native_id',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
        'tags': 'tags',
        'p_type': 'type',
        'volume_id': 'volume_id',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        links: ebs_backup_links_v1_.EBSBackupLinksV1 | None = None,
        account_native_id: str | None = None,
        aws_az: str | None = None,
        aws_region: str | None = None,
        browsing_failed_reason: str | None = None,
        expiration_timestamp: str | None = None,
        p_id: str | None = None,
        is_browsable: bool | None = None,
        is_encrypted: bool | None = None,
        kms_key_native_id: str | None = None,
        size: int | None = None,
        start_timestamp: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        p_type: str | None = None,
        volume_id: str | None = None,
        volume_native_id: str | None = None,
    ) -> None:
        """Constructor for the EBSBackupV1 class."""

        # Initialize members of the class
        self.links: ebs_backup_links_v1_.EBSBackupLinksV1 | None = links
        self.account_native_id: str | None = account_native_id
        self.aws_az: str | None = aws_az
        self.aws_region: str | None = aws_region
        self.browsing_failed_reason: str | None = browsing_failed_reason
        self.expiration_timestamp: str | None = expiration_timestamp
        self.p_id: str | None = p_id
        self.is_browsable: bool | None = is_browsable
        self.is_encrypted: bool | None = is_encrypted
        self.kms_key_native_id: str | None = kms_key_native_id
        self.size: int | None = size
        self.start_timestamp: str | None = start_timestamp
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.p_type: str | None = p_type
        self.volume_id: str | None = volume_id
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
        val = dictionary.get('_links', None)
        val_links = ebs_backup_links_v1_.EBSBackupLinksV1.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('browsing_failed_reason', None)
        val_browsing_failed_reason = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_browsable', None)
        val_is_browsable = val

        val = dictionary.get('is_encrypted', None)
        val_is_encrypted = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('volume_id', None)
        val_volume_id = val

        val = dictionary.get('volume_native_id', None)
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_account_native_id,
            val_aws_az,
            val_aws_region,
            val_browsing_failed_reason,
            val_expiration_timestamp,
            val_p_id,
            val_is_browsable,
            val_is_encrypted,
            val_kms_key_native_id,
            val_size,
            val_start_timestamp,
            val_tags,
            val_p_type,
            val_volume_id,
            val_volume_native_id,
        )
