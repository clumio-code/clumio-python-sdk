#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_embedded as aws_tag_embedded_
from clumioapi.models import aws_tag_links as aws_tag_links_
from clumioapi.models import protection_info as protection_info_
import requests

T = TypeVar('T', bound='AwsTag')


@dataclasses.dataclass
class AwsTag:
    """Implementation of the 'AwsTag' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        Id:
            The clumio-assigned id of the aws tag.

        Key:
            The aws-assigned tag key.

        KeyId:
            The clumio-assigned id of the aws key.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the tag.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not protected, then this field has a value of `null`.

        ProtectionStatus:
            The protection status of the ebs volume. possible values include "protected" and "unprotected".

        Value:
            The aws-assigned tag value.

    """

    Embedded: aws_tag_embedded_.AwsTagEmbedded | None = None
    Links: aws_tag_links_.AwsTagLinks | None = None
    Id: str | None = None
    Key: str | None = None
    KeyId: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_.ProtectionInfo | None = None
    ProtectionStatus: str | None = None
    Value: str | None = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = aws_tag_embedded_.AwsTagEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = aws_tag_links_.AwsTagLinks.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('key', None)
        val_key = val

        val = dictionary.get('key_id', None)
        val_key_id = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('value', None)
        val_value = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_id,
            val_key,
            val_key_id,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_value,
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
