#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_

T = TypeVar('T', bound='EC2MssqlDatabasePitrIntervalLinks')


class EC2MssqlDatabasePitrIntervalLinks:
    """Implementation of the 'EC2MssqlDatabasePitrIntervalLinks' model.

    URLs to pages related to the resource.

    Attributes:
        restore_ec2_mssql_database:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'restore_ec2_mssql_database': 'restore-ec2-mssql-database'}

    def __init__(self, restore_ec2_mssql_database: hateoas_link_.HateoasLink) -> None:
        """Constructor for the EC2MssqlDatabasePitrIntervalLinks class."""

        # Initialize members of the class
        self.restore_ec2_mssql_database: hateoas_link_.HateoasLink = restore_ec2_mssql_database

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
        val = dictionary['restore-ec2-mssql-database']
        val_restore_ec2_mssql_database = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_restore_ec2_mssql_database,  # type: ignore
        )
