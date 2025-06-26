#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import dynamodb_template_info
from clumioapi.models import ebs_template_info
from clumioapi.models import ec2_mssql_template_info
from clumioapi.models import ec2_template_info
from clumioapi.models import iceberg_template_info
from clumioapi.models import rds_template_info
from clumioapi.models import s3_template_info
from clumioapi.models import warm_tier_protect_template_info

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
    _names = {
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
        asset_types_enabled: Sequence[str] = None,
        available_template_version: str = None,
        dynamodb: dynamodb_template_info.DynamodbTemplateInfo = None,
        ebs: ebs_template_info.EbsTemplateInfo = None,
        ec2: ec2_template_info.Ec2TemplateInfo = None,
        ec2_mssql: ec2_mssql_template_info.EC2MSSQLTemplateInfo = None,
        iceberg: iceberg_template_info.IcebergTemplateInfo = None,
        rds: rds_template_info.RdsTemplateInfo = None,
        s3: s3_template_info.S3TemplateInfo = None,
        warm_tier_protect: warm_tier_protect_template_info.WarmTierProtectTemplateInfo = None,
    ) -> None:
        """Constructor for the TemplateConfigurationV2 class."""

        # Initialize members of the class
        self.asset_types_enabled: Sequence[str] = asset_types_enabled
        self.available_template_version: str = available_template_version
        self.dynamodb: dynamodb_template_info.DynamodbTemplateInfo = dynamodb
        self.ebs: ebs_template_info.EbsTemplateInfo = ebs
        self.ec2: ec2_template_info.Ec2TemplateInfo = ec2
        self.ec2_mssql: ec2_mssql_template_info.EC2MSSQLTemplateInfo = ec2_mssql
        self.iceberg: iceberg_template_info.IcebergTemplateInfo = iceberg
        self.rds: rds_template_info.RdsTemplateInfo = rds
        self.s3: s3_template_info.S3TemplateInfo = s3
        self.warm_tier_protect: warm_tier_protect_template_info.WarmTierProtectTemplateInfo = (
            warm_tier_protect
        )

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
        available_template_version = dictionary.get('available_template_version')
        key = 'dynamodb'
        dynamodb = (
            dynamodb_template_info.DynamodbTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ebs'
        ebs = (
            ebs_template_info.EbsTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ec2'
        ec2 = (
            ec2_template_info.Ec2TemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'ec2_mssql'
        ec2_mssql = (
            ec2_mssql_template_info.EC2MSSQLTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'iceberg'
        iceberg = (
            iceberg_template_info.IcebergTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'rds'
        rds = (
            rds_template_info.RdsTemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 's3'
        s3 = (
            s3_template_info.S3TemplateInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'warm_tier_protect'
        warm_tier_protect = (
            warm_tier_protect_template_info.WarmTierProtectTemplateInfo.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(
            asset_types_enabled,
            available_template_version,
            dynamodb,
            ebs,
            ec2,
            ec2_mssql,
            iceberg,
            rds,
            s3,
            warm_tier_protect,
        )
