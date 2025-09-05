#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_delete_marker_replication as s3_delete_marker_replication_
from clumioapi.models import s3_destination as s3_destination_
from clumioapi.models import s3_existing_object_replication as s3_existing_object_replication_
from clumioapi.models import s3_replication_rule_filter as s3_replication_rule_filter_
from clumioapi.models import s3_source_selection_criteria as s3_source_selection_criteria_

T = TypeVar('T', bound='S3ReplicationRule')


class S3ReplicationRule:
    """Implementation of the 'S3ReplicationRule' model.

    Specifies which Amazon S3 objects to replicate and where to store the replicas.

    Attributes:
        delete_marker_replication:
            Specifies whether Amazon S3 replicates delete markers.
        destination:
            Specifies information about where to publish analysis or configuration results.
        existing_object_replication:
            Configuration to replicate existing source bucket objects.
        filter:
            A filter that identifies the subset of objects
            to which the replication rule applies.
        p_id:
            A unique identifier for the rule (max 255 characters).
        priority:
            The priority indicates which rule has precedence whenever
            two or more replication rules conflict.
        source_selection_criteria:
            A container that describes additional filters for identifying
            the source objects that you want to replicate.
        status:
            Specifies whether the rule is enabled.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'delete_marker_replication': 'delete_marker_replication',
        'destination': 'destination',
        'existing_object_replication': 'existing_object_replication',
        'filter': 'filter',
        'p_id': 'id',
        'priority': 'priority',
        'source_selection_criteria': 'source_selection_criteria',
        'status': 'status',
    }

    def __init__(
        self,
        delete_marker_replication: (
            s3_delete_marker_replication_.S3DeleteMarkerReplication | None
        ) = None,
        destination: s3_destination_.S3Destination | None = None,
        existing_object_replication: (
            s3_existing_object_replication_.S3ExistingObjectReplication | None
        ) = None,
        filter: s3_replication_rule_filter_.S3ReplicationRuleFilter | None = None,
        p_id: str | None = None,
        priority: int | None = None,
        source_selection_criteria: (
            s3_source_selection_criteria_.S3SourceSelectionCriteria | None
        ) = None,
        status: str | None = None,
    ) -> None:
        """Constructor for the S3ReplicationRule class."""

        # Initialize members of the class
        self.delete_marker_replication: (
            s3_delete_marker_replication_.S3DeleteMarkerReplication | None
        ) = delete_marker_replication
        self.destination: s3_destination_.S3Destination | None = destination
        self.existing_object_replication: (
            s3_existing_object_replication_.S3ExistingObjectReplication | None
        ) = existing_object_replication
        self.filter: s3_replication_rule_filter_.S3ReplicationRuleFilter | None = filter
        self.p_id: str | None = p_id
        self.priority: int | None = priority
        self.source_selection_criteria: (
            s3_source_selection_criteria_.S3SourceSelectionCriteria | None
        ) = source_selection_criteria
        self.status: str | None = status

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
        val_p_id = val

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
            val_p_id,
            val_priority,
            val_source_selection_criteria,
            val_status,
        )
