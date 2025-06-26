#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_info
from clumioapi.models import compliance_run_hateoas_links
from clumioapi.models import parameter

T = TypeVar('T', bound='ComplianceRun')


class ComplianceRun:
    """Implementation of the 'ComplianceRun' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
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
    _names = {
        'embedded': '_embedded',
        'links': '_links',
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
        embedded: object = None,
        links: compliance_run_hateoas_links.ComplianceRunHateoasLinks = None,
        compliance_info: compliance_info.ComplianceInfo = None,
        created: str = None,
        expired: str = None,
        p_id: str = None,
        name: str = None,
        parameter: parameter.Parameter = None,
        report_config_id: str = None,
        report_download_link: str = None,
        status: str = None,
        task_id: str = None,
        updated: str = None,
    ) -> None:
        """Constructor for the ComplianceRun class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: compliance_run_hateoas_links.ComplianceRunHateoasLinks = links
        self.compliance_info: compliance_info.ComplianceInfo = compliance_info
        self.created: str = created
        self.expired: str = expired
        self.p_id: str = p_id
        self.name: str = name
        self.parameter: parameter.Parameter = parameter
        self.report_config_id: str = report_config_id
        self.report_download_link: str = report_download_link
        self.status: str = status
        self.task_id: str = task_id
        self.updated: str = updated

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

        key = 'compliance_info'
        p_compliance_info = (
            compliance_info.ComplianceInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        created = dictionary.get('created')
        expired = dictionary.get('expired')
        p_id = dictionary.get('id')
        name = dictionary.get('name')
        key = 'parameter'
        p_parameter = (
            parameter.Parameter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        report_config_id = dictionary.get('report_config_id')
        report_download_link = dictionary.get('report_download_link')
        status = dictionary.get('status')
        task_id = dictionary.get('task_id')
        updated = dictionary.get('updated')
        # Return an object of this model
        return cls(
            embedded,
            links,
            p_compliance_info,
            created,
            expired,
            p_id,
            name,
            p_parameter,
            report_config_id,
            report_download_link,
            status,
            task_id,
            updated,
        )
