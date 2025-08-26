#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CreateAwsConnectionGroupV1Request')


@dataclasses.dataclass
class CreateAwsConnectionGroupV1Request:
    """Implementation of the 'CreateAwsConnectionGroupV1Request' model.

        The body of the request.

        Attributes:
            AccountNativeId:
                The aws-assigned id of the account to be associated with the connection group.

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

            MasterAwsAccountId:
                The aws account that manages the connection-group's stack.
    if the provided master_aws_account_id different than the account_native_id then
    use service managed permissions while deploying stack.

            MasterRegion:
                The aws region that manages the connection-group's stack.

            OrganizationalUnitId:
                The clumio-assigned id of the organizational unit associated with the
    aws environment. if this parameter is not provided, then the value
    defaults to the first organizational unit assigned to the requesting
    user. for more information about organizational units, refer to the
    organizational-units documentation.

    """

    AccountNativeId: str | None = None
    AssetTypes: Sequence[str] | None = None
    AssetTypesEnabled: Sequence[str] | None = None
    AwsRegions: Sequence[str] | None = None
    Description: str | None = None
    MasterAwsAccountId: str | None = None
    MasterRegion: str | None = None
    OrganizationalUnitId: str | None = None

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
        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('asset_types', None)
        val_asset_types = val

        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('aws_regions', None)
        val_aws_regions = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('master_aws_account_id', None)
        val_master_aws_account_id = val

        val = dictionary.get('master_region', None)
        val_master_region = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        # Return an object of this model
        return cls(
            val_account_native_id,
            val_asset_types,
            val_asset_types_enabled,
            val_aws_regions,
            val_description,
            val_master_aws_account_id,
            val_master_region,
            val_organizational_unit_id,
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
