#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model

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
    _names = {
        'kms_key_native_id': 'kms_key_native_id',
        'name': 'name',
        'tags': 'tags',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        kms_key_native_id: str = None,
        name: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        volume_native_id: str = None,
    ) -> None:
        """Constructor for the EC2RestoreEbsBlockDeviceMapping class."""

        # Initialize members of the class
        self.kms_key_native_id: str = kms_key_native_id
        self.name: str = name
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
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
        kms_key_native_id = dictionary.get('kms_key_native_id')
        name = dictionary.get('name')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        volume_native_id = dictionary.get('volume_native_id')
        # Return an object of this model
        return cls(kms_key_native_id, name, tags, volume_native_id)
