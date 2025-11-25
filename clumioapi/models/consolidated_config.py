#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamodb_asset_info as dynamodb_asset_info_
from clumioapi.models import ebs_asset_info as ebs_asset_info_
from clumioapi.models import ec2_asset_info as ec2_asset_info_
from clumioapi.models import ec2_mssql_protect_config as ec2_mssql_protect_config_
from clumioapi.models import iceberg_on_glue_asset_info as iceberg_on_glue_asset_info_
from clumioapi.models import iceberg_on_s3_tables_asset_info as iceberg_on_s3_tables_asset_info_
from clumioapi.models import rds_asset_info as rds_asset_info_
from clumioapi.models import s3_asset_info as s3_asset_info_
from clumioapi.models import warm_tier_protect_config as warm_tier_protect_config_
import requests

T = TypeVar('T', bound='ConsolidatedConfig')


@dataclasses.dataclass
class ConsolidatedConfig:
    """Implementation of the 'ConsolidatedConfig' model.

    The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
    Discover products for this connection.If this connection is deprecated to use
    unconsolidated configuration, then this field has avalue of `null`.

    Attributes:
        AssetTypesEnabled:
            The asset types supported on the current version of the feature.

        Dynamodb:
            Dynamodbassetinfo
            the installed information for the dynamodb feature.

        Ebs:
            Ebsassetinfo
            the installed information for the ebs feature.

        Ec2:
            Ec2assetinfo
            the installed information for the ec2 feature.

        Ec2Mssql:
            Ec2mssqlprotectconfig
            the installed information for the ec2_mssql feature.

        IcebergOnGlue:
            Icebergonglueassetinfo
            the installed information for the iceberg on aws glue feature.

        IcebergOnS3Tables:
            Icebergons3tablesassetinfo
            the installed information for the iceberg on s3 tables feature.

        InstalledTemplateVersion:
            The current version of the feature.

        Rds:
            Rdsassetinfo
            the installed information for the rds feature.

        S3:
            S3assetinfo
            the installed information for the s3 feature.

        WarmTierProtect:
            The configuration of the clumio cloud warm-tier protect product for this
            connection.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    Dynamodb: dynamodb_asset_info_.DynamodbAssetInfo | None = None
    Ebs: ebs_asset_info_.EbsAssetInfo | None = None
    Ec2: ec2_asset_info_.Ec2AssetInfo | None = None
    Ec2Mssql: ec2_mssql_protect_config_.EC2MSSQLProtectConfig | None = None
    IcebergOnGlue: iceberg_on_glue_asset_info_.IcebergOnGlueAssetInfo | None = None
    IcebergOnS3Tables: iceberg_on_s3_tables_asset_info_.IcebergOnS3TablesAssetInfo | None = None
    InstalledTemplateVersion: str | None = None
    Rds: rds_asset_info_.RdsAssetInfo | None = None
    S3: s3_asset_info_.S3AssetInfo | None = None
    WarmTierProtect: warm_tier_protect_config_.WarmTierProtectConfig | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

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
        val = dictionary.get('asset_types_enabled', None)
        val_asset_types_enabled = val

        val = dictionary.get('dynamodb', None)
        val_dynamodb = dynamodb_asset_info_.DynamodbAssetInfo.from_dictionary(val)

        val = dictionary.get('ebs', None)
        val_ebs = ebs_asset_info_.EbsAssetInfo.from_dictionary(val)

        val = dictionary.get('ec2', None)
        val_ec2 = ec2_asset_info_.Ec2AssetInfo.from_dictionary(val)

        val = dictionary.get('ec2_mssql', None)
        val_ec2_mssql = ec2_mssql_protect_config_.EC2MSSQLProtectConfig.from_dictionary(val)

        val = dictionary.get('iceberg_on_glue', None)
        val_iceberg_on_glue = iceberg_on_glue_asset_info_.IcebergOnGlueAssetInfo.from_dictionary(
            val
        )

        val = dictionary.get('iceberg_on_s3_tables', None)
        val_iceberg_on_s3_tables = (
            iceberg_on_s3_tables_asset_info_.IcebergOnS3TablesAssetInfo.from_dictionary(val)
        )

        val = dictionary.get('installed_template_version', None)
        val_installed_template_version = val

        val = dictionary.get('rds', None)
        val_rds = rds_asset_info_.RdsAssetInfo.from_dictionary(val)

        val = dictionary.get('s3', None)
        val_s3 = s3_asset_info_.S3AssetInfo.from_dictionary(val)

        val = dictionary.get('warm_tier_protect', None)
        val_warm_tier_protect = warm_tier_protect_config_.WarmTierProtectConfig.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_dynamodb,
            val_ebs,
            val_ec2,
            val_ec2_mssql,
            val_iceberg_on_glue,
            val_iceberg_on_s3_tables,
            val_installed_template_version,
            val_rds,
            val_s3,
            val_warm_tier_protect,
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
