#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import notification_setting as notification_setting_
from clumioapi.models import parameter as parameter_
from clumioapi.models import schedule_setting as schedule_setting_

T = TypeVar('T', bound='UpdateComplianceReportConfigurationV1Request')


class UpdateComplianceReportConfigurationV1Request:
    """Implementation of the 'UpdateComplianceReportConfigurationV1Request' model.

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
    _names: dict[str, str] = {
        'description': 'description',
        'name': 'name',
        'notification': 'notification',
        'parameter': 'parameter',
        'schedule': 'schedule',
    }

    def __init__(
        self,
        description: str | None = None,
        name: str | None = None,
        notification: notification_setting_.NotificationSetting | None = None,
        parameter: parameter_.Parameter | None = None,
        schedule: schedule_setting_.ScheduleSetting | None = None,
    ) -> None:
        """Constructor for the UpdateComplianceReportConfigurationV1Request class."""

        # Initialize members of the class
        self.description: str | None = description
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
        val = dictionary.get('description', None)
        val_description = val

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
            val_description,
            val_name,
            val_notification,
            val_parameter,
            val_schedule,
        )
