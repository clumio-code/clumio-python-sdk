#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_
import requests

T = TypeVar('T', bound='ComplianceRunHateoasLinks')


@dataclasses.dataclass
class ComplianceRunHateoasLinks:
    """Implementation of the 'ComplianceRunHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        Self:
            The hateoas link to this resource.

        DeleteComplianceReportRun:
            A resource-specific hateoas link.

        SendComplianceReportRunEmail:
            A resource-specific hateoas link.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Self': '_self',
        'DeleteComplianceReportRun': 'delete-compliance-report-run',
        'SendComplianceReportRunEmail': 'send-compliance-report-run-email',
    }

    Self: hateoas_self_link_.HateoasSelfLink | None = None
    DeleteComplianceReportRun: hateoas_link_.HateoasLink | None = None
    SendComplianceReportRunEmail: hateoas_link_.HateoasLink | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_self', None)
        val_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('delete-compliance-report-run', None)
        val_delete_compliance_report_run = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('send-compliance-report-run-email', None)
        val_send_compliance_report_run_email = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_self,
            val_delete_compliance_report_run,
            val_send_compliance_report_run_email,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
