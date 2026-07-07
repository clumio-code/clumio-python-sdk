#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='S3AssetBackupTimeRange')


@dataclasses.dataclass
class S3AssetBackupTimeRange:
    """Implementation of the 'S3AssetBackupTimeRange' model.

    The parameters to generate the report of malicious objects detected within
    backup time range.

    Attributes:
        EndTimestamp:
            The end timestamp of searching time range in rfc-3339 format.
            clumio backup time until the given time inclusive. if not provided, defaults to
            the latest backup time.

        S3AssetId:
            Clumio-assigned id of protection group s3 asset, representing the
            bucket within the protection group to generate report from. use the
            [get /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.

        StartTimestamp:
            The start timestamp of searching time range in rfc-3339 format.
            clumio backup time since the given time inclusive. if not provided, defaults to
            the earliest backup time.

    """

    EndTimestamp: str | None = None
    S3AssetId: str | None = None
    StartTimestamp: str | None = None

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
        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('s3_asset_id', None)
        val_s3_asset_id = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        # Return an object of this model
        return cls(
            val_end_timestamp,
            val_s3_asset_id,
            val_start_timestamp,
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
