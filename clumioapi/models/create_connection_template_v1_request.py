#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'aws_account_id': 'aws_account_id',
        'aws_region': 'aws_region',
        'show_manual_resources': 'show_manual_resources',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str],
        aws_account_id: str,
        aws_region: str,
        show_manual_resources: bool,
    ) -> None:
        """Constructor for the CreateConnectionTemplateV1Request class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.aws_account_id: str = aws_account_id
        self.aws_region: str = aws_region
        self.show_manual_resources: bool = show_manual_resources

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
        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['aws_account_id']
        val_aws_account_id = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['show_manual_resources']
        val_show_manual_resources = val

        # Return an object of this model
        return cls(
            val_asset_types_enabled,  # type: ignore
            val_aws_account_id,  # type: ignore
            val_aws_region,  # type: ignore
            val_show_manual_resources,  # type: ignore
        )
