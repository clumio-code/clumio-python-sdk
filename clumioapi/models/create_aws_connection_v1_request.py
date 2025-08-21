#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateAwsConnectionV1Request')


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
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "IcebergOnGlue"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        services_enabled:
            The services to be enabled for this configuration. Valid values are
            ["discover"], ["discover", "protect"]. This is only set when the
            registration is created, the enabled services are obtained directly from
            the installed template after that. (Deprecated as all connections will have
            both discover and protect enabled)
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'account_native_id': 'account_native_id',
        'aws_region': 'aws_region',
        'description': 'description',
        'organizational_unit_id': 'organizational_unit_id',
        'protect_asset_types_enabled': 'protect_asset_types_enabled',
        'services_enabled': 'services_enabled',
    }

    def __init__(
        self,
        account_native_id: str | None = None,
        aws_region: str | None = None,
        description: str | None = None,
        organizational_unit_id: str | None = None,
        protect_asset_types_enabled: Sequence[str] | None = None,
        services_enabled: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the CreateAwsConnectionV1Request class."""

        # Initialize members of the class
        self.account_native_id: str | None = account_native_id
        self.aws_region: str | None = aws_region
        self.description: str | None = description
        self.organizational_unit_id: str | None = organizational_unit_id
        self.protect_asset_types_enabled: Sequence[str] | None = protect_asset_types_enabled
        self.services_enabled: Sequence[str] | None = services_enabled

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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protect_asset_types_enabled', None)
        val_protect_asset_types_enabled = val

        val = dictionary.get('services_enabled', None)
        val_services_enabled = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_aws_region,
            val_description,
            val_organizational_unit_id,
            val_protect_asset_types_enabled,
            val_services_enabled,
        )
