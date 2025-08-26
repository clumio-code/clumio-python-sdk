#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import dynamodb_template_info as dynamodb_template_info_
from clumioapi.models import ebs_template_info as ebs_template_info_
from clumioapi.models import ec2_mssql_template_info as ec2_mssql_template_info_
from clumioapi.models import ec2_template_info as ec2_template_info_
from clumioapi.models import iceberg_on_glue_template_info as iceberg_on_glue_template_info_
from clumioapi.models import rds_template_info as rds_template_info_
from clumioapi.models import s3_template_info as s3_template_info_
from clumioapi.models import warm_tier_protect_template_info as warm_tier_protect_template_info_
import requests

T = TypeVar('T', bound='TemplateConfigurationV2')


@dataclasses.dataclass
class TemplateConfigurationV2:
    """Implementation of the 'TemplateConfigurationV2' model.

    The configuration of the given template

    Attributes:
        AssetTypesEnabled:
            The aws asset types supported with the available version of the template.

        AvailableTemplateVersion:
            The latest available version for the template.

        Dynamodb:
            The latest available information for the dynamodb feature.

        Ebs:
            .

        Ec2:
            .

        Ec2Mssql:
            The latest available information for the ec2 mssql feature.

        IcebergOnGlue:
            Icebergongluetemplateinfo is the latest available information for the icebergonglue feature.

        Rds:
            .

        S3:
            The latest available information for the s3 feature.

        WarmTierProtect:
            Configuration information about the warm-tier protect feature of the template.

    """

    AssetTypesEnabled: Sequence[str] | None = None
    AvailableTemplateVersion: str | None = None
    Dynamodb: dynamodb_template_info_.DynamodbTemplateInfo | None = None
    Ebs: ebs_template_info_.EbsTemplateInfo | None = None
    Ec2: ec2_template_info_.Ec2TemplateInfo | None = None
    Ec2Mssql: ec2_mssql_template_info_.EC2MSSQLTemplateInfo | None = None
    IcebergOnGlue: iceberg_on_glue_template_info_.IcebergOnGlueTemplateInfo | None = None
    Rds: rds_template_info_.RdsTemplateInfo | None = None
    S3: s3_template_info_.S3TemplateInfo | None = None
    WarmTierProtect: warm_tier_protect_template_info_.WarmTierProtectTemplateInfo | None = None

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

        val = dictionary.get('iceberg_on_glue', None)
        val_iceberg_on_glue = (
            iceberg_on_glue_template_info_.IcebergOnGlueTemplateInfo.from_dictionary(val)
        )

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
            val_iceberg_on_glue,
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
