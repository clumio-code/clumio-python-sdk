#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import compliance_info as compliance_info_
from clumioapi.models import compliance_run_hateoas_links as compliance_run_hateoas_links_
from clumioapi.models import parameter as parameter_
import requests

T = TypeVar('T', bound='ComplianceRun')


@dataclasses.dataclass
class ComplianceRun:
    """Implementation of the 'ComplianceRun' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        ComplianceInfo:
            The status per controls in the compliance report created by the report run.

        Created:
            The rfc3339 format time when the report run was created.

        Expired:
            The rfc3339 format time when the report run was expired.

        Id:
            The unique identifier of the report run.

        Name:
            The name of the report run.

        Parameter:
            Filter and control parameters of compliance report.

        ReportConfigId:
            The unique identifier of the report configuration from which the report run was
            generated.

        ReportDownloadLink:
            The link to download the report csv.

        Status:
            The generation status of the report run.

        TaskId:
            The id of the report run generation task.

        Updated:
            The rfc3339 format time when the report run was updated.

    """

    Embedded: object | None = None
    Links: compliance_run_hateoas_links_.ComplianceRunHateoasLinks | None = None
    ComplianceInfo: compliance_info_.ComplianceInfo | None = None
    Created: str | None = None
    Expired: str | None = None
    Id: str | None = None
    Name: str | None = None
    Parameter: parameter_.Parameter | None = None
    ReportConfigId: str | None = None
    ReportDownloadLink: str | None = None
    Status: str | None = None
    TaskId: str | None = None
    Updated: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = compliance_run_hateoas_links_.ComplianceRunHateoasLinks.from_dictionary(val)

        val = dictionary.get('compliance_info', None)
        val_compliance_info = compliance_info_.ComplianceInfo.from_dictionary(val)

        val = dictionary.get('created', None)
        val_created = val

        val = dictionary.get('expired', None)
        val_expired = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('parameter', None)
        val_parameter = parameter_.Parameter.from_dictionary(val)

        val = dictionary.get('report_config_id', None)
        val_report_config_id = val

        val = dictionary.get('report_download_link', None)
        val_report_download_link = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        val = dictionary.get('updated', None)
        val_updated = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_compliance_info,
            val_created,
            val_expired,
            val_id,
            val_name,
            val_parameter,
            val_report_config_id,
            val_report_download_link,
            val_status,
            val_task_id,
            val_updated,
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
