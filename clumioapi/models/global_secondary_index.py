#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import key_schema_element as key_schema_element_
from clumioapi.models import projection as projection_
from clumioapi.models import provisioned_throughput as provisioned_throughput_

T = TypeVar('T', bound='GlobalSecondaryIndex')


class GlobalSecondaryIndex:
    """Implementation of the 'GlobalSecondaryIndex' model.

    Represents the properties of a global secondary index.

    Attributes:
        contributor_insights_status:
            Indicates whether DynamoDB Contributor Insights is enabled (true) or disabled
            (false)
            on the index.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            is defaulted to the
            value set in backup if `null`.
        index_name:
            The name of the global secondary index.
        key_schema:
            The complete key schema for a global secondary index, which consists of one or
            more
            pairs of attribute names and key types.
        projection:
            Represents attributes that are copied (projected) from the table into an index.
            These are in addition to the
            primary key attributes and index key attributes, which are automatically
            projected.
        provisioned_throughput:
            Represents the provisioned throughput settings for a DynamoDB table.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'contributor_insights_status': 'contributor_insights_status',
        'index_name': 'index_name',
        'key_schema': 'key_schema',
        'projection': 'projection',
        'provisioned_throughput': 'provisioned_throughput',
    }

    def __init__(
        self,
        contributor_insights_status: bool,
        index_name: str,
        key_schema: Sequence[key_schema_element_.KeySchemaElement],
        projection: projection_.Projection,
        provisioned_throughput: provisioned_throughput_.ProvisionedThroughput,
    ) -> None:
        """Constructor for the GlobalSecondaryIndex class."""

        # Initialize members of the class
        self.contributor_insights_status: bool = contributor_insights_status
        self.index_name: str = index_name
        self.key_schema: Sequence[key_schema_element_.KeySchemaElement] = key_schema
        self.projection: projection_.Projection = projection
        self.provisioned_throughput: provisioned_throughput_.ProvisionedThroughput = (
            provisioned_throughput
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
        val = dictionary['contributor_insights_status']
        val_contributor_insights_status = val

        val = dictionary['index_name']
        val_index_name = val

        val = dictionary['key_schema']

        val_key_schema = None
        if val:
            val_key_schema = list()
            for value in val:
                val_key_schema.append(key_schema_element_.KeySchemaElement.from_dictionary(value))

        val = dictionary['projection']
        val_projection = projection_.Projection.from_dictionary(val)

        val = dictionary['provisioned_throughput']
        val_provisioned_throughput = provisioned_throughput_.ProvisionedThroughput.from_dictionary(
            val
        )

        # Return an object of this model
        return cls(
            val_contributor_insights_status,  # type: ignore
            val_index_name,  # type: ignore
            val_key_schema,  # type: ignore
            val_projection,  # type: ignore
            val_provisioned_throughput,  # type: ignore
        )
