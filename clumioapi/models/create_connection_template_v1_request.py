#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateConnectionTemplateV1Request')


class CreateConnectionTemplateV1Request:
    """Implementation of the 'CreateConnectionTemplateV1Request' model.

    Attributes:
        asset_types_enabled:
            The asset types for which the template is to be generated.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "Iceberg"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        aws_account_id:
            Account ID for the AWS environment to be connected
            Mandatory to pass a 12 digit string if show_manual_resources is set to true
        aws_region:
            AWS Region of the AWS environment to be connected
            Mandatory to pass a non-empty string if show_manual_resources is set to true
        show_manual_resources:
            Returns the resources to be created manually if set to true
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'aws_account_id': 'aws_account_id',
        'aws_region': 'aws_region',
        'show_manual_resources': 'show_manual_resources',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        aws_account_id: str = None,
        aws_region: str = None,
        show_manual_resources: bool = None,
    ) -> None:
        """Constructor for the CreateConnectionTemplateV1Request class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_account_id: str = aws_account_id
        self.aws_region: str = aws_region
        self.show_manual_resources: bool = show_manual_resources

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
        aws_account_id = dictionary.get('aws_account_id')
        aws_region = dictionary.get('aws_region')
        show_manual_resources = dictionary.get('show_manual_resources')
        # Return an object of this model
        return cls(asset_types_enabled, aws_account_id, aws_region, show_manual_resources)
