#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protected_stats_deprecated
from clumioapi.models import protection_info_deprecated
from clumioapi.models import v_center_compute_resource_links

T = TypeVar('T', bound='VCenterComputeResource')


class VCenterComputeResource:
    """Implementation of the 'VCenterComputeResource' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        p_id:
            The Clumio-assigned ID of the item.
        isCluster:
            IsCluster denotes whether the compute resource is a cluster.
        isDrsEnabled:
            IsDrsEnabled denotes whether the compute resource has DRS enabled.
            NOTE: This is only applicable if "IsCluster" is true.
        name:
            The name of the compute resource.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the compute
            resource.
        protectionInfo:

        vmStats:
            ProtectedStatsDeprecated contains the compliance stats for policies which are
            protected along with
            the unprotected policies count
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'p_id': 'id',
        'isCluster': 'isCluster',
        'isDrsEnabled': 'isDrsEnabled',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protectionInfo': 'protectionInfo',
        'vmStats': 'vmStats',
    }

    def __init__(
        self,
        links: v_center_compute_resource_links.VCenterComputeResourceLinks = None,
        p_id: str = None,
        isCluster: bool = None,
        isDrsEnabled: bool = None,
        name: str = None,
        organizational_unit_id: str = None,
        protectionInfo: protection_info_deprecated.ProtectionInfoDeprecated = None,
        vmStats: protected_stats_deprecated.ProtectedStatsDeprecated = None,
    ) -> None:
        """Constructor for the VCenterComputeResource class."""

        # Initialize members of the class
        self.links: v_center_compute_resource_links.VCenterComputeResourceLinks = links
        self.p_id: str = p_id
        self.isCluster: bool = isCluster
        self.isDrsEnabled: bool = isDrsEnabled
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protectionInfo: protection_info_deprecated.ProtectionInfoDeprecated = protectionInfo
        self.vmStats: protected_stats_deprecated.ProtectedStatsDeprecated = vmStats

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
        key = '_links'
        links = (
            v_center_compute_resource_links.VCenterComputeResourceLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        isCluster = dictionary.get('isCluster')
        isDrsEnabled = dictionary.get('isDrsEnabled')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protectionInfo'
        protectionInfo = (
            protection_info_deprecated.ProtectionInfoDeprecated.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'vmStats'
        vmStats = (
            protected_stats_deprecated.ProtectedStatsDeprecated.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            links,
            p_id,
            isCluster,
            isDrsEnabled,
            name,
            organizational_unit_id,
            protectionInfo,
            vmStats,
        )
