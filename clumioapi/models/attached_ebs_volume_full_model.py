#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_

T = TypeVar('T', bound='AttachedEBSVolumeFullModel')


class AttachedEBSVolumeFullModel:
    """Implementation of the 'AttachedEBSVolumeFullModel' model.

    Attributes:
        p_id:
            The Clumio-assigned id for the volume.
        is_root:
            Determines whether this device is the root for the instance.
        kms_key_native_id:
            The AWS-assigned id of the KMS key used for encryption of the volume.
        name:
            The device name for the EBS volume. For example, '/dev/xvda'.
        size:
            The size of the EBS volume. Measured in bytes (B).
        status:
            The status of the EBS volume. Possible values include 'attaching', 'attached',
            'detaching', 'detached'.
        tags:
            The AWS tags applied to the EBS volume.
        p_type:
            The type of the volume. Possible values include 'gp2', 'io1', 'st1', 'sc1', and
            'standard'.
        utilized_size_in_bytes:
            The number of bytes written in the EBS volume.
        volume_native_id:
            The AWS-assigned ID of the EBS volume.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_id': 'id',
        'is_root': 'is_root',
        'kms_key_native_id': 'kms_key_native_id',
        'name': 'name',
        'size': 'size',
        'status': 'status',
        'tags': 'tags',
        'p_type': 'type',
        'utilized_size_in_bytes': 'utilized_size_in_bytes',
        'volume_native_id': 'volume_native_id',
    }

    def __init__(
        self,
        p_id: str | None = None,
        is_root: bool | None = None,
        kms_key_native_id: str | None = None,
        name: str | None = None,
        size: int | None = None,
        status: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        p_type: str | None = None,
        utilized_size_in_bytes: int | None = None,
        volume_native_id: str | None = None,
    ) -> None:
        """Constructor for the AttachedEBSVolumeFullModel class."""

        # Initialize members of the class
        self.p_id: str | None = p_id
        self.is_root: bool | None = is_root
        self.kms_key_native_id: str | None = kms_key_native_id
        self.name: str | None = name
        self.size: int | None = size
        self.status: str | None = status
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.p_type: str | None = p_type
        self.utilized_size_in_bytes: int | None = utilized_size_in_bytes
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
        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_root', None)
        val_is_root = val

        val = dictionary.get('kms_key_native_id', None)
        val_kms_key_native_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('utilized_size_in_bytes', None)
        val_utilized_size_in_bytes = val

        val = dictionary.get('volume_native_id', None)
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_p_id,
            val_is_root,
            val_kms_key_native_id,
            val_name,
            val_size,
            val_status,
            val_tags,
            val_p_type,
            val_utilized_size_in_bytes,
            val_volume_native_id,
        )
