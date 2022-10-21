#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link, read_v_center_object_protection_stats_hateoas_link

T = TypeVar('T', bound='VcenterLinks')


class VcenterLinks:
    """Implementation of the 'VcenterLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_vmware_vcenter_compliance_stats:
            A HATEOAS link to the compliance statistics of VMs in the folders and subfolders
            of this vCenter resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_vmware_vcenter_compliance_stats': 'read-vmware-vcenter-compliance-stats',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_vmware_vcenter_compliance_stats: read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink = None,
    ) -> None:
        """Constructor for the VcenterLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_vmware_vcenter_compliance_stats: read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink = (
            read_vmware_vcenter_compliance_stats
        )

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

        key = 'read-vmware-vcenter-compliance-stats'
        read_vmware_vcenter_compliance_stats = (
            read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_vmware_vcenter_compliance_stats)
