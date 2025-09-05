#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_asset_info as dynamodb_asset_info_
from clumioapi.models import ebs_asset_info as ebs_asset_info_
from clumioapi.models import ec2_asset_info as ec2_asset_info_
from clumioapi.models import ec2_mssql_protect_config as ec2_mssql_protect_config_
from clumioapi.models import iceberg_on_glue_asset_info as iceberg_on_glue_asset_info_
from clumioapi.models import rds_asset_info as rds_asset_info_
from clumioapi.models import s3_asset_info as s3_asset_info_
from clumioapi.models import warm_tier_protect_config as warm_tier_protect_config_

T = TypeVar('T', bound='ConsolidatedConfig')


class ConsolidatedConfig:
    """Implementation of the 'ConsolidatedConfig' model.

    The consolidated configuration of the Clumio Cloud Protect and Clumio Cloud
    Discover products for this connection.If this connection is deprecated to use
    unconsolidated configuration, then this field has avalue of `null`.

    Attributes:
        asset_types_enabled:
            The asset types supported on the current version of the feature
        dynamodb:
            DynamodbAssetInfo
            The installed information for the DynamoDB feature.
        ebs:
            EbsAssetInfo
            The installed information for the EBS feature.
        ec2:
            Ec2AssetInfo
            The installed information for the EC2 feature.
        ec2_mssql:
            EC2MSSQLProtectConfig
            The installed information for the EC2_MSSQL feature.
        iceberg_on_glue:
            IcebergOnGlueAssetInfo
            The installed information for the Iceberg on AWS Glue feature.
        installed_template_version:
            The current version of the feature.
        rds:
            RdsAssetInfo
            The installed information for the RDS feature.
        s3:
            S3AssetInfo
            The installed information for the S3 feature.
        warm_tier_protect:
            The configuration of the Clumio Cloud Warm-Tier Protect product for this
            connection.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'dynamodb': 'dynamodb',
        'ebs': 'ebs',
        'ec2': 'ec2',
        'ec2_mssql': 'ec2_mssql',
        'iceberg_on_glue': 'iceberg_on_glue',
        'installed_template_version': 'installed_template_version',
        'rds': 'rds',
        's3': 's3',
        'warm_tier_protect': 'warm_tier_protect',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] | None = None,
        dynamodb: dynamodb_asset_info_.DynamodbAssetInfo | None = None,
        ebs: ebs_asset_info_.EbsAssetInfo | None = None,
        ec2: ec2_asset_info_.Ec2AssetInfo | None = None,
        ec2_mssql: ec2_mssql_protect_config_.EC2MSSQLProtectConfig | None = None,
        iceberg_on_glue: iceberg_on_glue_asset_info_.IcebergOnGlueAssetInfo | None = None,
        installed_template_version: str | None = None,
        rds: rds_asset_info_.RdsAssetInfo | None = None,
        s3: s3_asset_info_.S3AssetInfo | None = None,
        warm_tier_protect: warm_tier_protect_config_.WarmTierProtectConfig | None = None,
    ) -> None:
        """Constructor for the ConsolidatedConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] | None = asset_types_enabled
        self.dynamodb: dynamodb_asset_info_.DynamodbAssetInfo | None = dynamodb
        self.ebs: ebs_asset_info_.EbsAssetInfo | None = ebs
        self.ec2: ec2_asset_info_.Ec2AssetInfo | None = ec2
        self.ec2_mssql: ec2_mssql_protect_config_.EC2MSSQLProtectConfig | None = ec2_mssql
        self.iceberg_on_glue: iceberg_on_glue_asset_info_.IcebergOnGlueAssetInfo | None = (
            iceberg_on_glue
        )
        self.installed_template_version: str | None = installed_template_version
        self.rds: rds_asset_info_.RdsAssetInfo | None = rds
        self.s3: s3_asset_info_.S3AssetInfo | None = s3
        self.warm_tier_protect: warm_tier_protect_config_.WarmTierProtectConfig | None = (
            warm_tier_protect
        )

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
            val_installed_template_version,
            val_rds,
            val_s3,
            val_warm_tier_protect,
        )
