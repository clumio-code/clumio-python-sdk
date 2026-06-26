#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
import requests

T = TypeVar('T', bound='GlueRetentionConfiguration')


@dataclasses.dataclass
class GlueRetentionConfiguration:
    """Implementation of the 'GlueRetentionConfiguration' model.

    Attributes:
        CleanExpiredFiles

        NumberOfSnapshotsToRetain

        RunRateInHours

        SnapshotRetentionPeriodInDays

        Status

    """

    CleanExpiredFiles: bool | None = None
    NumberOfSnapshotsToRetain: int | None = None
    RunRateInHours: int | None = None
    SnapshotRetentionPeriodInDays: int | None = None
    Status: str | None = None

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
        val = dictionary.get('clean_expired_files', None)
        val_clean_expired_files = val

        val = dictionary.get('number_of_snapshots_to_retain', None)
        val_number_of_snapshots_to_retain = val

        val = dictionary.get('run_rate_in_hours', None)
        val_run_rate_in_hours = val

        val = dictionary.get('snapshot_retention_period_in_days', None)
        val_snapshot_retention_period_in_days = val

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_clean_expired_files,
            val_number_of_snapshots_to_retain,
            val_run_rate_in_hours,
            val_snapshot_retention_period_in_days,
            val_status,
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
