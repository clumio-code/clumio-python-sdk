#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model

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
    _names = {
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
        p_id: str = None,
        is_root: bool = None,
        kms_key_native_id: str = None,
        name: str = None,
        size: int = None,
        status: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        p_type: str = None,
        utilized_size_in_bytes: int = None,
        volume_native_id: str = None,
    ) -> None:
        """Constructor for the AttachedEBSVolumeFullModel class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.is_root: bool = is_root
        self.kms_key_native_id: str = kms_key_native_id
        self.name: str = name
        self.size: int = size
        self.status: str = status
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.p_type: str = p_type
        self.utilized_size_in_bytes: int = utilized_size_in_bytes
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
        p_id = dictionary.get('id')
        is_root = dictionary.get('is_root')
        kms_key_native_id = dictionary.get('kms_key_native_id')
        name = dictionary.get('name')
        size = dictionary.get('size')
        status = dictionary.get('status')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        p_type = dictionary.get('type')
        utilized_size_in_bytes = dictionary.get('utilized_size_in_bytes')
        volume_native_id = dictionary.get('volume_native_id')
        # Return an object of this model
        return cls(
            p_id,
            is_root,
            kms_key_native_id,
            name,
            size,
            status,
            tags,
            p_type,
            utilized_size_in_bytes,
            volume_native_id,
        )
