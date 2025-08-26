#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_ds_grouping_criteria as aws_ds_grouping_criteria_
from clumioapi.models import m365_grouping_criteria as m365_grouping_criteria_

T = TypeVar('T', bound='OUGroupingCriteria')


class OUGroupingCriteria:
    """Implementation of the 'OUGroupingCriteria' model.

    The grouping criteria for each datasource type.These can only be edited for
    datasource types which do not have anyorganizational units configured.

    Attributes:
        aws:
            The entity type used to group organizational units for AWS resources.
        microsoft365:
            The entity type used to group organizational units for Microsoft 365 resources.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'aws': 'aws', 'microsoft365': 'microsoft365'}

    def __init__(
        self,
        aws: aws_ds_grouping_criteria_.AwsDsGroupingCriteria | None = None,
        microsoft365: m365_grouping_criteria_.M365GroupingCriteria | None = None,
    ) -> None:
        """Constructor for the OUGroupingCriteria class."""

        # Initialize members of the class
        self.aws: aws_ds_grouping_criteria_.AwsDsGroupingCriteria | None = aws
        self.microsoft365: m365_grouping_criteria_.M365GroupingCriteria | None = microsoft365

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
        val = dictionary.get('aws', None)
        val_aws = aws_ds_grouping_criteria_.AwsDsGroupingCriteria.from_dictionary(val)

        val = dictionary.get('microsoft365', None)
        val_microsoft365 = m365_grouping_criteria_.M365GroupingCriteria.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_aws,
            val_microsoft365,
        )
