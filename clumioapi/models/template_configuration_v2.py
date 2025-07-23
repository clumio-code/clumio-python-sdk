#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_template_info as dynamodb_template_info_
from clumioapi.models import ebs_template_info as ebs_template_info_
from clumioapi.models import ec2_mssql_template_info as ec2_mssql_template_info_
from clumioapi.models import ec2_template_info as ec2_template_info_
from clumioapi.models import iceberg_template_info as iceberg_template_info_
from clumioapi.models import rds_template_info as rds_template_info_
from clumioapi.models import s3_template_info as s3_template_info_
from clumioapi.models import warm_tier_protect_template_info as warm_tier_protect_template_info_

T = TypeVar('T', bound='TemplateConfigurationV2')


class TemplateConfigurationV2:
    """Implementation of the 'TemplateConfigurationV2' model.

    The configuration of the given template

    Attributes:
        asset_types_enabled:
            The AWS asset types supported with the available version of the template.
        available_template_version:
            The latest available version for the template.
        dynamodb:
            The latest available information for the DynamoDB feature.
        ebs:

        ec2:

        ec2_mssql:
            The latest available information for the EC2 MSSQL feature.
        iceberg:
            IcebergTemplateInfo is the latest available information for the Iceberg feature.
        rds:

        s3:
            The latest available information for the S3 feature.
        warm_tier_protect:
            Configuration information about the Warm-Tier Protect feature of the template.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'asset_types_enabled': 'asset_types_enabled',
        'available_template_version': 'available_template_version',
        'dynamodb': 'dynamodb',
        'ebs': 'ebs',
        'ec2': 'ec2',
        'ec2_mssql': 'ec2_mssql',
        'iceberg': 'iceberg',
        'rds': 'rds',
        's3': 's3',
        'warm_tier_protect': 'warm_tier_protect',
    }

    def __init__(
        self,
        asset_types_enabled: Sequence[str] | None = None,
        available_template_version: str | None = None,
        dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = None,
        ebs: ebs_template_info_.EbsTemplateInfo | None = None,
        ec2: ec2_template_info_.Ec2TemplateInfo | None = None,
        ec2_mssql: ec2_mssql_template_info_.EC2MSSQLTemplateInfo | None = None,
        iceberg: iceberg_template_info_.IcebergTemplateInfo | None = None,
        rds: rds_template_info_.RdsTemplateInfo | None = None,
        s3: s3_template_info_.S3TemplateInfo | None = None,
        warm_tier_protect: (
            warm_tier_protect_template_info_.WarmTierProtectTemplateInfo | None
        ) = None,
    ) -> None:
        """Constructor for the TemplateConfigurationV2 class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] | None = asset_types_enabled
        self.available_template_version: str | None = available_template_version
        self.dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = dynamodb
        self.ebs: ebs_template_info_.EbsTemplateInfo | None = ebs
        self.ec2: ec2_template_info_.Ec2TemplateInfo | None = ec2
        self.ec2_mssql: ec2_mssql_template_info_.EC2MSSQLTemplateInfo | None = ec2_mssql
        self.iceberg: iceberg_template_info_.IcebergTemplateInfo | None = iceberg
        self.rds: rds_template_info_.RdsTemplateInfo | None = rds
        self.s3: s3_template_info_.S3TemplateInfo | None = s3
        self.warm_tier_protect: (
            warm_tier_protect_template_info_.WarmTierProtectTemplateInfo | None
        ) = warm_tier_protect

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

        val = dictionary.get('available_template_version', None)
        val_available_template_version = val

        val = dictionary.get('dynamodb', None)
        val_dynamodb = dynamodb_template_info_.DynamodbTemplateInfo.from_dictionary(val)

        val = dictionary.get('ebs', None)
        val_ebs = ebs_template_info_.EbsTemplateInfo.from_dictionary(val)

        val = dictionary.get('ec2', None)
        val_ec2 = ec2_template_info_.Ec2TemplateInfo.from_dictionary(val)

        val = dictionary.get('ec2_mssql', None)
        val_ec2_mssql = ec2_mssql_template_info_.EC2MSSQLTemplateInfo.from_dictionary(val)

        val = dictionary.get('iceberg', None)
        val_iceberg = iceberg_template_info_.IcebergTemplateInfo.from_dictionary(val)

        val = dictionary.get('rds', None)
        val_rds = rds_template_info_.RdsTemplateInfo.from_dictionary(val)

        val = dictionary.get('s3', None)
        val_s3 = s3_template_info_.S3TemplateInfo.from_dictionary(val)

        val = dictionary.get('warm_tier_protect', None)
        val_warm_tier_protect = (
            warm_tier_protect_template_info_.WarmTierProtectTemplateInfo.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_asset_types_enabled,
            val_available_template_version,
            val_dynamodb,
            val_ebs,
            val_ec2,
            val_ec2_mssql,
            val_iceberg,
            val_rds,
            val_s3,
            val_warm_tier_protect,
        )
