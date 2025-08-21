#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import on_demand_setting as on_demand_setting_

T = TypeVar('T', bound='CreateBackupEc2MssqlDatabaseV1Request')

TypeValues = [
    'ec2_mssql_database_backup',
    'ec2_mssql_log_backup',
]


class CreateBackupEc2MssqlDatabaseV1Request:
    """Implementation of the 'CreateBackupEc2MssqlDatabaseV1Request' model.

    Attributes:
        asset_id:
            Performs the operation on the MSSQL asset with the specified Clumio-assigned ID.
        settings:
            Settings for requesting on-demand backup directly.
        p_type:
            The type of the backup.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'asset_id': 'asset_id', 'settings': 'settings', 'p_type': 'type'}

    def __init__(
        self,
        asset_id: str | None = None,
        settings: on_demand_setting_.OnDemandSetting | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the CreateBackupEc2MssqlDatabaseV1Request class."""

        # Initialize members of the class
        self.asset_id: str | None = asset_id
        self.settings: on_demand_setting_.OnDemandSetting | None = settings

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.'
            )
        self.p_type: str | None = p_type

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
        val = dictionary.get('asset_id', None)
        val_asset_id = val

        val = dictionary.get('settings', None)
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_asset_id,
            val_settings,
            val_p_type,
        )
