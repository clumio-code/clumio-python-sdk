#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compute_resource_embedded
from clumioapi.models import compute_resource_links
from clumioapi.models import protection_info
from clumioapi.models import v_mware_v_center_compute_resource_datacenter_model
from clumioapi.models import v_mware_v_center_compute_resource_folder_model

T = TypeVar('T', bound='ReadComputeResourceResponse')


class ReadComputeResourceResponse:
    """Implementation of the 'ReadComputeResourceResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        compute_resource_folder:
            The compute resource folder in which the compute resource resides.
        datacenter:
            The data center associated with this compute resource.
        p_id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the compute resource.
        is_cluster:
            Determines whether the compute resource is a cluster. If `true`, then the
            compute resource is a cluster.
        is_drs_enabled:
            Determines whether the compute resource has Distributed Resource Scheduler (DRS)
            enabled. If this field and `"is_cluster":true`, then DRS is enabled in the
            compute resource cluster.
        name:
            The VMware-assigned name of the compute resource.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the compute
            resource.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of this compute resource. Refer to the Protection Status
            table for a complete list of protection statuses.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'compute_resource_folder': 'compute_resource_folder',
        'datacenter': 'datacenter',
        'p_id': 'id',
        'is_cluster': 'is_cluster',
        'is_drs_enabled': 'is_drs_enabled',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
    }

    def __init__(
        self,
        embedded: compute_resource_embedded.ComputeResourceEmbedded = None,
        etag: str = None,
        links: compute_resource_links.ComputeResourceLinks = None,
        compute_resource_folder: v_mware_v_center_compute_resource_folder_model.VMwareVCenterComputeResourceFolderModel = None,
        datacenter: v_mware_v_center_compute_resource_datacenter_model.VMwareVCenterComputeResourceDatacenterModel = None,
        p_id: str = None,
        is_cluster: bool = None,
        is_drs_enabled: bool = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info.ProtectionInfo = None,
        protection_status: str = None,
    ) -> None:
        """Constructor for the ReadComputeResourceResponse class."""

        # Initialize members of the class
        self.embedded: compute_resource_embedded.ComputeResourceEmbedded = embedded
        self.etag: str = etag
        self.links: compute_resource_links.ComputeResourceLinks = links
        self.compute_resource_folder: v_mware_v_center_compute_resource_folder_model.VMwareVCenterComputeResourceFolderModel = (
            compute_resource_folder
        )
        self.datacenter: v_mware_v_center_compute_resource_datacenter_model.VMwareVCenterComputeResourceDatacenterModel = (
            datacenter
        )
        self.p_id: str = p_id
        self.is_cluster: bool = is_cluster
        self.is_drs_enabled: bool = is_drs_enabled
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info.ProtectionInfo = protection_info
        self.protection_status: str = protection_status

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
            compute_resource_embedded.ComputeResourceEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            compute_resource_links.ComputeResourceLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'compute_resource_folder'
        compute_resource_folder = (
            v_mware_v_center_compute_resource_folder_model.VMwareVCenterComputeResourceFolderModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'datacenter'
        datacenter = (
            v_mware_v_center_compute_resource_datacenter_model.VMwareVCenterComputeResourceDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        is_cluster = dictionary.get('is_cluster')
        is_drs_enabled = dictionary.get('is_drs_enabled')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        p_protection_info = (
            protection_info.ProtectionInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            compute_resource_folder,
            datacenter,
            p_id,
            is_cluster,
            is_drs_enabled,
            name,
            organizational_unit_id,
            p_protection_info,
            protection_status,
        )
