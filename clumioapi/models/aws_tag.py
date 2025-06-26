#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_embedded
from clumioapi.models import aws_tag_links
from clumioapi.models import protection_info

T = TypeVar('T', bound='AwsTag')


class AwsTag:
    """Implementation of the 'AwsTag' model.

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
    _names = {
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
        embedded: aws_tag_embedded.AwsTagEmbedded = None,
        links: aws_tag_links.AwsTagLinks = None,
        p_id: str = None,
        key: str = None,
        key_id: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
        value: str = None,
    ) -> None:
        """Constructor for the AwsTag class."""

        # Initialize members of the class
        self.embedded: aws_tag_embedded.AwsTagEmbedded = embedded
        self.links: aws_tag_links.AwsTagLinks = links
        self.p_id: str = p_id
        self.key: str = key
        self.key_id: str = key_id
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status
        self.value: str = value

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
        key = '_embedded'
        embedded = (
            aws_tag_embedded.AwsTagEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            aws_tag_links.AwsTagLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        key = dictionary.get('key')
        key_id = dictionary.get('key_id')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        value = dictionary.get('value')
        # Return an object of this model
        return cls(
            embedded,
            links,
            p_id,
            key,
            key_id,
            organizational_unit_id,
            p_protection_info,
            protection_status,
            value,
        )
