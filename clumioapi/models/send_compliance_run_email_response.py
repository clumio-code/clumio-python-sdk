#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_run_hateoas_links as compliance_run_hateoas_links_

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
    _names: dict[str, str] = {'embedded': '_embedded', 'links': '_links'}

    def __init__(
        self,
        embedded: object | None = None,
        links: compliance_run_hateoas_links_.ComplianceRunHateoasLinks | None = None,
    ) -> None:
        """Constructor for the SendComplianceRunEmailResponse class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: compliance_run_hateoas_links_.ComplianceRunHateoasLinks | None = links

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
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = compliance_run_hateoas_links_.ComplianceRunHateoasLinks.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
        )
