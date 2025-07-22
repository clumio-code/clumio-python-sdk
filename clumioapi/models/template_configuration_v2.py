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
        asset_types_enabled: Sequence[str],
        available_template_version: str,
        dynamodb: dynamodb_template_info_.DynamodbTemplateInfo,
        ebs: ebs_template_info_.EbsTemplateInfo,
        ec2: ec2_template_info_.Ec2TemplateInfo,
        ec2_mssql: ec2_mssql_template_info_.EC2MSSQLTemplateInfo,
        iceberg: iceberg_template_info_.IcebergTemplateInfo,
        rds: rds_template_info_.RdsTemplateInfo,
        s3: s3_template_info_.S3TemplateInfo,
        warm_tier_protect: warm_tier_protect_template_info_.WarmTierProtectTemplateInfo,
    ) -> None:
        """Constructor for the TemplateConfigurationV2 class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_version: str = available_template_version
        self.dynamodb: dynamodb_template_info_.DynamodbTemplateInfo = dynamodb
        self.ebs: ebs_template_info_.EbsTemplateInfo = ebs
        self.ec2: ec2_template_info_.Ec2TemplateInfo = ec2
        self.ec2_mssql: ec2_mssql_template_info_.EC2MSSQLTemplateInfo = ec2_mssql
        self.iceberg: iceberg_template_info_.IcebergTemplateInfo = iceberg
        self.rds: rds_template_info_.RdsTemplateInfo = rds
        self.s3: s3_template_info_.S3TemplateInfo = s3
        self.warm_tier_protect: warm_tier_protect_template_info_.WarmTierProtectTemplateInfo = (
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

        # Extract variables from the dictionary
        val = dictionary['asset_types_enabled']
        val_asset_types_enabled = val

        val = dictionary['available_template_version']
        val_available_template_version = val

        val = dictionary['dynamodb']
        val_dynamodb = dynamodb_template_info_.DynamodbTemplateInfo.from_dictionary(val)

        val = dictionary['ebs']
        val_ebs = ebs_template_info_.EbsTemplateInfo.from_dictionary(val)

        val = dictionary['ec2']
        val_ec2 = ec2_template_info_.Ec2TemplateInfo.from_dictionary(val)

        val = dictionary['ec2_mssql']
        val_ec2_mssql = ec2_mssql_template_info_.EC2MSSQLTemplateInfo.from_dictionary(val)

        val = dictionary['iceberg']
        val_iceberg = iceberg_template_info_.IcebergTemplateInfo.from_dictionary(val)

        val = dictionary['rds']
        val_rds = rds_template_info_.RdsTemplateInfo.from_dictionary(val)

        val = dictionary['s3']
        val_s3 = s3_template_info_.S3TemplateInfo.from_dictionary(val)

        val = dictionary['warm_tier_protect']
        val_warm_tier_protect = (
            warm_tier_protect_template_info_.WarmTierProtectTemplateInfo.from_dictionary(val)
        )

        # Return an object of this model
        return cls(
            val_asset_types_enabled,  # type: ignore
            val_available_template_version,  # type: ignore
            val_dynamodb,  # type: ignore
            val_ebs,  # type: ignore
            val_ec2,  # type: ignore
            val_ec2_mssql,  # type: ignore
            val_iceberg,  # type: ignore
            val_rds,  # type: ignore
            val_s3,  # type: ignore
            val_warm_tier_protect,  # type: ignore
        )
