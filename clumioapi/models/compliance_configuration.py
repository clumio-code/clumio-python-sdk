#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_configuration_links as compliance_configuration_links_
from clumioapi.models import latest_run as latest_run_
from clumioapi.models import notification_setting as notification_setting_
from clumioapi.models import parameter as parameter_
from clumioapi.models import schedule_setting as schedule_setting_

T = TypeVar('T', bound='ComplianceConfiguration')


class ComplianceConfiguration:
    """Implementation of the 'ComplianceConfiguration' model.

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
        embedded: object | None = None,
        links: compliance_configuration_links_.ComplianceConfigurationLinks | None = None,
        created: str | None = None,
        description: str | None = None,
        p_id: str | None = None,
        latest_run: latest_run_.LatestRun | None = None,
        name: str | None = None,
        notification: notification_setting_.NotificationSetting | None = None,
        parameter: parameter_.Parameter | None = None,
        schedule: schedule_setting_.ScheduleSetting | None = None,
    ) -> None:
        """Constructor for the ComplianceConfiguration class."""

        # Initialize members of the class
        self.embedded: object | None = embedded
        self.links: compliance_configuration_links_.ComplianceConfigurationLinks | None = links
        self.created: str | None = created
        self.description: str | None = description
        self.p_id: str | None = p_id
        self.latest_run: latest_run_.LatestRun | None = latest_run
        self.name: str | None = name
        self.notification: notification_setting_.NotificationSetting | None = notification
        self.parameter: parameter_.Parameter | None = parameter
        self.schedule: schedule_setting_.ScheduleSetting | None = schedule

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
        val = dictionary.get('_embedded', None)
        val_embedded = val

        val = dictionary.get('_links', None)
        val_links = compliance_configuration_links_.ComplianceConfigurationLinks.from_dictionary(
            val
        )

        val = dictionary.get('created', None)
        val_created = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('latest_run', None)
        val_latest_run = latest_run_.LatestRun.from_dictionary(val)

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('notification', None)
        val_notification = notification_setting_.NotificationSetting.from_dictionary(val)

        val = dictionary.get('parameter', None)
        val_parameter = parameter_.Parameter.from_dictionary(val)

        val = dictionary.get('schedule', None)
        val_schedule = schedule_setting_.ScheduleSetting.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_created,
            val_description,
            val_p_id,
            val_latest_run,
            val_name,
            val_notification,
            val_parameter,
            val_schedule,
        )
