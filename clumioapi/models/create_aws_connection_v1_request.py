#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CreateAwsConnectionV1Request')


@dataclasses.dataclass
class CreateAwsConnectionV1Request:
    """Implementation of the 'CreateAwsConnectionV1Request' model.

        Attributes:
            AccountNativeId:
                The aws-assigned id of the account associated with the connection.

            AwsRegion:
                The aws region associated with the connection. for example, `us-east-1`.

            Description:
                The user-provided description for this connection.

            OrganizationalUnitId:
                The clumio-assigned id of the organizational unit associated with the
    aws environment. if this parameter is not provided, then the value
    defaults to the first organizational unit assigned to the requesting
    user. for more information about organizational units, refer to the
    organizational-units documentation.

            ProtectAssetTypesEnabled:
                The asset types enabled for protect.
    valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs", "icebergonglue"].

    note -
    1. ec2/ebs is required for ec2mssql.
    2. ebs as a value is deprecated in favor of ec2/ebs.

            ServicesEnabled:
                The services to be enabled for this configuration. valid values are
    ["discover"], ["discover", "protect"]. this is only set when the
    registration is created, the enabled services are obtained directly from
    the installed template after that. (deprecated as all connections will have
    both discover and protect enabled).

    """

    AccountNativeId: str | None = None
    AwsRegion: str | None = None
    Description: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectAssetTypesEnabled: Sequence[str] | None = None
    ServicesEnabled: Sequence[str] | None = None

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
