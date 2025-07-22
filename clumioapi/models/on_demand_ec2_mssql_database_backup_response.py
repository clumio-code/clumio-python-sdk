#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    create_on_demand_ec2_mssql_database_backup_response_links as \
    create_on_demand_ec2_mssql_database_backup_response_links_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
from clumioapi.models import read_task_hateoas_outer_embedded as read_task_hateoas_outer_embedded_

T = TypeVar('T', bound='OnDemandEC2MSSQLDatabaseBackupResponse')


class OnDemandEC2MSSQLDatabaseBackupResponse:
    """Implementation of the 'OnDemandEC2MSSQLDatabaseBackupResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        p_self:
            The HATEOAS link to this resource.
        task_id:
            Task Id
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'p_self': '_self',
        'task_id': 'task_id',
    }

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded,
        links: create_on_demand_ec2_mssql_database_backup_response_links_.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks,
        p_self: hateoas_self_link_.HateoasSelfLink,
        task_id: str,
    ) -> None:
        """Constructor for the OnDemandEC2MSSQLDatabaseBackupResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded = embedded
        self.links: (
            create_on_demand_ec2_mssql_database_backup_response_links_.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks
        ) = links
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.task_id: str = task_id

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
        val = dictionary['_embedded']
        val_embedded = (
            read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded.from_dictionary(val)
        )

        val = dictionary['_links']
        val_links = create_on_demand_ec2_mssql_database_backup_response_links_.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks.from_dictionary(
            val
        )

        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_p_self,  # type: ignore
            val_task_id,  # type: ignore
        )
