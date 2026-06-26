#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, ClassVar, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi import api_helper
from clumioapi.models import \
    gcpgcs_asset_continuous_backup_stats as gcpgcs_asset_continuous_backup_stats_
from clumioapi.models import \
    gcpgcs_asset_continuous_backup_stats_links as gcpgcs_asset_continuous_backup_stats_links_
import requests

T = TypeVar('T', bound='ReadGCPGCSAssetContinuousBackupStatsResponse')


@dataclasses.dataclass
class ReadGCPGCSAssetContinuousBackupStatsResponse:
    """Implementation of the 'ReadGCPGCSAssetContinuousBackupStatsResponse' model.

    Attributes:
        Links:
            Gcsassetcontinuousbackupstatslinks
            urls to pages related to the resource.

        Bins:
            The list of continuous backup statistics grouped by the given time interval.

        TotalStats:
            Gcsassetcontinuousbackupstats is one bin of cdp execution and dmover/drain
            aggregates for a gcs asset. used for both the window-wide total and per-bin
            entries in the continuous-backup-stats response.

    """

    # Maps Python attribute names to API keys that cannot be recovered from the
    # attribute name, so serialization round-trips correctly. E.g. attribute
    # ``Eq`` <-> key ``$eq``, ``Links`` <-> ``_links``, ``Type`` <-> ``@type``.
    _names: ClassVar[Dict[str, str]] = {
        'Links': '_links',
    }

    Links: (
        gcpgcs_asset_continuous_backup_stats_links_.GCPGCSAssetContinuousBackupStatsLinks | None
    ) = None
    Bins: (
        Sequence[gcpgcs_asset_continuous_backup_stats_.GCPGCSAssetContinuousBackupStats] | None
    ) = None
    TotalStats: gcpgcs_asset_continuous_backup_stats_.GCPGCSAssetContinuousBackupStats | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_links', None)
        val_links = gcpgcs_asset_continuous_backup_stats_links_.GCPGCSAssetContinuousBackupStatsLinks.from_dictionary(
            val
        )

        val = dictionary.get('bins', None)

        val_bins = []
        if val:
            for value in val:
                val_bins.append(
                    gcpgcs_asset_continuous_backup_stats_.GCPGCSAssetContinuousBackupStats.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('total_stats', None)
        val_total_stats = (
            gcpgcs_asset_continuous_backup_stats_.GCPGCSAssetContinuousBackupStats.from_dictionary(
                val
            )
        )

        # Return an object of this model
        return cls(
            val_links,
            val_bins,
            val_total_stats,
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
        model_instance.raw_response = response
        return model_instance
