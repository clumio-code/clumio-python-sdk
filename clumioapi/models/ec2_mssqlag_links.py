#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_policy_definition_hateoas_link

T = TypeVar('T', bound='EC2MSSQLAGLinks')


class EC2MSSQLAGLinks:
    """Implementation of the 'EC2MSSQLAGLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        get_mssql_ec2_availability_group_backup_status_stats:
            A resource-specific HATEOAS link.
        get_mssql_ec2_availability_group_stats:
            A resource-specific HATEOAS link.
        read_policy_definition:
            A HATEOAS link to the policy protecting this resource. Will be omitted for
            unprotected entities.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'get_mssql_ec2_availability_group_backup_status_stats': 'get-mssql-ec2-availability-group-backup-status-stats',
        'get_mssql_ec2_availability_group_stats': 'get-mssql-ec2-availability-group-stats',
        'read_policy_definition': 'read-policy-definition',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        get_mssql_ec2_availability_group_backup_status_stats: hateoas_link.HateoasLink = None,
        get_mssql_ec2_availability_group_stats: hateoas_link.HateoasLink = None,
        read_policy_definition: read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink = None,
    ) -> None:
        """Constructor for the EC2MSSQLAGLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.get_mssql_ec2_availability_group_backup_status_stats: hateoas_link.HateoasLink = (
            get_mssql_ec2_availability_group_backup_status_stats
        )
        self.get_mssql_ec2_availability_group_stats: hateoas_link.HateoasLink = (
            get_mssql_ec2_availability_group_stats
        )
        self.read_policy_definition: (
            read_policy_definition_hateoas_link.ReadPolicyDefinitionHateoasLink
        ) = read_policy_definition

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

        key = 'get-mssql-ec2-availability-group-backup-status-stats'
        get_mssql_ec2_availability_group_backup_status_stats = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'get-mssql-ec2-availability-group-stats'
        get_mssql_ec2_availability_group_stats = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
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

        # Return an object of this model
        return cls(
            p_self,
            get_mssql_ec2_availability_group_backup_status_stats,
            get_mssql_ec2_availability_group_stats,
            read_policy_definition,
        )
