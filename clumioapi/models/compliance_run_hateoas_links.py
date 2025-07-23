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
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        delete_compliance_report_run: hateoas_link_.HateoasLink | None = None,
        send_compliance_report_run_email: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the ComplianceRunHateoasLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.delete_compliance_report_run: hateoas_link_.HateoasLink | None = (
            delete_compliance_report_run
        )
        self.send_compliance_report_run_email: hateoas_link_.HateoasLink | None = (
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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('delete-compliance-report-run', None)
        val_delete_compliance_report_run = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('send-compliance-report-run-email', None)
        val_send_compliance_report_run_email = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_delete_compliance_report_run,
            val_send_compliance_report_run_email,
        )
