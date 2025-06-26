#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='S3InstantAccessEndpointLinks')


class S3InstantAccessEndpointLinks:
    """Implementation of the 'S3InstantAccessEndpointLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_protection_group_instant_access_endpoint:
            URL to the detailed information of the instant access endpoint
        read_protection_group_instant_access_endpoint_role_permission:
            URL to the role permissions of the instant access endpoint
        read_protection_group_instant_access_endpoint_uri:
            URL for getting URI of the instant access endpoint
        read_protection_group_s3_asset:
            URL to the associated protection group S3 asset
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_protection_group_instant_access_endpoint': 'read-protection-group-instant-access-endpoint',
        'read_protection_group_instant_access_endpoint_role_permission': 'read-protection-group-instant-access-endpoint-role-permission',
        'read_protection_group_instant_access_endpoint_uri': 'read-protection-group-instant-access-endpoint-uri',
        'read_protection_group_s3_asset': 'read-protection-group-s3-asset',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_protection_group_instant_access_endpoint: object = None,
        read_protection_group_instant_access_endpoint_role_permission: object = None,
        read_protection_group_instant_access_endpoint_uri: object = None,
        read_protection_group_s3_asset: object = None,
    ) -> None:
        """Constructor for the S3InstantAccessEndpointLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_protection_group_instant_access_endpoint: object = (
            read_protection_group_instant_access_endpoint
        )
        self.read_protection_group_instant_access_endpoint_role_permission: object = (
            read_protection_group_instant_access_endpoint_role_permission
        )
        self.read_protection_group_instant_access_endpoint_uri: object = (
            read_protection_group_instant_access_endpoint_uri
        )
        self.read_protection_group_s3_asset: object = read_protection_group_s3_asset

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        read_protection_group_instant_access_endpoint = dictionary.get(
            'read-protection-group-instant-access-endpoint'
        )
        read_protection_group_instant_access_endpoint_role_permission = dictionary.get(
            'read-protection-group-instant-access-endpoint-role-permission'
        )
        read_protection_group_instant_access_endpoint_uri = dictionary.get(
            'read-protection-group-instant-access-endpoint-uri'
        )
        read_protection_group_s3_asset = dictionary.get('read-protection-group-s3-asset')
        # Return an object of this model
        return cls(
            p_self,
            read_protection_group_instant_access_endpoint,
            read_protection_group_instant_access_endpoint_role_permission,
            read_protection_group_instant_access_endpoint_uri,
            read_protection_group_s3_asset,
        )
