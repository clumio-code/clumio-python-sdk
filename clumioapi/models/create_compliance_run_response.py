#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    create_compliance_run_hateoas_links as create_compliance_run_hateoas_links_
from clumioapi.models import read_task_hateoas_outer_embedded as read_task_hateoas_outer_embedded_

T = TypeVar('T', bound='CreateComplianceRunResponse')


class CreateComplianceRunResponse:
    """Implementation of the 'CreateComplianceRunResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            CreateComplianceRunHateoasLinks
            URLs to pages related to the resource.
        task_id:
            The Clumio-assigned ID of the task created for compliance report run generation.
            The progress of the task can be monitored using the `GET /tasks/{task_id}`
            endpoint.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links', 'task_id': 'task_id'}

    def __init__(
        self,
        embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded | None = None,
        links: create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks | None = None,
        task_id: str | None = None,
    ) -> None:
        """Constructor for the CreateComplianceRunResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded | None = (
            embedded
        )
        self.links: create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks | None = (
            links
        )
        self.task_id: str | None = task_id

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
        val = dictionary.get('_embedded', None)
        val_embedded = (
            read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded.from_dictionary(val)
        )

        val = dictionary.get('_links', None)
        val_links = (
            create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks.from_dictionary(
                val
            )
        )

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_task_id,
        )
