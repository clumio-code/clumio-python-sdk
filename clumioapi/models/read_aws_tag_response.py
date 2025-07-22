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
        embedded: aws_tag_embedded_.AwsTagEmbedded,
        links: aws_tag_links_.AwsTagLinks,
        p_id: str,
        key: str,
        key_id: str,
        organizational_unit_id: str,
        protection_info: protection_info_.ProtectionInfo,
        protection_status: str,
        value: str,
    ) -> None:
        """Constructor for the ReadAwsTagResponse class."""

        # Initialize members of the class
        self.embedded: aws_tag_embedded_.AwsTagEmbedded = embedded
        self.links: aws_tag_links_.AwsTagLinks = links
        self.p_id: str = p_id
        self.key: str = key
        self.key_id: str = key_id
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.value: str = value

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
        val = dictionary['_embedded']
        val_embedded = aws_tag_embedded_.AwsTagEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = aws_tag_links_.AwsTagLinks.from_dictionary(val)

        val = dictionary['id']
        val_p_id = val

        val = dictionary['key']
        val_key = val

        val = dictionary['key_id']
        val_key_id = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_.ProtectionInfo.from_dictionary(val)

        val = dictionary['protection_status']
        val_protection_status = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_p_id,  # type: ignore
            val_key,  # type: ignore
            val_key_id,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_protection_status,  # type: ignore
            val_value,  # type: ignore
        )
