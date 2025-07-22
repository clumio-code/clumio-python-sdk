#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RDSDatabaseTableEmbedded')


class RDSDatabaseTableEmbedded:
    """Implementation of the 'RDSDatabaseTableEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_backup_aws_rds_resource_database_table_columns:
            Add resource specific HATEOAS embedded
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'read_backup_aws_rds_resource_database_table_columns': 'read-backup-aws-rds-resource-database-table-columns'
    }

    def __init__(self, read_backup_aws_rds_resource_database_table_columns: object) -> None:
        """Constructor for the RDSDatabaseTableEmbedded class."""

        # Initialize members of the class
        self.read_backup_aws_rds_resource_database_table_columns: object = (
            read_backup_aws_rds_resource_database_table_columns
        )

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

        # Extract variables from the dictionary
        val = dictionary['read-backup-aws-rds-resource-database-table-columns']
        val_read_backup_aws_rds_resource_database_table_columns = val

        # Return an object of this model
        return cls(
            val_read_backup_aws_rds_resource_database_table_columns,  # type: ignore
        )
