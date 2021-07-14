#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_ds_grouping_criteria
from clumioapi.models import m365_grouping_criteria
from clumioapi.models import v_mware_ds_grouping_criteria

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
        vmware:
            The entity type used to group organizational units for VMware resources.
    """

    # Create a mapping from Model property names to API property names
    _names = {'aws': 'aws', 'microsoft365': 'microsoft365', 'vmware': 'vmware'}

    def __init__(
        self,
        aws: aws_ds_grouping_criteria.AwsDsGroupingCriteria = None,
        microsoft365: m365_grouping_criteria.M365GroupingCriteria = None,
        vmware: v_mware_ds_grouping_criteria.VMwareDsGroupingCriteria = None,
    ) -> None:
        """Constructor for the OUGroupingCriteria class."""

        # Initialize members of the class
        self.aws: aws_ds_grouping_criteria.AwsDsGroupingCriteria = aws
        self.microsoft365: m365_grouping_criteria.M365GroupingCriteria = microsoft365
        self.vmware: v_mware_ds_grouping_criteria.VMwareDsGroupingCriteria = vmware

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
        key = 'aws'
        aws = (
            aws_ds_grouping_criteria.AwsDsGroupingCriteria.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'microsoft365'
        microsoft365 = (
            m365_grouping_criteria.M365GroupingCriteria.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'vmware'
        vmware = (
            v_mware_ds_grouping_criteria.VMwareDsGroupingCriteria.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(aws, microsoft365, vmware)
