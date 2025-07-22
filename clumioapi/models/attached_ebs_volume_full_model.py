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
        p_id: str,
        is_root: bool,
        kms_key_native_id: str,
        name: str,
        size: int,
        status: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
        p_type: str,
        utilized_size_in_bytes: int,
        volume_native_id: str,
    ) -> None:
        """Constructor for the AttachedEBSVolumeFullModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.is_root: bool = is_root
        self.kms_key_native_id: str = kms_key_native_id
        self.name: str = name
        self.size: int = size
        self.status: str = status
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] = tags
        self.p_type: str = p_type
        self.utilized_size_in_bytes: int = utilized_size_in_bytes
        self.volume_native_id: str = volume_native_id

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

        # Extract variables from the dictionary
        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_root']
        val_is_root = val

        val = dictionary['kms_key_native_id']
        val_kms_key_native_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['size']
        val_size = val

        val = dictionary['status']
        val_status = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary['type']
        val_p_type = val

        val = dictionary['utilized_size_in_bytes']
        val_utilized_size_in_bytes = val

        val = dictionary['volume_native_id']
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_is_root,  # type: ignore
            val_kms_key_native_id,  # type: ignore
            val_name,  # type: ignore
            val_size,  # type: ignore
            val_status,  # type: ignore
            val_tags,  # type: ignore
            val_p_type,  # type: ignore
            val_utilized_size_in_bytes,  # type: ignore
            val_volume_native_id,  # type: ignore
        )
