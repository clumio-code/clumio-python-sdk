#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_embedded as aws_tag_embedded_
from clumioapi.models import aws_tag_links as aws_tag_links_
from clumioapi.models import protection_info as protection_info_

T = TypeVar('T', bound='ReadAwsTagResponse')


class ReadAwsTagResponse:
    """Implementation of the 'ReadAwsTagResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the AWS tag.
        key:
            The AWS-assigned tag key.
        key_id:
            The Clumio-assigned ID of the AWS key.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the tag.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the EBS volume. Possible values include "protected" and
            "unprotected".
        value:
            The AWS-assigned tag value.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'p_id': 'id',
        'key': 'key',
        'key_id': 'key_id',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'value': 'value',
    }

    def __init__(
        self,
        embedded: aws_tag_embedded_.AwsTagEmbedded | None = None,
        links: aws_tag_links_.AwsTagLinks | None = None,
        p_id: str | None = None,
        key: str | None = None,
        key_id: str | None = None,
        organizational_unit_id: str | None = None,
        protection_info: protection_info_.ProtectionInfo | None = None,
        protection_status: str | None = None,
        value: str | None = None,
    ) -> None:
        """Constructor for the ReadAwsTagResponse class."""

        # Initialize members of the class
        self.embedded: aws_tag_embedded_.AwsTagEmbedded | None = embedded
        self.links: aws_tag_links_.AwsTagLinks | None = links
        self.p_id: str | None = p_id
        self.key: str | None = key
        self.key_id: str | None = key_id
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo | None = protection_info
        self.protection_status: str | None = protection_status
        self.value: str | None = value

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
        val = dictionary.get('_embedded', None)
        val_embedded = aws_tag_embedded_.AwsTagEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = aws_tag_links_.AwsTagLinks.from_dictionary(val)

        val = dictionary.get('id', None)
        val_p_id = val

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
            val_p_id,
            val_key,
            val_key_id,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_value,
        )
