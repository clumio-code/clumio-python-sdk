#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import on_demand_setting as on_demand_setting_
import requests

T = TypeVar('T', bound='CreateBackupAwsEc2InstanceV1Request')


@dataclasses.dataclass
class CreateBackupAwsEc2InstanceV1Request:
    """Implementation of the 'CreateBackupAwsEc2InstanceV1Request' model.

    Attributes:
        InstanceId:
            Performs the operation on the ec2 instance with the specified clumio-assigned
            id.

        Settings:
            Settings for requesting on-demand backup directly.

        Type:
            The type of the backup. possible values - `clumio_backup`, `aws_snapshot`. the
            type will be assumed as `clumio_backup` if the field is left empty.

    """

    InstanceId: str | None = None
    Settings: on_demand_setting_.OnDemandSetting | None = None
    Type: str | None = None

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
        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('settings', None)
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_instance_id,
            val_settings,
            val_type,
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
