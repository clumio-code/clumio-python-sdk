#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_ds_grouping_criteria as aws_ds_grouping_criteria_
from clumioapi.models import m365_grouping_criteria as m365_grouping_criteria_
import requests

T = TypeVar('T', bound='OUGroupingCriteria')


@dataclasses.dataclass
class OUGroupingCriteria:
    """Implementation of the 'OUGroupingCriteria' model.

    The grouping criteria for each datasource type.These can only be edited for
    datasource types which do not have anyorganizational units configured.

    Attributes:
        Aws:
            The entity type used to group organizational units for aws resources.

        Microsoft365:
            The entity type used to group organizational units for microsoft 365 resources.

    """

    Aws: aws_ds_grouping_criteria_.AwsDsGroupingCriteria | None = None
    Microsoft365: m365_grouping_criteria_.M365GroupingCriteria | None = None

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
        val = dictionary.get('aws', None)
        val_aws = aws_ds_grouping_criteria_.AwsDsGroupingCriteria.from_dictionary(val)

        val = dictionary.get('microsoft365', None)
        val_microsoft365 = m365_grouping_criteria_.M365GroupingCriteria.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_aws,
            val_microsoft365,
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
