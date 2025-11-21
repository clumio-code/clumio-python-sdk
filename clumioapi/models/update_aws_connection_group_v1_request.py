#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='UpdateAwsConnectionGroupV1Request')

TemplatePermissionSetValues = [
    'all',
    'inventory_backup',
]


@dataclasses.dataclass
class UpdateAwsConnectionGroupV1Request:
    """Implementation of the 'UpdateAwsConnectionGroupV1Request' model.

    Attributes:
        AssetTypes:
            The asset types to be connected via the connection-group.
            valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs",
            "icebergonglue", "icebergons3tables", "fsx"].

            note -
            1. ec2/ebs is required for ec2mssql.
            2. ebs as a value is deprecated in favor of ec2/ebs.

        AssetTypesEnabled:
            Deprecated, use "asset_types" instead.


            the asset types to be connected via the connection-group.
            valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs",
            "icebergonglue", "icebergons3tables", "fsx"].

            note -
            1. ec2/ebs is required for ec2mssql.
            2. ebs as a value is deprecated in favor of ec2/ebs.

        AwsRegions:
            The aws regions to be associated with the connection group.

        Description:
            Description for this connection group.

        TemplatePermissionSet

    """

    AssetTypes: Sequence[str] | None = None
    AssetTypesEnabled: Sequence[str] | None = None
    AwsRegions: Sequence[str] | None = None
    Description: str | None = None

    TemplatePermissionSet: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('asset_types', None)
        val_asset_types = val

        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('aws_regions', None)
        val_aws_regions = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('template_permission_set', None)
        val_template_permission_set = val

        # Return an object of this model
        return cls(
            val_asset_types,
            val_asset_types_enabled,
            val_aws_regions,
            val_description,
            val_template_permission_set,
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
