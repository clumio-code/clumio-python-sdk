#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateAwsConnectionGroupV1Request')


class CreateAwsConnectionGroupV1Request:
    """Implementation of the 'CreateAwsConnectionGroupV1Request' model.

    The body of the request.

    Attributes:
        account_native_id:
            The AWS-assigned ID of the account to be associated with the Connection Group.
        asset_types:
            The asset types to be connected via the connection-group.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "Iceberg"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        asset_types_enabled:
            DEPRECATED, use "asset_types" instead.

            The asset types to be connected via the connection-group.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "Iceberg"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        aws_regions:
            The AWS regions to be associated with the Connection Group.
        description:
            Description for this connection group.
        master_aws_account_id:
            The AWS Account that manages the connection-group's stack.
            If the provided master_aws_account_id different than the account_native_id then
            use service managed permissions while deploying stack.
        master_region:
            The AWS Region that manages the connection-group's stack.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the
            AWS environment. If this parameter is not provided, then the value
            defaults to the first organizational unit assigned to the requesting
            user. For more information about organizational units, refer to the
            Organizational-Units documentation.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'account_native_id': 'account_native_id',
        'asset_types': 'asset_types',
        'asset_types_enabled': 'asset_types_enabled',
        'aws_regions': 'aws_regions',
        'description': 'description',
        'master_aws_account_id': 'master_aws_account_id',
        'master_region': 'master_region',
        'organizational_unit_id': 'organizational_unit_id',
    }

    def __init__(
        self,
        account_native_id: str,
        asset_types: Sequence[str],
        asset_types_enabled: Sequence[str],
        aws_regions: Sequence[str],
        description: str,
        master_aws_account_id: str,
        master_region: str,
        organizational_unit_id: str,
    ) -> None:
        """Constructor for the CreateAwsConnectionGroupV1Request class."""

        # Initialize members of the class
        self.account_native_id: str = account_native_id
        self.asset_types: Sequence[str] = asset_types
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_regions: Sequence[str] = aws_regions
        self.description: str = description
        self.master_aws_account_id: str = master_aws_account_id
        self.master_region: str = master_region
        self.organizational_unit_id: str = organizational_unit_id

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
        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['asset_types']
        val_asset_types = val

        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['aws_regions']
        val_aws_regions = val

        val = dictionary['description']
        val_description = val

        val = dictionary['master_aws_account_id']
        val_master_aws_account_id = val

        val = dictionary['master_region']
        val_master_region = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        # Return an object of this model
        return cls(
            val_account_native_id,  # type: ignore
            val_asset_types,  # type: ignore
            val_asset_types_enabled,  # type: ignore
            val_aws_regions,  # type: ignore
            val_description,  # type: ignore
            val_master_aws_account_id,  # type: ignore
            val_master_region,  # type: ignore
            val_organizational_unit_id,  # type: ignore
        )
