#
# Copyright 2023. Clumio, A Commvault Company.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception
from clumioapi.models import on_demand_setting as on_demand_setting_

T = TypeVar('T', bound='CreateBackupAwsDynamodbTableV1Request')

TypeValues = [
    'clumio_backup',
    'aws_snapshot',
]


class CreateBackupAwsDynamodbTableV1Request:
    """Implementation of the 'CreateBackupAwsDynamodbTableV1Request' model.

    Attributes:
        settings:
            Settings for requesting on-demand backup directly.
        table_id:
            Performs the operation on the DynamoDB table with the specified Clumio-assigned
            ID.
        p_type:
            The type of the backup. Possible values - `clumio_backup`, `aws_snapshot`. The
            type will be assumed as `aws_snapshot` if the field is left empty.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'settings': 'settings', 'table_id': 'table_id', 'p_type': 'type'}

    def __init__(
        self, settings: on_demand_setting_.OnDemandSetting, table_id: str, p_type: str
    ) -> None:
        """Constructor for the CreateBackupAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting_.OnDemandSetting = settings
        self.table_id: str = table_id

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.',
                None,
            )
        self.p_type: str = p_type

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
        val = dictionary['settings']
        val_settings = on_demand_setting_.OnDemandSetting.from_dictionary(val)

        val = dictionary['table_id']
        val_table_id = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_settings,  # type: ignore
            val_table_id,  # type: ignore
            val_p_type,  # type: ignore
        )
