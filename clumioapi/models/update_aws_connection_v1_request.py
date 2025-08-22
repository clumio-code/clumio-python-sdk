#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import resources as resources_

T = TypeVar('T', bound='UpdateAwsConnectionV1Request')


class UpdateAwsConnectionV1Request:
    """Implementation of the 'UpdateAwsConnectionV1Request' model.

    Attributes:
        asset_types_enabled:
            Asset types enabled with the given resource ARNs.
            This field is only applicable to manually configured connections.
            Valid values are any of ["EC2/EBS", "RDS", "DynamoDB", "EC2MSSQL", "S3", "EBS",
            "IcebergOnGlue"].

            NOTE -
            1. EC2/EBS is required for EC2MSSQL.
            2. EBS as a value is deprecated in favor of EC2/EBS.
        description:
            An optional, user-provided description for this connection.
        resources:
            Partial updates are not supported, therefore you must provide ARNs for all
            configured resources,
            including those for resources that are not being updated.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'description': 'description',
        'resources': 'resources',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] | None = None,
        description: str | None = None,
        resources: resources_.Resources | None = None,
    ) -> None:
        """Constructor for the UpdateAwsConnectionV1Request class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] | None = asset_types_enabled
        self.description: str | None = description
        self.resources: resources_.Resources | None = resources

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
