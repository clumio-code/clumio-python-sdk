#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

T = TypeVar('T', bound='EC2RestoreEbsBlockDeviceMapping')


class EC2RestoreEbsBlockDeviceMapping:
    """Implementation of the 'EC2RestoreEbsBlockDeviceMapping' model.

    Attributes:
        kms_key_native_id:
            The AWS-assigned ID for a customer managed KMS key under which the
            EBS volume is encrypted.
        name:
            The device name where the EBS volume is attached to the instance, needed by
            instance_restore_target and ami_restore_target restore type and by
            volumes_restore_target
            when target_instance_native_id is provided.
        tags:
            The AWS tags to be applied to the volume.
        volume_native_id:
            The AWS-assigned ID of the backed-up volume.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'kms_key_native_id': 'kms_key_native_id',
        'name': 'name',
        'tags': 'tags',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        kms_key_native_id: str | None = None,
        name: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        volume_native_id: str | None = None,
    ) -> None:
        """Constructor for the EC2RestoreEbsBlockDeviceMapping class."""

        # Initialize members of the class
        self.kms_key_native_id: str | None = kms_key_native_id
        self.name: str | None = name
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
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
        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('volume_native_id', None)
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_kms_key_native_id,
            val_name,
            val_tags,
            val_volume_native_id,
        )
