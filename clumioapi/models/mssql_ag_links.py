#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import (
    hateoas_link,
    hateoas_self_link,
    protect_entities_hateoas_link,
    read_policy_definition_hateoas_link,
    unprotect_entities_hateoas_link,
)

T = TypeVar('T', bound='MssqlAGLinks')


class MssqlAGLinks:
    """Implementation of the 'MssqlAGLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        get_mssql_availability_group_stats:
            A resource-specific HATEOAS link.
        protect_entities:
            A HATEOAS link to protect the entities.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
        unprotect_entities:
            A HATEOAS link to unprotect the entities.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'get_mssql_availability_group_stats': 'get-mssql-availability-group-stats',
        'protect_entities': 'protect-entities',
        'read_policy_definition': 'read-policy-definition',
        'unprotect_entities': 'unprotect-entities',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        get_mssql_availability_group_stats: hateoas_link.HateoasLink = None,
        protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
        unprotect_entities: unprotect_entities_hateoas_link.UnprotectEntitiesHateoasLink = None,
    ) -> None:
        """Constructor for the MssqlAGLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.get_mssql_availability_group_stats: hateoas_link.HateoasLink = (
            get_mssql_availability_group_stats
        )
        self.protect_entities: protect_entities_hateoas_link.ProtectEntitiesHateoasLink = (
            protect_entities
        )
        self.read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = (
            read_policy_definition
        )
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

        key = 'get-mssql-availability-group-stats'
        get_mssql_availability_group_stats = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
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
            get_mssql_availability_group_stats,
            protect_entities,
            read_policy_definition,
            unprotect_entities,
        )
