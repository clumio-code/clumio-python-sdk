#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import on_demand_setting as on_demand_setting_
import requests

T = TypeVar('T', bound='CreateBackupAwsDynamodbTableV1Request')

TypeValues = [
    'clumio_backup',
    'aws_snapshot',
]


@dataclasses.dataclass
class CreateBackupAwsDynamodbTableV1Request:
    """Implementation of the 'CreateBackupAwsDynamodbTableV1Request' model.

        Attributes:
            Settings:
    Settings for requesting on-demand backup directly.

            TableId:
    Performs the operation on the dynamodb table with the specified clumio-assigned id.

            Type:
    The type of the backup. possible values - `clumio_backup`, `aws_snapshot`. the
    type will be assumed as `aws_snapshot` if the field is left empty.

    """

    Settings: on_demand_setting_.OnDemandSetting | None = None
    TableId: str | None = None

    Type: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self,
            dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v not in [None, {}]},
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
        val = dictionary.get('settings', None)
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary.get('table_id', None)
        val_table_id = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_settings,
            val_table_id,
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
