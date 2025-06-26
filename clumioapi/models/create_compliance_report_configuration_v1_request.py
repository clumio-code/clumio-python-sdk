#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import notification_setting
from clumioapi.models import parameter
from clumioapi.models import schedule_setting

T = TypeVar('T', bound='CreateComplianceReportConfigurationV1Request')


class CreateComplianceReportConfigurationV1Request:
    """Implementation of the 'CreateComplianceReportConfigurationV1Request' model.

    Attributes:
        description:
            The user-provided description of the compliance report configuration.
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
        'description': 'description',
        'name': 'name',
        'notification': 'notification',
        'parameter': 'parameter',
        'schedule': 'schedule',
    }

    def __init__(
        self,
        description: str = None,
        name: str = None,
        notification: notification_setting.NotificationSetting = None,
        parameter: parameter.Parameter = None,
        schedule: schedule_setting.ScheduleSetting = None,
    ) -> None:
        """Constructor for the CreateComplianceReportConfigurationV1Request class."""

        # Initialize members of the class
        self.description: str = description
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
        description = dictionary.get('description')
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
        return cls(description, name, notification, p_parameter, schedule)
