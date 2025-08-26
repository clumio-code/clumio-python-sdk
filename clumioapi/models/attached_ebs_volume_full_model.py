#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
import requests

T = TypeVar('T', bound='AttachedEBSVolumeFullModel')


@dataclasses.dataclass
class AttachedEBSVolumeFullModel:
    """Implementation of the 'AttachedEBSVolumeFullModel' model.

        Attributes:
            Id:
                The clumio-assigned id for the volume.

            IsRoot:
                Determines whether this device is the root for the instance.

            KmsKeyNativeId:
                The aws-assigned id of the kms key used for encryption of the volume.

            Name:
                The device name for the ebs volume. for example, '/dev/xvda'.

            Size:
                The size of the ebs volume. measured in bytes (b).

            Status:
                The status of the ebs volume. possible values include 'attaching', 'attached',
    'detaching', 'detached'.

            Tags:
                The aws tags applied to the ebs volume.

            Type:
                The type of the volume. possible values include 'gp2', 'io1', 'st1', 'sc1', and 'standard'.

            UtilizedSizeInBytes:
                The number of bytes written in the ebs volume.

            VolumeNativeId:
                The aws-assigned id of the ebs volume.

    """

    Id: str | None = None
    IsRoot: bool | None = None
    KmsKeyNativeId: str | None = None
    Name: str | None = None
    Size: int | None = None
    Status: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    Type: str | None = None
    UtilizedSizeInBytes: int | None = None
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
        val = dictionary.get('id', None)
        val_id = val

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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('utilized_size_in_bytes', None)
        val_utilized_size_in_bytes = val

        val = dictionary.get('volume_native_id', None)
        val_volume_native_id = val

        # Return an object of this model
        return cls(
            val_id,
            val_is_root,
            val_kms_key_native_id,
            val_name,
            val_size,
            val_status,
            val_tags,
            val_type,
            val_utilized_size_in_bytes,
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
