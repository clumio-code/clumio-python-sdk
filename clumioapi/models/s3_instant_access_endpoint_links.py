#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link as hateoas_self_link_

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
    _names: dict[str, str] = {
        'p_self': '_self',
        'read_protection_group_instant_access_endpoint': 'read-protection-group-instant-access-endpoint',
        'read_protection_group_instant_access_endpoint_role_permission': 'read-protection-group-instant-access-endpoint-role-permission',
        'read_protection_group_instant_access_endpoint_uri': 'read-protection-group-instant-access-endpoint-uri',
        'read_protection_group_s3_asset': 'read-protection-group-s3-asset',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        read_protection_group_instant_access_endpoint: object | None = None,
        read_protection_group_instant_access_endpoint_role_permission: object | None = None,
        read_protection_group_instant_access_endpoint_uri: object | None = None,
        read_protection_group_s3_asset: object | None = None,
    ) -> None:
        """Constructor for the S3InstantAccessEndpointLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.read_protection_group_instant_access_endpoint: object | None = (
            read_protection_group_instant_access_endpoint
        )
        self.read_protection_group_instant_access_endpoint_role_permission: object | None = (
            read_protection_group_instant_access_endpoint_role_permission
        )
        self.read_protection_group_instant_access_endpoint_uri: object | None = (
            read_protection_group_instant_access_endpoint_uri
        )
        self.read_protection_group_s3_asset: object | None = read_protection_group_s3_asset

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
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-protection-group-instant-access-endpoint', None)
        val_read_protection_group_instant_access_endpoint = val

        val = dictionary.get('read-protection-group-instant-access-endpoint-role-permission', None)
        val_read_protection_group_instant_access_endpoint_role_permission = val

        val = dictionary.get('read-protection-group-instant-access-endpoint-uri', None)
        val_read_protection_group_instant_access_endpoint_uri = val

        val = dictionary.get('read-protection-group-s3-asset', None)
        val_read_protection_group_s3_asset = val

        # Return an object of this model
        return cls(
            val_p_self,
            val_read_protection_group_instant_access_endpoint,
            val_read_protection_group_instant_access_endpoint_role_permission,
            val_read_protection_group_instant_access_endpoint_uri,
            val_read_protection_group_s3_asset,
        )
