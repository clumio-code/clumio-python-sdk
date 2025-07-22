#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='ComplianceRunHateoasLinks')


class ComplianceRunHateoasLinks:
    """Implementation of the 'ComplianceRunHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_compliance_report_run:
            A resource-specific HATEOAS link.
        send_compliance_report_run_email:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_compliance_report_run': 'delete-compliance-report-run',
        'send_compliance_report_run_email': 'send-compliance-report-run-email',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        delete_compliance_report_run: hateoas_link_.HateoasLink,
        send_compliance_report_run_email: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the ComplianceRunHateoasLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.delete_compliance_report_run: hateoas_link_.HateoasLink = delete_compliance_report_run
        self.send_compliance_report_run_email: hateoas_link_.HateoasLink = (
            send_compliance_report_run_email
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
        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['delete-compliance-report-run']
        val_delete_compliance_report_run = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['send-compliance-report-run-email']
        val_send_compliance_report_run_email = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_delete_compliance_report_run,  # type: ignore
            val_send_compliance_report_run_email,  # type: ignore
        )
