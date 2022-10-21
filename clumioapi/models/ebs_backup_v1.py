#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model, ebs_backup_links_v1

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
        id:
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
        type:
            The volume type of the original EBS volume before backup. Possible values
            include `gp2`, `io1`, `st1`, `sc1`, `standard`.
        volume_id:
            The Clumio-assigned ID of the EBS volume associated with the volume backup.
        volume_native_id:
            The AWS-assigned ID of the EBS volume associated with the volume backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'browsing_failed_reason': 'browsing_failed_reason',
        'expiration_timestamp': 'expiration_timestamp',
        'id': 'id',
        'is_browsable': 'is_browsable',
        'is_encrypted': 'is_encrypted',
        'kms_key_native_id': 'kms_key_native_id',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
        'tags': 'tags',
        'type': 'type',
        'volume_id': 'volume_id',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        links: ebs_backup_links_v1.EBSBackupLinksV1 = None,
        account_native_id: str = None,
        aws_az: str = None,
        aws_region: str = None,
        browsing_failed_reason: str = None,
        expiration_timestamp: str = None,
        id: str = None,
        is_browsable: bool = None,
        is_encrypted: bool = None,
        kms_key_native_id: str = None,
        size: int = None,
        start_timestamp: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        type: str = None,
        volume_id: str = None,
        volume_native_id: str = None,
    ) -> None:
        """Constructor for the EBSBackupV1 class."""

        # Initialize members of the class
        self.links: ebs_backup_links_v1.EBSBackupLinksV1 = links
        self.account_native_id: str = account_native_id
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.browsing_failed_reason: str = browsing_failed_reason
        self.expiration_timestamp: str = expiration_timestamp
        self.id: str = id
        self.is_browsable: bool = is_browsable
        self.is_encrypted: bool = is_encrypted
        self.kms_key_native_id: str = kms_key_native_id
        self.size: int = size
        self.start_timestamp: str = start_timestamp
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.type: str = type
        self.volume_id: str = volume_id
        self.volume_native_id: str = volume_native_id

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
            ebs_backup_links_v1.EBSBackupLinksV1.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_az = dictionary.get('aws_az')
        aws_region = dictionary.get('aws_region')
        browsing_failed_reason = dictionary.get('browsing_failed_reason')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        id = dictionary.get('id')
        is_browsable = dictionary.get('is_browsable')
        is_encrypted = dictionary.get('is_encrypted')
        kms_key_native_id = dictionary.get('kms_key_native_id')
        size = dictionary.get('size')
        start_timestamp = dictionary.get('start_timestamp')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        type = dictionary.get('type')
        volume_id = dictionary.get('volume_id')
        volume_native_id = dictionary.get('volume_native_id')
        # Return an object of this model
        return cls(
            links,
            account_native_id,
            aws_az,
            aws_region,
            browsing_failed_reason,
            expiration_timestamp,
            id,
            is_browsable,
            is_encrypted,
            kms_key_native_id,
            size,
            start_timestamp,
            tags,
            type,
            volume_id,
            volume_native_id,
        )
