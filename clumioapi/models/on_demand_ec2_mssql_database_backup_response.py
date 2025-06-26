#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import create_on_demand_ec2_mssql_database_backup_response_links
from clumioapi.models import hateoas_self_link
from clumioapi.models import read_task_hateoas_outer_embedded

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
    _names = {'embedded': '_embedded', 'links': '_links', 'p_self': '_self', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = None,
        links: create_on_demand_ec2_mssql_database_backup_response_links.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks = None,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        task_id: str = None,
    ) -> None:
        """Constructor for the OnDemandEC2MSSQLDatabaseBackupResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded = embedded
        self.links: (
            create_on_demand_ec2_mssql_database_backup_response_links.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks
        ) = links
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.task_id: str = task_id

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
        key = '_embedded'
        embedded = (
            read_task_hateoas_outer_embedded.ReadTaskHateoasOuterEmbedded.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            create_on_demand_ec2_mssql_database_backup_response_links.CreateOnDemandEC2MSSQLDatabaseBackupResponseLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        task_id = dictionary.get('task_id')
        # Return an object of this model
        return cls(embedded, links, p_self, task_id)
