#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import notification_setting as notification_setting_
from clumioapi.models import parameter as parameter_
from clumioapi.models import schedule_setting as schedule_setting_
import requests

T = TypeVar('T', bound='CreateComplianceReportConfigurationV1Request')


@dataclasses.dataclass
class CreateComplianceReportConfigurationV1Request:
    """Implementation of the 'CreateComplianceReportConfigurationV1Request' model.

        Attributes:
            Description:
                The user-provided description of the compliance report configuration.

            Name:
                The user-provided name of the compliance report configuration.

            Notification:
                Notification channels to send the generated report runs.

            Parameter:
                Filter and control parameters of compliance report.

            Schedule:
                When the report will be generated and sent. if the schedule is not provided then a
    default value will be used.

    """

    Description: str | None = None
    Name: str | None = None
    Notification: notification_setting_.NotificationSetting | None = None
    Parameter: parameter_.Parameter | None = None
    Schedule: schedule_setting_.ScheduleSetting | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
