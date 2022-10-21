#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import (
    compute_resource_id_model,
    host_id_model,
    v_mware_datastore_links,
    v_mware_v_center_datastore_datacenter_model,
    v_mware_v_center_datastore_folder_model,
)

T = TypeVar('T', bound='VMwareDatastoreWithETag')


class VMwareDatastoreWithETag:
    """Implementation of the 'VMwareDatastoreWithETag' model.

    VMwareDatastoreWithETag to support etag string to be calculated

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        compute_resources:
            The compute resources associated with this datastore.
        datacenter:
            The data center in which this datastore resides.
        datastore_folder:
            VMwareVCenterDatastoreFolderModel
            The datastore folder in which this datastore resides.
        datastore_type:
            The file system format used for the datastore. Refer to the Supported Datastore
            Types section for a complete list of datastore types.
        hosts:
            The hosts associated with this datastore.
        id:
            The VMware-assigned Managed Object Reference (MoRef) ID of the datastore.
        is_multi_host:
            Determines whether the datastore is shared across multiple hosts. If `true`, the
            datastore is a multi-host datastore.
        is_supported:
            Determines whether the datastore can be used as a restore destination. If
            `true`, the datastore can be used as a restore destination and backups can be
            restored to the datastore.
        name:
            The VMware-assigned name of this datastore.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'etag': '_etag',
        'links': '_links',
        'compute_resources': 'compute_resources',
        'datacenter': 'datacenter',
        'datastore_folder': 'datastore_folder',
        'datastore_type': 'datastore_type',
        'hosts': 'hosts',
        'id': 'id',
        'is_multi_host': 'is_multi_host',
        'is_supported': 'is_supported',
        'name': 'name',
    }

    def __init__(
        self,
        etag: str = None,
        links: v_mware_datastore_links.VMwareDatastoreLinks = None,
        compute_resources: Sequence[compute_resource_id_model.ComputeResourceIDModel] = None,
        datacenter: v_mware_v_center_datastore_datacenter_model.VMwareVCenterDatastoreDatacenterModel = None,
        datastore_folder: v_mware_v_center_datastore_folder_model.VMwareVCenterDatastoreFolderModel = None,
        datastore_type: str = None,
        hosts: Sequence[host_id_model.HostIDModel] = None,
        id: str = None,
        is_multi_host: bool = None,
        is_supported: bool = None,
        name: str = None,
    ) -> None:
        """Constructor for the VMwareDatastoreWithETag class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: v_mware_datastore_links.VMwareDatastoreLinks = links
        self.compute_resources: Sequence[
            compute_resource_id_model.ComputeResourceIDModel
        ] = compute_resources
        self.datacenter: v_mware_v_center_datastore_datacenter_model.VMwareVCenterDatastoreDatacenterModel = (
            datacenter
        )
        self.datastore_folder: v_mware_v_center_datastore_folder_model.VMwareVCenterDatastoreFolderModel = (
            datastore_folder
        )
        self.datastore_type: str = datastore_type
        self.hosts: Sequence[host_id_model.HostIDModel] = hosts
        self.id: str = id
        self.is_multi_host: bool = is_multi_host
        self.is_supported: bool = is_supported
        self.name: str = name

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
            v_mware_datastore_links.VMwareDatastoreLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        compute_resources = None
        if dictionary.get('compute_resources'):
            compute_resources = list()
            for value in dictionary.get('compute_resources'):
                compute_resources.append(
                    compute_resource_id_model.ComputeResourceIDModel.from_dictionary(value)
                )

        key = 'datacenter'
        datacenter = (
            v_mware_v_center_datastore_datacenter_model.VMwareVCenterDatastoreDatacenterModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'datastore_folder'
        datastore_folder = (
            v_mware_v_center_datastore_folder_model.VMwareVCenterDatastoreFolderModel.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        datastore_type = dictionary.get('datastore_type')
        hosts = None
        if dictionary.get('hosts'):
            hosts = list()
            for value in dictionary.get('hosts'):
                hosts.append(host_id_model.HostIDModel.from_dictionary(value))

        id = dictionary.get('id')
        is_multi_host = dictionary.get('is_multi_host')
        is_supported = dictionary.get('is_supported')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(
            etag,
            links,
            compute_resources,
            datacenter,
            datastore_folder,
            datastore_type,
            hosts,
            id,
            is_multi_host,
            is_supported,
            name,
        )
