#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateAwsConnectionGroupV1Request')


class UpdateAwsConnectionGroupV1Request:
    """Implementation of the 'UpdateAwsConnectionGroupV1Request' model.

    Attributes:
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
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types': 'asset_types',
        'asset_types_enabled': 'asset_types_enabled',
        'aws_regions': 'aws_regions',
        'description': 'description',
    }

    def __init__(
        self,
        asset_types: Sequence[str],
        asset_types_enabled: Sequence[str],
        aws_regions: Sequence[str],
        description: str,
    ) -> None:
        """Constructor for the UpdateAwsConnectionGroupV1Request class."""

        # Initialize members of the class
        self.asset_types: Sequence[str] = asset_types
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_regions: Sequence[str] = aws_regions
        self.description: str = description

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
        val = dictionary['asset_types']
        val_asset_types = val

        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['aws_regions']
        val_aws_regions = val

        val = dictionary['description']
        val_description = val

        # Return an object of this model
        return cls(
            val_asset_types,  # type: ignore
            val_asset_types_enabled,  # type: ignore
            val_aws_regions,  # type: ignore
            val_description,  # type: ignore
        )
