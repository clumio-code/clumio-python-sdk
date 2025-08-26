#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ebs_asset_info as ebs_asset_info_
from clumioapi.models import rds_asset_info as rds_asset_info_
import requests

T = TypeVar('T', bound='ProtectConfig')


@dataclasses.dataclass
class ProtectConfig:
    """Implementation of the 'ProtectConfig' model.

        The configuration of the Clumio Cloud Protect product for this connection.If
        this connection is not configured for Clumio Cloud Protect, then this field has
        avalue of `null`.

        Attributes:
            AssetTypesEnabled:
                The asset types supported on the current version of the feature.

            Ebs:
                Ebsassetinfo
    the installed information for the ebs feature.

            InstalledTemplateVersion:
                The current version of the feature.

            Rds:
                Rdsassetinfo
    the installed information for the rds feature.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    Ebs: ebs_asset_info_.EbsAssetInfo | None = None
    InstalledTemplateVersion: str | None = None
    Rds: rds_asset_info_.RdsAssetInfo | None = None

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

        val = dictionary.get('ebs', None)
        val_ebs = ebs_asset_info_.EbsAssetInfo.from_dictionary(val)

        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        val = dictionary.get('rds', None)
        val_rds = rds_asset_info_.RdsAssetInfo.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_ebs,
            val_installed_template_version,
            val_rds,
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
