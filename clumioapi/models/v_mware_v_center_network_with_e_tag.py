#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import v_mware_v_center_network_datacenter_model
from clumioapi.models import v_mware_v_center_network_folder_model
from clumioapi.models import v_mware_v_center_network_links

T = TypeVar('T', bound='VMwareVCenterNetworkWithETag')


class VMwareVCenterNetworkWithETag:
    """Implementation of the 'VMwareVCenterNetworkWithETag' model.

    VMwareVCenterNetworkWithETag to support etag string to be calculated.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        datacenter:
            The data center associated with this network.
        p_id:
            The VMware-assigned ID of this network.
        is_supported:
            Determines whether VMs can be connected to the network. If `true`, VMs can be
            connected to the network.
        name:
            The name of this network.
        network_folder:
            The network folder associated with this network.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'datacenter': 'datacenter',
        'p_id': 'id',
        'is_supported': 'is_supported',
        'name': 'name',
        'network_folder': 'network_folder',
    }

    def __init__(
        self,
        etag: str = None,
        links: v_mware_v_center_network_links.VMwareVCenterNetworkLinks = None,
        datacenter: v_mware_v_center_network_datacenter_model.VMwareVCenterNetworkDatacenterModel = None,
        p_id: str = None,
        is_supported: bool = None,
        name: str = None,
        network_folder: v_mware_v_center_network_folder_model.VMwareVCenterNetworkFolderModel = None,
    ) -> None:
        """Constructor for the VMwareVCenterNetworkWithETag class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: v_mware_v_center_network_links.VMwareVCenterNetworkLinks = links
        self.datacenter: (
            v_mware_v_center_network_datacenter_model.VMwareVCenterNetworkDatacenterModel
        ) = datacenter
        self.p_id: str = p_id
        self.is_supported: bool = is_supported
        self.name: str = name
        self.network_folder: (
            v_mware_v_center_network_folder_model.VMwareVCenterNetworkFolderModel
        ) = network_folder

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
        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            v_mware_v_center_network_links.VMwareVCenterNetworkLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'datacenter'
        datacenter = (
            v_mware_v_center_network_datacenter_model.VMwareVCenterNetworkDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        is_supported = dictionary.get('is_supported')
        name = dictionary.get('name')
        key = 'network_folder'
        network_folder = (
            v_mware_v_center_network_folder_model.VMwareVCenterNetworkFolderModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(etag, links, datacenter, p_id, is_supported, name, network_folder)
