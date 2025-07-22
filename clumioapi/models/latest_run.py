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
        compliance_info: compliance_info_.ComplianceInfo,
        created: str,
        expired: str,
        p_id: str,
        name: str,
        parameter: parameter_.Parameter,
        report_config_id: str,
        report_download_link: str,
        status: str,
        task_id: str,
        updated: str,
    ) -> None:
        """Constructor for the LatestRun class."""

        # Initialize members of the class
        self.compliance_info: compliance_info_.ComplianceInfo = compliance_info
        self.created: str = created
        self.expired: str = expired
        self.p_id: str = p_id
        self.name: str = name
        self.parameter: parameter_.Parameter = parameter
        self.report_config_id: str = report_config_id
        self.report_download_link: str = report_download_link
        self.status: str = status
        self.task_id: str = task_id
        self.updated: str = updated

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
        val = dictionary['compliance_info']
        val_compliance_info = compliance_info_.ComplianceInfo.from_dictionary(val)

        val = dictionary['created']
        val_created = val

        val = dictionary['expired']
        val_expired = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['name']
        val_name = val

        val = dictionary['parameter']
        val_parameter = parameter_.Parameter.from_dictionary(val)

        val = dictionary['report_config_id']
        val_report_config_id = val

        val = dictionary['report_download_link']
        val_report_download_link = val

        val = dictionary['status']
        val_status = val

        val = dictionary['task_id']
        val_task_id = val

        val = dictionary['updated']
        val_updated = val

        # Return an object of this model
        return cls(
            val_compliance_info,  # type: ignore
            val_created,  # type: ignore
            val_expired,  # type: ignore
            val_p_id,  # type: ignore
            val_name,  # type: ignore
            val_parameter,  # type: ignore
            val_report_config_id,  # type: ignore
            val_report_download_link,  # type: ignore
            val_status,  # type: ignore
            val_task_id,  # type: ignore
            val_updated,  # type: ignore
        )
