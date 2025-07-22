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
        embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded,
        links: create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks,
        task_id: str,
    ) -> None:
        """Constructor for the CreateComplianceRunResponse class."""

        # Initialize members of the class
        self.embedded: read_task_hateoas_outer_embedded_.ReadTaskHateoasOuterEmbedded = embedded
        self.links: create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks = links
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
        val_links = (
            create_compliance_run_hateoas_links_.CreateComplianceRunHateoasLinks.from_dictionary(
                val
            )
        )

        val = dictionary['task_id']
        val_task_id = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_task_id,  # type: ignore
        )
