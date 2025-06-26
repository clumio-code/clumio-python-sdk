#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import compliance_configuration_links
from clumioapi.models import latest_run
from clumioapi.models import notification_setting
from clumioapi.models import parameter
from clumioapi.models import schedule_setting

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
    _names = {
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
        embedded: object = None,
        links: compliance_configuration_links.ComplianceConfigurationLinks = None,
        created: str = None,
        description: str = None,
        p_id: str = None,
        latest_run: latest_run.LatestRun = None,
        name: str = None,
        notification: notification_setting.NotificationSetting = None,
        parameter: parameter.Parameter = None,
        schedule: schedule_setting.ScheduleSetting = None,
    ) -> None:
        """Constructor for the ComplianceConfiguration class."""

        # Initialize members of the class
        self.embedded: object = embedded
        self.links: compliance_configuration_links.ComplianceConfigurationLinks = links
        self.created: str = created
        self.description: str = description
        self.p_id: str = p_id
        self.latest_run: latest_run.LatestRun = latest_run
        self.name: str = name
        self.notification: notification_setting.NotificationSetting = notification
        self.parameter: parameter.Parameter = parameter
        self.schedule: schedule_setting.ScheduleSetting = schedule

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
            compliance_configuration_links.ComplianceConfigurationLinks.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        created = dictionary.get('created')
        description = dictionary.get('description')
        p_id = dictionary.get('id')
        key = 'latest_run'
        p_latest_run = (
            latest_run.LatestRun.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        name = dictionary.get('name')
        key = 'notification'
        notification = (
            notification_setting.NotificationSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'parameter'
        p_parameter = (
            parameter.Parameter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'schedule'
        schedule = (
            schedule_setting.ScheduleSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            embedded,
            links,
            created,
            description,
            p_id,
            p_latest_run,
            name,
            notification,
            p_parameter,
            schedule,
        )
