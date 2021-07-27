#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import host_links
from clumioapi.models import v_mware_v_center_host_compute_resource_model
from clumioapi.models import v_mware_v_center_host_datacenter_model

T = TypeVar('T', bound='ReadHostResponse')


class ReadHostResponse:
    """Implementation of the 'ReadHostResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        compute_resource:
            The VMware compute resource representing the host.
        connection_state:
            The connection state of the host as seen through the vCenter server. Examples
            include "connected", "disconnected", and "not_responding".
        datacenter:
            The data center in which the host resides.
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the host.
        is_in_maintenance_mode:
            Determines whether the host has been placed in maintenance mode as seen through
            the vCenter server. If `true`, the host is in maintenance mode.
        is_in_quarantine_mode:
            Determines whether the host has been placed in quarantine mode as seen through
            the vCenter server. If `true`, the host is in quarantine mode.
        is_standalone:
            Determines whether the host is a standalone host. If `true`, the host is a
            standalone host.
        is_supported:
            Determines whether the host can be used as a restore destination. If `true`, the
            host can be used as a restore destination and backups can be restored to the
            host.
        name:
            The VMware-assigned name of the host.
        power_state:
            The power state of the host as seen through the vCenter server. Examples include
            "powered_off", "powered_on", and "standby".
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'compute_resource': 'compute_resource',
        'connection_state': 'connection_state',
        'datacenter': 'datacenter',
        'id': 'id',
        'is_in_maintenance_mode': 'is_in_maintenance_mode',
        'is_in_quarantine_mode': 'is_in_quarantine_mode',
        'is_standalone': 'is_standalone',
        'is_supported': 'is_supported',
        'name': 'name',
        'power_state': 'power_state',
    }

    def __init__(
        self,
        etag: str = None,
        links: host_links.HostLinks = None,
        compute_resource: v_mware_v_center_host_compute_resource_model.VMwareVCenterHostComputeResourceModel = None,
        connection_state: str = None,
        datacenter: v_mware_v_center_host_datacenter_model.VMwareVCenterHostDatacenterModel = None,
        id: str = None,
        is_in_maintenance_mode: bool = None,
        is_in_quarantine_mode: bool = None,
        is_standalone: bool = None,
        is_supported: bool = None,
        name: str = None,
        power_state: str = None,
    ) -> None:
        """Constructor for the ReadHostResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: host_links.HostLinks = links
        self.compute_resource: v_mware_v_center_host_compute_resource_model.VMwareVCenterHostComputeResourceModel = (
            compute_resource
        )
        self.connection_state: str = connection_state
        self.datacenter: v_mware_v_center_host_datacenter_model.VMwareVCenterHostDatacenterModel = (
            datacenter
        )
        self.id: str = id
        self.is_in_maintenance_mode: bool = is_in_maintenance_mode
        self.is_in_quarantine_mode: bool = is_in_quarantine_mode
        self.is_standalone: bool = is_standalone
        self.is_supported: bool = is_supported
        self.name: str = name
        self.power_state: str = power_state

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
            host_links.HostLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'compute_resource'
        compute_resource = (
            v_mware_v_center_host_compute_resource_model.VMwareVCenterHostComputeResourceModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        connection_state = dictionary.get('connection_state')
        key = 'datacenter'
        datacenter = (
            v_mware_v_center_host_datacenter_model.VMwareVCenterHostDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        id = dictionary.get('id')
        is_in_maintenance_mode = dictionary.get('is_in_maintenance_mode')
        is_in_quarantine_mode = dictionary.get('is_in_quarantine_mode')
        is_standalone = dictionary.get('is_standalone')
        is_supported = dictionary.get('is_supported')
        name = dictionary.get('name')
        power_state = dictionary.get('power_state')
        # Return an object of this model
        return cls(
            etag,
            links,
            compute_resource,
            connection_state,
            datacenter,
            id,
            is_in_maintenance_mode,
            is_in_quarantine_mode,
            is_standalone,
            is_supported,
            name,
            power_state,
        )
