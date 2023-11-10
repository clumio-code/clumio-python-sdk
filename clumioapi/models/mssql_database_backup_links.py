#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='MssqlDatabaseBackupLinks')


class MssqlDatabaseBackupLinks:
    """Implementation of the 'MssqlDatabaseBackupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_management_group:
            A resource-specific HATEOAS link.
        read_management_subgroup:
            A resource-specific HATEOAS link.
        restore_mssql_database:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_management_group': 'read-management-group',
        'read_management_subgroup': 'read-management-subgroup',
        'restore_mssql_database': 'restore-mssql-database',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_management_group: hateoas_link.HateoasLink = None,
        read_management_subgroup: hateoas_link.HateoasLink = None,
        restore_mssql_database: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the MssqlDatabaseBackupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_management_group: hateoas_link.HateoasLink = read_management_group
        self.read_management_subgroup: hateoas_link.HateoasLink = read_management_subgroup
        self.restore_mssql_database: hateoas_link.HateoasLink = restore_mssql_database

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

        key = 'read-management-group'
        read_management_group = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'read-management-subgroup'
        read_management_subgroup = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore-mssql-database'
        restore_mssql_database = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_management_group, read_management_subgroup, restore_mssql_database)
