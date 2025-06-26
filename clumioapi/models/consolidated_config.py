#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_asset_info
from clumioapi.models import ebs_asset_info
from clumioapi.models import ec2_asset_info
from clumioapi.models import ec2_mssql_protect_config
from clumioapi.models import iceberg_asset_info
from clumioapi.models import rds_asset_info
from clumioapi.models import s3_asset_info
from clumioapi.models import warm_tier_protect_config

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
        iceberg:
            IcebergAssetInfo
            The installed information for the Iceberg feature.
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
    _names = {
        'asset_types_enabled': 'asset_types_enabled',
        'dynamodb': 'dynamodb',
        'ebs': 'ebs',
        'ec2': 'ec2',
        'ec2_mssql': 'ec2_mssql',
        'iceberg': 'iceberg',
        'installed_template_version': 'installed_template_version',
        'rds': 'rds',
        's3': 's3',
        'warm_tier_protect': 'warm_tier_protect',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] = None,
        dynamodb: dynamodb_asset_info.DynamodbAssetInfo = None,
        ebs: ebs_asset_info.EbsAssetInfo = None,
        ec2: ec2_asset_info.Ec2AssetInfo = None,
        ec2_mssql: ec2_mssql_protect_config.EC2MSSQLProtectConfig = None,
        iceberg: iceberg_asset_info.IcebergAssetInfo = None,
        installed_template_version: str = None,
        rds: rds_asset_info.RdsAssetInfo = None,
        s3: s3_asset_info.S3AssetInfo = None,
        warm_tier_protect: warm_tier_protect_config.WarmTierProtectConfig = None,
    ) -> None:
        """Constructor for the ConsolidatedConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.dynamodb: dynamodb_asset_info.DynamodbAssetInfo = dynamodb
        self.ebs: ebs_asset_info.EbsAssetInfo = ebs
        self.ec2: ec2_asset_info.Ec2AssetInfo = ec2
        self.ec2_mssql: ec2_mssql_protect_config.EC2MSSQLProtectConfig = ec2_mssql
        self.iceberg: iceberg_asset_info.IcebergAssetInfo = iceberg
        self.installed_template_version: str = installed_template_version
        self.rds: rds_asset_info.RdsAssetInfo = rds
        self.s3: s3_asset_info.S3AssetInfo = s3
        self.warm_tier_protect: warm_tier_protect_config.WarmTierProtectConfig = warm_tier_protect

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        asset_types_enabled = dictionary.get('asset_types_enabled')
        key = 'dynamodb'
        dynamodb = (
            dynamodb_asset_info.DynamodbAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ebs'
        ebs = (
            ebs_asset_info.EbsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ec2'
        ec2 = (
            ec2_asset_info.Ec2AssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ec2_mssql'
        ec2_mssql = (
            ec2_mssql_protect_config.EC2MSSQLProtectConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'iceberg'
        iceberg = (
            iceberg_asset_info.IcebergAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        installed_template_version = dictionary.get('installed_template_version')
        key = 'rds'
        rds = (
            rds_asset_info.RdsAssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 's3'
        s3 = (
            s3_asset_info.S3AssetInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'warm_tier_protect'
        warm_tier_protect = (
            warm_tier_protect_config.WarmTierProtectConfig.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            asset_types_enabled,
            dynamodb,
            ebs,
            ec2,
            ec2_mssql,
            iceberg,
            installed_template_version,
            rds,
            s3,
            warm_tier_protect,
        )
