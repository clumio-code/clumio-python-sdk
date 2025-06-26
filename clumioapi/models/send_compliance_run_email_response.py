#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_run_hateoas_links

T = TypeVar('T', bound='SendComplianceRunEmailResponse')


class SendComplianceRunEmailResponse:
    """Implementation of the 'SendComplianceRunEmailResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
    """

    # Create a mapping from Model property names to API property names
    _names = {'embedded': '_embedded', 'links': '_links'}

    def __init__(
        self,
        embedded: object = None,
        links: compliance_run_hateoas_links.ComplianceRunHateoasLinks = None,
    ) -> None:
        """Constructor for the SendComplianceRunEmailResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: compliance_run_hateoas_links.ComplianceRunHateoasLinks = links

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
        embedded = dictionary.get('_embedded')
        key = '_links'
        links = (
            compliance_run_hateoas_links.ComplianceRunHateoasLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(embedded, links)
