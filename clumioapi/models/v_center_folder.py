#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import protected_stats_deprecated
from clumioapi.models import protection_info_deprecated
from clumioapi.models import v_center_folder_links

T = TypeVar('T', bound='VCenterFolder')


class VCenterFolder:
    """Implementation of the 'VCenterFolder' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        hasChildGroups:
            HasChildGroups denotes whether direct child folders exist.
        p_id:
            The Clumio-assigned ID of the item.
        isRoot:
            IsRoot denotes whether this folder is a root (hidden) folder.
        name:
            Name of the folder.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the folder.
        protectionInfo:

        vmStats:
            ProtectedStatsDeprecated contains the compliance stats for policies which are
            protected along with
            the unprotected policies count
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'hasChildGroups': 'hasChildGroups',
        'p_id': 'id',
        'isRoot': 'isRoot',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protectionInfo': 'protectionInfo',
        'vmStats': 'vmStats',
    }

    def __init__(
        self,
        links: v_center_folder_links.VCenterFolderLinks = None,
        hasChildGroups: bool = None,
        p_id: str = None,
        isRoot: bool = None,
        name: str = None,
        organizational_unit_id: str = None,
        protectionInfo: protection_info_deprecated.ProtectionInfoDeprecated = None,
        vmStats: protected_stats_deprecated.ProtectedStatsDeprecated = None,
    ) -> None:
        """Constructor for the VCenterFolder class."""

        # Initialize members of the class
        self.links: v_center_folder_links.VCenterFolderLinks = links
        self.hasChildGroups: bool = hasChildGroups
        self.p_id: str = p_id
        self.isRoot: bool = isRoot
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
            v_center_folder_links.VCenterFolderLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        hasChildGroups = dictionary.get('hasChildGroups')
        p_id = dictionary.get('id')
        isRoot = dictionary.get('isRoot')
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
            hasChildGroups,
            p_id,
            isRoot,
            name,
            organizational_unit_id,
            protectionInfo,
            vmStats,
        )
