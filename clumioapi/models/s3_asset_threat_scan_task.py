#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='S3AssetThreatScanTask')


@dataclasses.dataclass
class S3AssetThreatScanTask:
    """Implementation of the 'S3AssetThreatScanTask' model.

    The parameters to generate the report of malicious objects detected in a
    specific threat scan task.

    Attributes:
        S3AssetId:
            Clumio-assigned id of protection group s3 asset, representing the
            bucket within the protection group to generate report from. use the
            [get /datasources/protection-groups/s3-assets](#operation/list-protection-
            group-s3-assets)
            endpoint to fetch valid values.

        TaskId:
            The task id assigned to the backup or regular threat scan where malicious
            objects were detected.

    """

    S3AssetId: str | None = None
    TaskId: int | None = None

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
        val = dictionary.get('s3_asset_id', None)
        val_s3_asset_id = val

        val = dictionary.get('task_id', None)
        val_task_id = val

        # Return an object of this model
        return cls(
            val_s3_asset_id,
            val_task_id,
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
