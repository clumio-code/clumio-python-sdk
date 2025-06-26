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
    _names = {
        'read_backup_aws_rds_resource_database_table_columns': 'read-backup-aws-rds-resource-database-table-columns'
    }

    def __init__(self, read_backup_aws_rds_resource_database_table_columns: object = None) -> None:
        """Constructor for the RDSDatabaseTableEmbedded class."""

        # Initialize members of the class
        self.read_backup_aws_rds_resource_database_table_columns: object = (
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
        read_backup_aws_rds_resource_database_table_columns = dictionary.get(
            'read-backup-aws-rds-resource-database-table-columns'
        )
        # Return an object of this model
        return cls(read_backup_aws_rds_resource_database_table_columns)
