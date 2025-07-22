#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    create_ec2_mssql_database_restore_response_links as \
    create_ec2_mssql_database_restore_response_links_
from clumioapi.models import read_task_hateoas_outer_embedded as read_task_hateoas_outer_embedded_

T = TypeVar('T', bound='CreateEC2MSSQLDatabaseRestoreResponse')


class CreateEC2MSSQLDatabaseRestoreResponse:
    """Implementation of the 'CreateEC2MSSQLDatabaseRestoreResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        task_id:
            The Clumio-assigned ID of the task created by this restore request.
            The progress of the task can be monitored using the
            `GET /tasks/{task_id}` endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded,
        links: create_ec2_mssql_database_restore_response_links_.CreateEC2MSSQLDatabaseRestoreResponseLinks,
        task_id: str,
    ) -> None:
        """Constructor for the CreateEC2MSSQLDatabaseRestoreResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded = embedded
        self.links: (
            create_ec2_mssql_database_restore_response_links_.CreateEC2MSSQLDatabaseRestoreResponseLinks
        ) = links
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
        val_links = create_ec2_mssql_database_restore_response_links_.CreateEC2MSSQLDatabaseRestoreResponseLinks.from_dictionary(
            val
        )

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_task_id,  # type: ignore
        )
