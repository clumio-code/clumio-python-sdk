#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import s3_tables_iceberg_compaction as s3_tables_iceberg_compaction_
from clumioapi.models import \
    s3_tables_iceberg_snapshot_management as s3_tables_iceberg_snapshot_management_
import requests

T = TypeVar('T', bound='S3TablesOptimizer')


@dataclasses.dataclass
class S3TablesOptimizer:
    """Implementation of the 'S3TablesOptimizer' model.

    Attributes:
        IcebergCompaction

        IcebergSnapshotManagement

    """

    IcebergCompaction: s3_tables_iceberg_compaction_.S3TablesIcebergCompaction | None = None
    IcebergSnapshotManagement: (
        s3_tables_iceberg_snapshot_management_.S3TablesIcebergSnapshotManagement | None
    ) = None

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
        val = dictionary.get('iceberg_compaction', None)
        val_iceberg_compaction = (
            s3_tables_iceberg_compaction_.S3TablesIcebergCompaction.from_dictionary(val)
        )

        val = dictionary.get('iceberg_snapshot_management', None)
        val_iceberg_snapshot_management = s3_tables_iceberg_snapshot_management_.S3TablesIcebergSnapshotManagement.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_iceberg_compaction,
            val_iceberg_snapshot_management,
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
