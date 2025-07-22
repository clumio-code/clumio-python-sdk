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
        description: str,
        name: str,
        notification: notification_setting_.NotificationSetting,
        parameter: parameter_.Parameter,
        schedule: schedule_setting_.ScheduleSetting,
    ) -> None:
        """Constructor for the UpdateComplianceReportConfigurationV1Request class."""

        # Initialize members of the class
        self.description: str = description
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
        val = dictionary['description']
        val_description = val

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
            val_description,  # type: ignore
            val_name,  # type: ignore
            val_notification,  # type: ignore
            val_parameter,  # type: ignore
            val_schedule,  # type: ignore
        )
