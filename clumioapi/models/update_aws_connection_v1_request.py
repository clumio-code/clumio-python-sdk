#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import resources as resources_
import requests

T = TypeVar('T', bound='UpdateAwsConnectionV1Request')


@dataclasses.dataclass
class UpdateAwsConnectionV1Request:
    """Implementation of the 'UpdateAwsConnectionV1Request' model.

        Attributes:
            AssetTypesEnabled:
                Asset types enabled with the given resource arns.
    this field is only applicable to manually configured connections.
    valid values are any of ["ec2/ebs", "rds", "dynamodb", "ec2mssql", "s3", "ebs", "icebergonglue"].

    note -
    1. ec2/ebs is required for ec2mssql.
    2. ebs as a value is deprecated in favor of ec2/ebs.

            Description:
                An optional, user-provided description for this connection.

            Resources:
                Partial updates are not supported, therefore you must provide arns for all configured resources,
    including those for resources that are not being updated.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    Description: str | None = None
    Resources: resources_.Resources | None = None

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
        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('resources', None)
        val_resources = resources_.Resources.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_description,
            val_resources,
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
