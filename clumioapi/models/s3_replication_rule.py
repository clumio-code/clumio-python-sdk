#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import s3_delete_marker_replication as s3_delete_marker_replication_
from clumioapi.models import s3_destination as s3_destination_
from clumioapi.models import s3_existing_object_replication as s3_existing_object_replication_
from clumioapi.models import s3_replication_rule_filter as s3_replication_rule_filter_
from clumioapi.models import s3_source_selection_criteria as s3_source_selection_criteria_
import requests

T = TypeVar('T', bound='S3ReplicationRule')


@dataclasses.dataclass
class S3ReplicationRule:
    """Implementation of the 'S3ReplicationRule' model.

    Specifies which Amazon S3 objects to replicate and where to store the replicas.

    Attributes:
        DeleteMarkerReplication:
            Specifies whether amazon s3 replicates delete markers.

        Destination:
            Specifies information about where to publish analysis or configuration results.

        ExistingObjectReplication:
            Configuration to replicate existing source bucket objects.

        Filter:
            A filter that identifies the subset of objects
            to which the replication rule applies.

        Id:
            A unique identifier for the rule (max 255 characters).

        Priority:
            The priority indicates which rule has precedence whenever
            two or more replication rules conflict.

        SourceSelectionCriteria:
            A container that describes additional filters for identifying
            the source objects that you want to replicate.

        Status:
            Specifies whether the rule is enabled.

    """

    DeleteMarkerReplication: s3_delete_marker_replication_.S3DeleteMarkerReplication | None = None
    Destination: s3_destination_.S3Destination | None = None
    ExistingObjectReplication: (
        s3_existing_object_replication_.S3ExistingObjectReplication | None
    ) = None
    Filter: s3_replication_rule_filter_.S3ReplicationRuleFilter | None = None
    Id: str | None = None
    Priority: int | None = None
    SourceSelectionCriteria: s3_source_selection_criteria_.S3SourceSelectionCriteria | None = None
    Status: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('delete_marker_replication', None)
        val_delete_marker_replication = (
            s3_delete_marker_replication_.S3DeleteMarkerReplication.from_dictionary(val)
        )

        val = dictionary.get('destination', None)
        val_destination = s3_destination_.S3Destination.from_dictionary(val)

        val = dictionary.get('existing_object_replication', None)
        val_existing_object_replication = (
            s3_existing_object_replication_.S3ExistingObjectReplication.from_dictionary(val)
        )

        val = dictionary.get('filter', None)
        val_filter = s3_replication_rule_filter_.S3ReplicationRuleFilter.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('priority', None)
        val_priority = val

        val = dictionary.get('source_selection_criteria', None)
        val_source_selection_criteria = (
            s3_source_selection_criteria_.S3SourceSelectionCriteria.from_dictionary(val)
        )

        val = dictionary.get('status', None)
        val_status = val

        # Return an object of this model
        return cls(
            val_delete_marker_replication,
            val_destination,
            val_existing_object_replication,
            val_filter,
            val_id,
            val_priority,
            val_source_selection_criteria,
            val_status,
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
