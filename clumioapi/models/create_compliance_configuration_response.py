#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import compliance_configuration_links as compliance_configuration_links_
from clumioapi.models import latest_run as latest_run_
from clumioapi.models import notification_setting as notification_setting_
from clumioapi.models import parameter as parameter_
from clumioapi.models import schedule_setting as schedule_setting_
import requests

T = TypeVar('T', bound='CreateComplianceConfigurationResponse')


@dataclasses.dataclass
class CreateComplianceConfigurationResponse:
    """Implementation of the 'CreateComplianceConfigurationResponse' model.

    Attributes:
        Embedded:
            If the `embed` query parameter is set, displays the responses of the related
            resource,
            as defined by the embeddable link specified.

        Links:
            Urls to pages related to the resource.

        Created:
            The rfc3339 format time when the report configuration was created.

        Description:
            The user-provided description of the compliance report configuration.

        Id:
            The unique identifier of the report configuration.

        LatestRun:
            Most recent report run generated from the report configuration.

        Name:
            The user-provided name of the compliance report configuration.

        Notification:
            Notification channels to send the generated report runs.

        Parameter:
            Filter and control parameters of compliance report.

        Schedule:
            When the report will be generated and sent. if the schedule is not provided then
            a
            default value will be used.

    """

    Embedded: object | None = None
    Links: compliance_configuration_links_.ComplianceConfigurationLinks | None = None
    Created: str | None = None
    Description: str | None = None
    Id: str | None = None
    LatestRun: latest_run_.LatestRun | None = None
    Name: str | None = None
    Notification: notification_setting_.NotificationSetting | None = None
    Parameter: parameter_.Parameter | None = None
    Schedule: schedule_setting_.ScheduleSetting | None = None
    raw_response: Optional[requests.Response] = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val_id = val

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
            val_id,
            val_latest_run,
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
        model_instance.raw_response = response
        return model_instance
