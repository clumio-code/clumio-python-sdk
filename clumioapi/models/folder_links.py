#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link
from clumioapi.models import protect_entities_hateoas_link
from clumioapi.models import read_policy_definition_hateoas_link
from clumioapi.models import read_v_center_object_protection_stats_hateoas_link
from clumioapi.models import unprotect_entities_hateoas_link

T = TypeVar('T', bound='FolderLinks')


class FolderLinks:
    """Implementation of the 'FolderLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        protect_entities:
            A HATEOAS link to protect the entities.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        read_vmware_vcenter_folder_compliance_stats:
            A HATEOAS link to the compliance statistics of VMs in the folders and subfolders
            of this vCenter resource.
        unprotect_entities:
            A HATEOAS link to unprotect the entities.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'protect_entities': 'protect-entities',
        'read_policy_definition': 'read-policy-definition',
        'read_vmware_vcenter_folder_compliance_stats': 'read-vmware-vcenter-folder-compliance-stats',
        'unprotect_entities': 'unprotect-entities',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        read_vmware_vcenter_folder_compliance_stats: read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink = None,
        unprotect_entities: unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink = None,
    ) -> None:
        """Constructor for the FolderLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = (
            protect_entities
        )
        self.read_policy_definition: (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition
        self.read_vmware_vcenter_folder_compliance_stats: (
            read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink
        ) = read_vmware_vcenter_folder_compliance_stats
        self.unprotect_entities: unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink = (
            unprotect_entities
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

        key = 'protect-entities'
        protect_entities = (
            protect_entities_hateoas_link.ProtectEntitiesHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'read-policy-definition'
        read_policy_definition = (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'read-vmware-vcenter-folder-compliance-stats'
        read_vmware_vcenter_folder_compliance_stats = (
            read_v_center_object_protection_stats_hateoas_link.ReadVCenterObjectProtectionStatsHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'unprotect-entities'
        unprotect_entities = (
            unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            p_self,
            protect_entities,
            read_policy_definition,
            read_vmware_vcenter_folder_compliance_stats,
            unprotect_entities,
        )
