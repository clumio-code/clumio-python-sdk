#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import on_demand_setting

T = TypeVar('T', bound='CreateBackupAwsDynamodbTableV1Request')


class CreateBackupAwsDynamodbTableV1Request:
    """Implementation of the 'CreateBackupAwsDynamodbTableV1Request' model.

    Attributes:
        settings:
            Settings for requesting on-demand backup directly.
        table_id:
            Performs the operation on the DynamoDB table with the specified Clumio-assigned
            ID.
        type:
            The type of the backup. Possible values - `clumio_backup`, `aws_snapshot`. The
            type will be assumed as `aws_snapshot` if the field is left empty.
    """

    # Create a mapping from Model property names to API property names
    _names = {'settings': 'settings', 'table_id': 'table_id', 'type': 'type'}

    def __init__(
        self,
        settings: on_demand_setting.OnDemandSetting = None,
        table_id: str = None,
        type: str = None,
    ) -> None:
        """Constructor for the CreateBackupAwsDynamodbTableV1Request class."""

        # Initialize members of the class
        self.settings: on_demand_setting.OnDemandSetting = settings
        self.table_id: str = table_id
        self.type: str = type

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
        key = 'settings'
        settings = (
            on_demand_setting.OnDemandSetting.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        table_id = dictionary.get('table_id')
        type = dictionary.get('type')
        # Return an object of this model
        return cls(settings, table_id, type)
