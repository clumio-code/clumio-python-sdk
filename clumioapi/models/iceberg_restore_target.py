#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import optimizer as optimizer_
import requests

T = TypeVar('T', bound='IcebergRestoreTarget')


@dataclasses.dataclass
class IcebergRestoreTarget:
    """Implementation of the 'IcebergRestoreTarget' model.

    IcebergRestoreTargetThe target destination for the restored Iceberg Table.

    Attributes:
        AssetId:
            The asset id of the target iceberg table to restore into.
            if specified, the restore targets an existing table. if omitted, a new table is
            created
            using the catalog-specific fields below.

        Catalog:
            The catalog of the iceberg table — an empty string for glue tables,
            and the table bucket arn for s3 tables.
            required when creating a new s3 tables target table.

        CatalogType:
            The type of catalog to which the restored iceberg table belongs.

        EnvironmentId:
            The clumio-assigned id of the aws environment to be used as the restore
            destination. use the
            [get /datasources/aws/environments](#operation/list-aws-environments) endpoint
            to fetch valid
            values.

        Namespace:
            The namespace of the iceberg table - database name for glue tables,
            and namespace for s3 tables.
            required when creating a new target table.

        Optimizer

        TableLocation:
            The location of the iceberg table. this is generally the s3 prefix of
            the table bucket.
            required when creating a new glue target table.

        TableName:
            The name of the iceberg table to restore.
            required when creating a new target table.

    """

    AssetId: str | None = None
    Catalog: str | None = None
    CatalogType: str | None = None
    EnvironmentId: str | None = None
    Namespace: str | None = None
    Optimizer: optimizer_.Optimizer | None = None
    TableLocation: str | None = None
    TableName: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return api_helper.to_dictionary(self)

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
        val = dictionary.get('asset_id', None)
        val_asset_id = val

        val = dictionary.get('catalog', None)
        val_catalog = val

        val = dictionary.get('catalog_type', None)
        val_catalog_type = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('namespace', None)
        val_namespace = val

        val = dictionary.get('optimizer', None)
        val_optimizer = optimizer_.Optimizer.from_dictionary(val)

        val = dictionary.get('table_location', None)
        val_table_location = val

        val = dictionary.get('table_name', None)
        val_table_name = val

        # Return an object of this model
        return cls(
            val_asset_id,
            val_catalog,
            val_catalog_type,
            val_environment_id,
            val_namespace,
            val_optimizer,
            val_table_location,
            val_table_name,
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
