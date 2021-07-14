#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import resource_pool_datacenter_model
from clumioapi.models import resource_pool_links
from clumioapi.models import v_mware_resource_pool_compute_resource_model
from clumioapi.models import v_mware_resource_pool_parent_model

T = TypeVar('T', bound='ReadResourcePoolResponse')


class ReadResourcePoolResponse:
    """Implementation of the 'ReadResourcePoolResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        compute_resource:
            The compute resource that the resource pool comprises.
        datacenter:
            The data center in which the resource pool resides.
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the resource pool.
        is_root:
            Determines whether the resource pool is the default, hidden resource pool.
        is_supported:
            Determines whether the resource pool can be used as a restore destination. If
            `true`, the resource pool can be used as a restore destination and backups can
            be restored to the resource pool.
        name:
            The VMware-assigned name of the resource pool.
        parent:
            The vCenter object that is the parent of the resource pool.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'compute_resource': 'compute_resource',
        'datacenter': 'datacenter',
        'id': 'id',
        'is_root': 'is_root',
        'is_supported': 'is_supported',
        'name': 'name',
        'parent': 'parent',
    }

    def __init__(
        self,
        etag: str = None,
        links: resource_pool_links.ResourcePoolLinks = None,
        compute_resource: v_mware_resource_pool_compute_resource_model.VMwareResourcePoolComputeResourceModel = None,
        datacenter: resource_pool_datacenter_model.ResourcePoolDatacenterModel = None,
        id: str = None,
        is_root: bool = None,
        is_supported: bool = None,
        name: str = None,
        parent: v_mware_resource_pool_parent_model.VMwareResourcePoolParentModel = None,
    ) -> None:
        """Constructor for the ReadResourcePoolResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: resource_pool_links.ResourcePoolLinks = links
        self.compute_resource: v_mware_resource_pool_compute_resource_model.VMwareResourcePoolComputeResourceModel = (
            compute_resource
        )
        self.datacenter: resource_pool_datacenter_model.ResourcePoolDatacenterModel = datacenter
        self.id: str = id
        self.is_root: bool = is_root
        self.is_supported: bool = is_supported
        self.name: str = name
        self.parent: v_mware_resource_pool_parent_model.VMwareResourcePoolParentModel = parent

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
            resource_pool_links.ResourcePoolLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'compute_resource'
        compute_resource = (
            v_mware_resource_pool_compute_resource_model.VMwareResourcePoolComputeResourceModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'datacenter'
        datacenter = (
            resource_pool_datacenter_model.ResourcePoolDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        id = dictionary.get('id')
        is_root = dictionary.get('is_root')
        is_supported = dictionary.get('is_supported')
        name = dictionary.get('name')
        key = 'parent'
        parent = (
            v_mware_resource_pool_parent_model.VMwareResourcePoolParentModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            etag, links, compute_resource, datacenter, id, is_root, is_supported, name, parent
        )
