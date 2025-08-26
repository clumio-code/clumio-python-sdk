#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import key_schema_element as key_schema_element_
from clumioapi.models import projection as projection_
from clumioapi.models import provisioned_throughput as provisioned_throughput_
import requests

T = TypeVar('T', bound='GlobalSecondaryIndex')


@dataclasses.dataclass
class GlobalSecondaryIndex:
    """Implementation of the 'GlobalSecondaryIndex' model.

        Represents the properties of a global secondary index.

        Attributes:
            ContributorInsightsStatus:
                Indicates whether dynamodb contributor insights is enabled (true) or disabled (false)
    on the index.
    for [post /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this is defaulted to the
    value set in backup if `null`.

            IndexName:
                The name of the global secondary index.

            KeySchema:
                The complete key schema for a global secondary index, which consists of one or more
    pairs of attribute names and key types.

            Projection:
                Represents attributes that are copied (projected) from the table into an index. these are in addition to the
    primary key attributes and index key attributes, which are automatically projected.

            ProvisionedThroughput:
                Represents the provisioned throughput settings for a dynamodb table.

    """

    ContributorInsightsStatus: bool | None = None
    IndexName: str | None = None
    KeySchema: Sequence[key_schema_element_.KeySchemaElement] | None = None
    Projection: projection_.Projection | None = None
    ProvisionedThroughput: provisioned_throughput_.ProvisionedThroughput | None = None

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
        val = dictionary.get('contributor_insights_status', None)
        val_contributor_insights_status = val

        val = dictionary.get('index_name', None)
        val_index_name = val

        val = dictionary.get('key_schema', None)

        val_key_schema = []
        if val:
            for value in val:
                val_key_schema.append(key_schema_element_.KeySchemaElement.from_dictionary(value))

        val = dictionary.get('projection', None)
        val_projection = projection_.Projection.from_dictionary(val)

        val = dictionary.get('provisioned_throughput', None)
        val_provisioned_throughput = provisioned_throughput_.ProvisionedThroughput.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_contributor_insights_status,
            val_index_name,
            val_key_schema,
            val_projection,
            val_provisioned_throughput,
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
