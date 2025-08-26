#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import on_demand_setting as on_demand_setting_
import requests

T = TypeVar('T', bound='CreateBackupEc2MssqlDatabaseV1Request')

TypeValues = [
    'ec2_mssql_database_backup',
    'ec2_mssql_log_backup',
]


@dataclasses.dataclass
class CreateBackupEc2MssqlDatabaseV1Request:
    """Implementation of the 'CreateBackupEc2MssqlDatabaseV1Request' model.

    Attributes:
        AssetId:
            Performs the operation on the mssql asset with the specified clumio-assigned id.

        Settings:
            Settings for requesting on-demand backup directly.

        Type:
            The type of the backup.

    """

    AssetId: str | None = None
    Settings: on_demand_setting_.OnDemandSetting | None = None

    Type: str | None = None

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
        val = dictionary.get('asset_id', None)
        val_asset_id = val

        val = dictionary.get('settings', None)
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_asset_id,
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
