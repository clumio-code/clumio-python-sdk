#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateAwsConnectionGroupV1Request')


class UpdateAwsConnectionGroupV1Request:
    """Implementation of the 'UpdateAwsConnectionGroupV1Request' model.

    Attributes:
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
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types': 'asset_types',
        'asset_types_enabled': 'asset_types_enabled',
        'aws_regions': 'aws_regions',
        'description': 'description',
    }

    def __init__(
        self,
        asset_types: Sequence[str] = None,
        asset_types_enabled: Sequence[str] = None,
        aws_regions: Sequence[str] = None,
        description: str = None,
    ) -> None:
        """Constructor for the UpdateAwsConnectionGroupV1Request class."""

        # Initialize members of the class
        self.asset_types: Sequence[str] = asset_types
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_regions: Sequence[str] = aws_regions
        self.description: str = description

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
        asset_types = dictionary.get('asset_types')
        asset_types_enabled = dictionary.get('asset_types_enabled')
        aws_regions = dictionary.get('aws_regions')
        description = dictionary.get('description')
        # Return an object of this model
        return cls(asset_types, asset_types_enabled, aws_regions, description)
