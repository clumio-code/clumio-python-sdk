#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_info as compliance_info_
from clumioapi.models import parameter as parameter_

T = TypeVar('T', bound='LatestRun')


class LatestRun:
    """Implementation of the 'LatestRun' model.

    Most recent report run generated from the report configuration.

    Attributes:
        compliance_info:
            The status per controls in the compliance report created by the report run.
        created:
            The RFC3339 format time when the report run was created.
        expired:
            The RFC3339 format time when the report run was expired.
        p_id:
            The unique identifier of the report run.
        name:
            The name of the report run.
        parameter:
            Filter and control parameters of compliance report.
        report_config_id:
            The unique identifier of the report configuration from which the report run was
            generated.
        report_download_link:
            The link to download the report CSV.
        status:
            The generation status of the report run.
        task_id:
            The ID of the report run generation task.
        updated:
            The RFC3339 format time when the report run was updated.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'compliance_info': 'compliance_info',
        'created': 'created',
        'expired': 'expired',
        'p_id': 'id',
        'name': 'name',
        'parameter': 'parameter',
        'report_config_id': 'report_config_id',
        'report_download_link': 'report_download_link',
        'status': 'status',
        'task_id': 'task_id',
        'updated': 'updated',
    }

    def __init__(
        self,
        compliance_info: compliance_info_.ComplianceInfo | None = None,
        created: str | None = None,
        expired: str | None = None,
        p_id: str | None = None,
        name: str | None = None,
        parameter: parameter_.Parameter | None = None,
        report_config_id: str | None = None,
        report_download_link: str | None = None,
        status: str | None = None,
        task_id: str | None = None,
        updated: str | None = None,
    ) -> None:
        """Constructor for the LatestRun class."""

        # Initialize members of the class
        self.compliance_info: compliance_info_.ComplianceInfo | None = compliance_info
        self.created: str | None = created
        self.expired: str | None = expired
        self.p_id: str | None = p_id
        self.name: str | None = name
        self.parameter: parameter_.Parameter | None = parameter
        self.report_config_id: str | None = report_config_id
        self.report_download_link: str | None = report_download_link
        self.status: str | None = status
        self.task_id: str | None = task_id
        self.updated: str | None = updated

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
        val = dictionary.get('compliance_info', None)
        val_compliance_info = compliance_info_.ComplianceInfo.from_dictionary(val)

        val = dictionary.get('created', None)
        val_created = val

        val = dictionary.get('expired', None)
        val_expired = val

        val = dictionary.get('id', None)
        val_p_id = val

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
            val_compliance_info,
            val_created,
            val_expired,
            val_p_id,
            val_name,
            val_parameter,
            val_report_config_id,
            val_report_download_link,
            val_status,
            val_task_id,
            val_updated,
        )
