#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_configuration_links as compliance_configuration_links_
from clumioapi.models import latest_run as latest_run_
from clumioapi.models import notification_setting as notification_setting_
from clumioapi.models import parameter as parameter_
from clumioapi.models import schedule_setting as schedule_setting_

T = TypeVar('T', bound='UpdateComplianceConfigurationResponse')


class UpdateComplianceConfigurationResponse:
    """Implementation of the 'UpdateComplianceConfigurationResponse' model.

    Attributes:
        embedded:
            If the `embed` query parameter is set, displays the responses of the related
            resource,
            as defined by the embeddable link specified.
        links:
            URLs to pages related to the resource.
        created:
            The RFC3339 format time when the report configuration was created.
        description:
            The user-provided description of the compliance report configuration.
        p_id:
            The unique identifier of the report configuration.
        latest_run:
            Most recent report run generated from the report configuration.
        name:
            The user-provided name of the compliance report configuration.
        notification:
            Notification channels to send the generated report runs.
        parameter:
            Filter and control parameters of compliance report.
        schedule:
            When the report will be generated and sent. If the schedule is not provided then
            a
            default value will be used.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'created': 'created',
        'description': 'description',
        'p_id': 'id',
        'latest_run': 'latest_run',
        'name': 'name',
        'notification': 'notification',
        'parameter': 'parameter',
        'schedule': 'schedule',
    }

    def __init__(
        self,
        embedded: object,
        links: compliance_configuration_links_.ComplianceConfigurationLinks,
        created: str,
        description: str,
        p_id: str,
        latest_run: latest_run_.LatestRun,
        name: str,
        notification: notification_setting_.NotificationSetting,
        parameter: parameter_.Parameter,
        schedule: schedule_setting_.ScheduleSetting,
    ) -> None:
        """Constructor for the UpdateComplianceConfigurationResponse class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: compliance_configuration_links_.ComplianceConfigurationLinks = links
        self.created: str = created
        self.description: str = description
        self.p_id: str = p_id
        self.latest_run: latest_run_.LatestRun = latest_run
        self.name: str = name
        self.notification: notification_setting_.NotificationSetting = notification
        self.parameter: parameter_.Parameter = parameter
        self.schedule: schedule_setting_.ScheduleSetting = schedule

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
        val = dictionary['_embedded']
        val_embedded = val

        val = dictionary['_links']
        val_links = compliance_configuration_links_.ComplianceConfigurationLinks.from_dictionary(
            val
        )

        val = dictionary['created']
        val_created = val

        val = dictionary['description']
        val_description = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['latest_run']
        val_latest_run = latest_run_.LatestRun.from_dictionary(val)

        val = dictionary['name']
        val_name = val

        val = dictionary['notification']
        val_notification = notification_setting_.NotificationSetting.from_dictionary(val)

        val = dictionary['parameter']
        val_parameter = parameter_.Parameter.from_dictionary(val)

        val = dictionary['schedule']
        val_schedule = schedule_setting_.ScheduleSetting.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_created,  # type: ignore
            val_description,  # type: ignore
            val_p_id,  # type: ignore
            val_latest_run,  # type: ignore
            val_name,  # type: ignore
            val_notification,  # type: ignore
            val_parameter,  # type: ignore
            val_schedule,  # type: ignore
        )
