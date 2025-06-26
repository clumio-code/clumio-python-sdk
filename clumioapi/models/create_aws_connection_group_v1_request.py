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
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        asset_types_enabled:
            DEPRECATED, use "asset_types" instead.

            The asset types to be connected via the connection-group.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS"].

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
    _names = {
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
        account_native_id: str = None,
        asset_types: Sequence[str] = None,
        asset_types_enabled: Sequence[str] = None,
        aws_regions: Sequence[str] = None,
        description: str = None,
        master_aws_account_id: str = None,
        master_region: str = None,
        organizational_unit_id: str = None,
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
        asset_types = dictionary.get('asset_types')
        asset_types_enabled = dictionary.get('asset_types_enabled')
        aws_regions = dictionary.get('aws_regions')
        description = dictionary.get('description')
        master_aws_account_id = dictionary.get('master_aws_account_id')
        master_region = dictionary.get('master_region')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        # Return an object of this model
        return cls(
            account_native_id,
            asset_types,
            asset_types_enabled,
            aws_regions,
            description,
            master_aws_account_id,
            master_region,
            organizational_unit_id,
        )
