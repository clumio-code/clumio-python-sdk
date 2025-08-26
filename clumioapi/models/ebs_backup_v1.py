#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import ebs_backup_links_v1 as ebs_backup_links_v1_
import requests

T = TypeVar('T', bound='EBSBackupV1')


@dataclasses.dataclass
class EBSBackupV1:
    """Implementation of the 'EBSBackupV1' model.

        Attributes:
            Links:
                Urls to pages related to the resource.

            AccountNativeId:
                The aws-assigned id of the account associated with the backup.

            AwsAz:
                The availability zone associated with the volume backup. for example, `us-west-2a`.

            AwsRegion:
                The aws region in which the volume backup resides. for example, `us-west-2`.

            BrowsingFailedReason:
                The reason that browsing is unavailable for the backup. possible values include "file_limit_exceeded" and
    "browsing_unavailable". if browse indexing is successful, then this field has a value of `null`.

            ExpirationTimestamp:
                The timestamp of when this backup expires. represented in rfc-3339 format.

            Id:
                The clumio-assigned id of the volume backup.

            IsBrowsable:
                Determines whether browsing is available for the backup. if `true`, then browsing is available for the backup.

            IsEncrypted:
                Determines whether the ebs volume backup is encrypted. if `true`, the volume backup is encrypted.

            KmsKeyNativeId:
                The aws-assigned id of the kms key encrypting this ebs volume backup. if the volume is not encrypted, this field has a value of `null`.

            Size:
                The size of the volume backup. measured in gigabytes (gb).

            StartTimestamp:
                The timestamp of when this backup started. represented in rfc-3339 format.

            Tags:
                The volume tags applied to the original ebs volume before backup.

            Type:
                The volume type of the original ebs volume before backup. possible values include `gp2`, `io1`, `st1`, `sc1`, `standard`.

            VolumeId:
                The clumio-assigned id of the ebs volume associated with the volume backup.

            VolumeNativeId:
                The aws-assigned id of the ebs volume associated with the volume backup.

    """

    Links: ebs_backup_links_v1_.EBSBackupLinksV1 | None = None
    AccountNativeId: str | None = None
    AwsAz: str | None = None
    AwsRegion: str | None = None
    BrowsingFailedReason: str | None = None
    ExpirationTimestamp: str | None = None
    Id: str | None = None
    IsBrowsable: bool | None = None
    IsEncrypted: bool | None = None
    KmsKeyNativeId: str | None = None
    Size: int | None = None
    StartTimestamp: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    Type: str | None = None
    VolumeId: str | None = None
    VolumeNativeId: str | None = None

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
        val_id = val

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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
            val_is_browsable,
            val_is_encrypted,
            val_kms_key_native_id,
            val_size,
            val_start_timestamp,
            val_tags,
            val_type,
            val_volume_id,
            val_volume_native_id,
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
