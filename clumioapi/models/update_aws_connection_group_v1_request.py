#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='UpdateAwsConnectionGroupV1Request')


@dataclasses.dataclass
class UpdateAwsConnectionGroupV1Request:
    """Implementation of the 'UpdateAwsConnectionGroupV1Request' model.

        Attributes:
            AssetTypes:
                The asset types to be connected via the connection-group.
    valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs", "icebergonglue"].

    note -
    1. ec2/ebs is required for ec2mssql.
    2. ebs as a value is deprecated in favor of ec2/ebs.

            AssetTypesEnabled:
                Deprecated, use "asset_types" instead.


    the asset types to be connected via the connection-group.
    valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs", "icebergonglue"].

    note -
    1. ec2/ebs is required for ec2mssql.
    2. ebs as a value is deprecated in favor of ec2/ebs.

            AwsRegions:
                The aws regions to be associated with the connection group.

            Description:
                Description for this connection group.

    """

    AssetTypes: Sequence[str] | None = None
    AssetTypesEnabled: Sequence[str] | None = None
    AwsRegions: Sequence[str] | None = None
    Description: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('asset_types', None)
        val_asset_types = val

        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('aws_regions', None)
        val_aws_regions = val

        val = dictionary.get('description', None)
        val_description = val

        # Return an object of this model
        return cls(
            val_asset_types,
            val_asset_types_enabled,
            val_aws_regions,
            val_description,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
