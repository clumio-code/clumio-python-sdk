#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_asset_info as dynamodb_asset_info_
from clumioapi.models import ebs_asset_info as ebs_asset_info_
from clumioapi.models import ec2_asset_info as ec2_asset_info_
from clumioapi.models import ec2_mssql_protect_config as ec2_mssql_protect_config_
from clumioapi.models import iceberg_asset_info as iceberg_asset_info_
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
    _names: dict[str, str] = {
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
        asset_types_enabled: Sequence[str],
        dynamodb: dynamodb_asset_info_.DynamodbAssetInfo,
        ebs: ebs_asset_info_.EbsAssetInfo,
        ec2: ec2_asset_info_.Ec2AssetInfo,
        ec2_mssql: ec2_mssql_protect_config_.EC2MSSQLProtectConfig,
        iceberg: iceberg_asset_info_.IcebergAssetInfo,
        installed_template_version: str,
        rds: rds_asset_info_.RdsAssetInfo,
        s3: s3_asset_info_.S3AssetInfo,
        warm_tier_protect: warm_tier_protect_config_.WarmTierProtectConfig,
    ) -> None:
        """Constructor for the ConsolidatedConfig class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.dynamodb: dynamodb_asset_info_.DynamodbAssetInfo = dynamodb
        self.ebs: ebs_asset_info_.EbsAssetInfo = ebs
        self.ec2: ec2_asset_info_.Ec2AssetInfo = ec2
        self.ec2_mssql: ec2_mssql_protect_config_.EC2MSSQLProtectConfig = ec2_mssql
        self.iceberg: iceberg_asset_info_.IcebergAssetInfo = iceberg
        self.installed_template_version: str = installed_template_version
        self.rds: rds_asset_info_.RdsAssetInfo = rds
        self.s3: s3_asset_info_.S3AssetInfo = s3
        self.warm_tier_protect: warm_tier_protect_config_.WarmTierProtectConfig = warm_tier_protect

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

        # Extract variables from the dictionary
        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['dynamodb']
        val_dynamodb = dynamodb_asset_info_.DynamodbAssetInfo.from_dictionary(val)

        val = dictionary['ebs']
        val_ebs = ebs_asset_info_.EbsAssetInfo.from_dictionary(val)

        val = dictionary['ec2']
        val_ec2 = ec2_asset_info_.Ec2AssetInfo.from_dictionary(val)

        val = dictionary['ec2_mssql']
        val_ec2_mssql = ec2_mssql_protect_config_.EC2MSSQLProtectConfig.from_dictionary(val)

        val = dictionary['iceberg']
        val_iceberg = iceberg_asset_info_.IcebergAssetInfo.from_dictionary(val)

        val = dictionary['installed_template_version']
        val_installed_template_version = val

        val = dictionary['rds']
        val_rds = rds_asset_info_.RdsAssetInfo.from_dictionary(val)

        val = dictionary['s3']
        val_s3 = s3_asset_info_.S3AssetInfo.from_dictionary(val)

        val = dictionary['warm_tier_protect']
        val_warm_tier_protect = warm_tier_protect_config_.WarmTierProtectConfig.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_asset_types_enabled,  # type: ignore
            val_dynamodb,  # type: ignore
            val_ebs,  # type: ignore
            val_ec2,  # type: ignore
            val_ec2_mssql,  # type: ignore
            val_iceberg,  # type: ignore
            val_installed_template_version,  # type: ignore
            val_rds,  # type: ignore
            val_s3,  # type: ignore
            val_warm_tier_protect,  # type: ignore
        )
