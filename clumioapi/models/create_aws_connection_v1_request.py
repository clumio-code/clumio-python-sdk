#
# Copyright 2023. Clumio, Inc.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception

T = TypeVar('T', bound='CreateAwsConnectionV1Request')

ProtectAssetTypesEnabledValues = [
    'EBS',
    'RDS',
    'DynamoDB',
    'EC2MSSQL',
    'S3',
]


class CreateAwsConnectionV1Request:
    """Implementation of the 'CreateAwsConnectionV1Request' model.

    Attributes:
        account_native_id:
            The AWS-assigned ID of the account associated with the connection.
        aws_region:
            The AWS region associated with the connection. For example, `us-east-1`.
        description:
            The user-provided description for this connection.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            AWS environment. If this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. For more information about organizational units, refer to the
            Organizational-Units documentation.
        protect_asset_types_enabled:
            The asset types enabled for protect.
            Valid values are any of ["EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3"].
        services_enabled:
            The services to be enabled for this configuration. Valid values are
            ["discover"], ["discover", "protect"]. This is only set when the
            registration is created, the enabled services are obtained directly from
            the installed template after that. (Deprecated as all connections will have
            both discover and protect enabled)
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'description': 'description',
        'organizational_unit_id': 'organizational_unit_id',
        'protect_asset_types_enabled': 'protect_asset_types_enabled',
        'services_enabled': 'services_enabled',
    }

    def __init__(
        self,
        account_native_id: str = None,
        aws_region: str = None,
        description: str = None,
        organizational_unit_id: str = None,
        protect_asset_types_enabled: Sequence[str] = None,
        services_enabled: Sequence[str] = None,
    ) -> None:
        """Constructor for the CreateAwsConnectionV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id
        self.aws_region: str = aws_region
        self.description: str = description
        self.organizational_unit_id: str = organizational_unit_id

        for enum_value in protect_asset_types_enabled:
            if enum_value not in ProtectAssetTypesEnabledValues:
                raise clumio_exception.ClumioException(
                    f'Invalid value for protect_asset_types_enabled: {enum_value}. Valid values are { ProtectAssetTypesEnabledValues }.',
                    None,
                )
        self.protect_asset_types_enabled: Sequence[str] = protect_asset_types_enabled
        self.services_enabled: Sequence[str] = services_enabled

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
        account_native_id = dictionary.get('account_native_id')
        aws_region = dictionary.get('aws_region')
        description = dictionary.get('description')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        protect_asset_types_enabled = dictionary.get('protect_asset_types_enabled')
        services_enabled = dictionary.get('services_enabled')
        # Return an object of this model
        return cls(
            account_native_id,
            aws_region,
            description,
            organizational_unit_id,
            protect_asset_types_enabled,
            services_enabled,
        )
