#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import vcenter_embedded
from clumioapi.models import vcenter_links

T = TypeVar('T', bound='ReadVcenterResponse')


class ReadVcenterResponse:
    """Implementation of the 'ReadVcenterResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        backup_region:
            The region to which data is backed-up to for the vCenter server. If the vCenter
            server's back up region is unavailable, this field has a value of `unavailable`.
            Refer to the Back up Regions table for a complete list of back up regions.
        cloud_connector_download_url:
            The URL at which the Clumio Cloud Connector for this vCenter server can be
            downloaded.
        endpoint:
            The IP address or FQDN of the vCenter server.
        p_id:
            The Clumio-assigned ID of the vCenter server.
        ip_address:
            The IP address or FQDN of the vCenter server.
            This field has been replaced by the `endpoint` field
            and is being retained for backward compatibility reasons.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the vCenter.
        status:
            The connection status of the Clumio Cloud Connector. Examples include "pending",
            "connected", "disconnected", "invalid_credentials", "partial", and
            "unavailable".
        p_type:
            The type of vCenter server. If the vCenter server's type is unavailable, this
            field has a value of `unavailable`. Refer to the vCenter Types table for a
            complete list of vCenter types.
        vcenter_token:
            The token given to the Clumio Cloud Connectors to identify the vCenter server.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'links': '_links',
        'backup_region': 'backup_region',
        'cloud_connector_download_url': 'cloud_connector_download_url',
        'endpoint': 'endpoint',
        'p_id': 'id',
        'ip_address': 'ip_address',
        'organizational_unit_id': 'organizational_unit_id',
        'status': 'status',
        'p_type': 'type',
        'vcenter_token': 'vcenter_token',
    }

    def __init__(
        self,
        embedded: vcenter_embedded.VcenterEmbedded = None,
        links: vcenter_links.VcenterLinks = None,
        backup_region: str = None,
        cloud_connector_download_url: str = None,
        endpoint: str = None,
        p_id: str = None,
        ip_address: str = None,
        organizational_unit_id: str = None,
        status: str = None,
        p_type: str = None,
        vcenter_token: str = None,
    ) -> None:
        """Constructor for the ReadVcenterResponse class."""

        # Initialize members of the class
        self.embedded: vcenter_embedded.VcenterEmbedded = embedded
        self.links: vcenter_links.VcenterLinks = links
        self.backup_region: str = backup_region
        self.cloud_connector_download_url: str = cloud_connector_download_url
        self.endpoint: str = endpoint
        self.p_id: str = p_id
        self.ip_address: str = ip_address
        self.organizational_unit_id: str = organizational_unit_id
        self.status: str = status
        self.p_type: str = p_type
        self.vcenter_token: str = vcenter_token

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
            vcenter_embedded.VcenterEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            vcenter_links.VcenterLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        backup_region = dictionary.get('backup_region')
        cloud_connector_download_url = dictionary.get('cloud_connector_download_url')
        endpoint = dictionary.get('endpoint')
        p_id = dictionary.get('id')
        ip_address = dictionary.get('ip_address')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        status = dictionary.get('status')
        p_type = dictionary.get('type')
        vcenter_token = dictionary.get('vcenter_token')
        # Return an object of this model
        return cls(
            embedded,
            links,
            backup_region,
            cloud_connector_download_url,
            endpoint,
            p_id,
            ip_address,
            organizational_unit_id,
            status,
            p_type,
            vcenter_token,
        )
