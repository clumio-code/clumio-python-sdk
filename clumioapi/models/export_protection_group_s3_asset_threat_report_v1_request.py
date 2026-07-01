#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, TypeVar

from clumioapi import api_helper
from clumioapi.models import s3_asset_threat_report_source as s3_asset_threat_report_source_
from clumioapi.models import s3_asset_threat_report_target as s3_asset_threat_report_target_
import requests

T = TypeVar('T', bound='ExportProtectionGroupS3AssetThreatReportV1Request')


@dataclasses.dataclass
class ExportProtectionGroupS3AssetThreatReportV1Request:
    """Implementation of the 'ExportProtectionGroupS3AssetThreatReportV1Request' model.

    Attributes:
        Source:
            The parameters to specify how to generate the threat report for protection group
            s3 asset.
            must set exactly one of the options.

        Target:
            The parameters for which s3 bucket to export the threat report to.

    """

    Source: s3_asset_threat_report_source_.S3AssetThreatReportSource | None = None
    Target: s3_asset_threat_report_target_.S3AssetThreatReportTarget | None = None

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
        val = dictionary.get('source', None)
        val_source = s3_asset_threat_report_source_.S3AssetThreatReportSource.from_dictionary(val)

        val = dictionary.get('target', None)
        val_target = s3_asset_threat_report_target_.S3AssetThreatReportTarget.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_source,
            val_target,
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
