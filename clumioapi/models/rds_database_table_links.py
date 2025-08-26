#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

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
    _names: dict[str, str] = {
        'p_self': '_self',
        'read_backup_aws_rds_resource_database_table_columns': 'read-backup-aws-rds-resource-database-table-columns',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        read_backup_aws_rds_resource_database_table_columns: (
            hateoas_link_.HateoasLink | None
        ) = None,
    ) -> None:
        """Constructor for the RDSDatabaseTableLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.read_backup_aws_rds_resource_database_table_columns: (
            hateoas_link_.HateoasLink | None
        ) = read_backup_aws_rds_resource_database_table_columns

    @classmethod
    def from_dictionary(cls: Type[T], dictionary: Mapping[str, Any]) -> T:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-backup-aws-rds-resource-database-table-columns', None)
        val_read_backup_aws_rds_resource_database_table_columns = (
            hateoas_link_.HateoasLink.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_p_self,
            val_read_backup_aws_rds_resource_database_table_columns,
        )
