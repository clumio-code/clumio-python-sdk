#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EC2MSSQLRestoreToAAGOptions')


class EC2MSSQLRestoreToAAGOptions:
    """Implementation of the 'EC2MSSQLRestoreToAAGOptions' model.

    An AG database to be restored to an AAG.

    Attributes:
        database_id:
            The Clumio-assigned ID of the MSSQL database to be restored.
            Use the [GET /datasources/aws/ec2-mssql/databases](#operation/list-ec2-mssql-
            databases)
            endpoint to fetch valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'database_id': 'database_id'}

    def __init__(self, database_id: str) -> None:
        """Constructor for the EC2MSSQLRestoreToAAGOptions class."""

        # Initialize members of the class
        self.database_id: str = database_id

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
        val = dictionary['database_id']
        val_database_id = val

        # Return an object of this model
        return cls(
            val_database_id,  # type: ignore
        )
