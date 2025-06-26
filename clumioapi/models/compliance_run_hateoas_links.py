#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

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
    _names = {
        'p_self': '_self',
        'delete_compliance_report_run': 'delete-compliance-report-run',
        'send_compliance_report_run_email': 'send-compliance-report-run-email',
    }

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        delete_compliance_report_run: hateoas_link.HateoasLink = None,
        send_compliance_report_run_email: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the ComplianceRunHateoasLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.delete_compliance_report_run: hateoas_link.HateoasLink = delete_compliance_report_run
        self.send_compliance_report_run_email: hateoas_link.HateoasLink = (
            send_compliance_report_run_email
        )

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'delete-compliance-report-run'
        delete_compliance_report_run = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'send-compliance-report-run-email'
        send_compliance_report_run_email = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, delete_compliance_report_run, send_compliance_report_run_email)
