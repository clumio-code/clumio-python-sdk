#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_first_link as hateoas_first_link_
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_next_link as hateoas_next_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='ComplianceConfigurationListLinks')


class ComplianceConfigurationListLinks:
    """Implementation of the 'ComplianceConfigurationListLinks' model.

    URLs to pages related to the resource.

    Attributes:
        first:
            The HATEOAS link to the first page of results.
        p_next:
            The HATEOAS link to the next page of results.
        p_self:
            The HATEOAS link to this resource.
        create_compliance_report_configuration:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'first': '_first',
        'p_next': '_next',
        'p_self': '_self',
        'create_compliance_report_configuration': 'create-compliance-report-configuration',
    }

    def __init__(
        self,
        first: hateoas_first_link_.HateoasFirstLink,
        p_next: hateoas_next_link_.HateoasNextLink,
        p_self: hateoas_self_link_.HateoasSelfLink,
        create_compliance_report_configuration: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the ComplianceConfigurationListLinks class."""

        # Initialize members of the class
        self.first: hateoas_first_link_.HateoasFirstLink = first
        self.p_next: hateoas_next_link_.HateoasNextLink = p_next
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.create_compliance_report_configuration: hateoas_link_.HateoasLink = (
            create_compliance_report_configuration
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

        # Extract variables from the dictionary
        val = dictionary['_first']
        val_first = hateoas_first_link_.HateoasFirstLink.from_dictionary(val)

        val = dictionary['_next']
        val_p_next = hateoas_next_link_.HateoasNextLink.from_dictionary(val)

        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['create-compliance-report-configuration']
        val_create_compliance_report_configuration = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_first,  # type: ignore
            val_p_next,  # type: ignore
            val_p_self,  # type: ignore
            val_create_compliance_report_configuration,  # type: ignore
        )
