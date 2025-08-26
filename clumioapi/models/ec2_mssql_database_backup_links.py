#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='EC2MSSQLDatabaseBackupLinks')


class EC2MSSQLDatabaseBackupLinks:
    """Implementation of the 'EC2MSSQLDatabaseBackupLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_aws_environment:
            A resource-specific HATEOAS link.
        restore_ec2_mssql_database:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'read_aws_environment': 'read-aws-environment',
        'restore_ec2_mssql_database': 'restore-ec2-mssql-database',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        read_aws_environment: hateoas_link_.HateoasLink | None = None,
        restore_ec2_mssql_database: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the EC2MSSQLDatabaseBackupLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.read_aws_environment: hateoas_link_.HateoasLink | None = read_aws_environment
        self.restore_ec2_mssql_database: hateoas_link_.HateoasLink | None = (
            restore_ec2_mssql_database
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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-aws-environment', None)
        val_read_aws_environment = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('restore-ec2-mssql-database', None)
        val_restore_ec2_mssql_database = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_read_aws_environment,
            val_restore_ec2_mssql_database,
        )
