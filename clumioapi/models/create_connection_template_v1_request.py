#
# Copyright 2021. Clumio, Inc.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception

T = TypeVar('T', bound='CreateConnectionTemplateV1Request')

AssetTypesEnabledValues = [
    'EBS',
    'RDS',
    'DynamoDB',
    'EC2MSSQL',
    'S3',
]


class CreateConnectionTemplateV1Request:
    """Implementation of the 'CreateConnectionTemplateV1Request' model.

    Attributes:
        asset_types_enabled:
            The asset types for which the template is to be generated. Possible
            asset types are ["EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3"].
    """

    # Create a mapping from Model property names to API property names
    _names = {'asset_types_enabled': 'asset_types_enabled'}

    def __init__(self, asset_types_enabled: Sequence[str] = None) -> None:
        """Constructor for the CreateConnectionTemplateV1Request class."""

        # Initialize members of the class

        for enum_value in asset_types_enabled:
            if enum_value not in AssetTypesEnabledValues:
                raise clumio_exception.ClumioException(
                    f'Invalid value for asset_types_enabled: {enum_value}. Valid values are { AssetTypesEnabledValues }.',
                    None,
                )
        self.asset_types_enabled: Sequence[str] = asset_types_enabled

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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        # Return an object of this model
        return cls(asset_types_enabled)
