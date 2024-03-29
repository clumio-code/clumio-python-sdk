#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='RDSDatabaseTableLinks')


class RDSDatabaseTableLinks:
    """Implementation of the 'RDSDatabaseTableLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_backup_aws_rds_resource_database_table_columns:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_self': '_self',
        'read_backup_aws_rds_resource_database_table_columns': 'read-backup-aws-rds-resource-database-table-columns',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        read_backup_aws_rds_resource_database_table_columns: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the RDSDatabaseTableLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.read_backup_aws_rds_resource_database_table_columns: hateoas_link.HateoasLink = (
            read_backup_aws_rds_resource_database_table_columns
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

        key = 'read-backup-aws-rds-resource-database-table-columns'
        read_backup_aws_rds_resource_database_table_columns = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, read_backup_aws_rds_resource_database_table_columns)
