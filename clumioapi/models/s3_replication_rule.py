#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import s3_delete_marker_replication
from clumioapi.models import s3_destination
from clumioapi.models import s3_existing_object_replication
from clumioapi.models import s3_replication_rule_filter
from clumioapi.models import s3_source_selection_criteria

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
        p_filter:
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
    _names = {
        'delete_marker_replication': 'delete_marker_replication',
        'destination': 'destination',
        'existing_object_replication': 'existing_object_replication',
        'p_filter': 'filter',
        'p_id': 'id',
        'priority': 'priority',
        'source_selection_criteria': 'source_selection_criteria',
        'status': 'status',
    }

    def __init__(
        self,
        delete_marker_replication: s3_delete_marker_replication.S3DeleteMarkerReplication = None,
        destination: s3_destination.S3Destination = None,
        existing_object_replication: s3_existing_object_replication.S3ExistingObjectReplication = None,
        p_filter: s3_replication_rule_filter.S3ReplicationRuleFilter = None,
        p_id: str = None,
        priority: int = None,
        source_selection_criteria: s3_source_selection_criteria.S3SourceSelectionCriteria = None,
        status: str = None,
    ) -> None:
        """Constructor for the S3ReplicationRule class."""

        # Initialize members of the class
        self.delete_marker_replication: s3_delete_marker_replication.S3DeleteMarkerReplication = (
            delete_marker_replication
        )
        self.destination: s3_destination.S3Destination = destination
        self.existing_object_replication: s3_existing_object_replication.S3ExistingObjectReplication = (
            existing_object_replication
        )
        self.p_filter: s3_replication_rule_filter.S3ReplicationRuleFilter = p_filter
        self.p_id: str = p_id
        self.priority: int = priority
        self.source_selection_criteria: s3_source_selection_criteria.S3SourceSelectionCriteria = (
            source_selection_criteria
        )
        self.status: str = status

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
        key = 'delete_marker_replication'
        delete_marker_replication = (
            s3_delete_marker_replication.S3DeleteMarkerReplication.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'destination'
        destination = (
            s3_destination.S3Destination.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'existing_object_replication'
        existing_object_replication = (
            s3_existing_object_replication.S3ExistingObjectReplication.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'filter'
        p_filter = (
            s3_replication_rule_filter.S3ReplicationRuleFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        priority = dictionary.get('priority')
        key = 'source_selection_criteria'
        source_selection_criteria = (
            s3_source_selection_criteria.S3SourceSelectionCriteria.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        status = dictionary.get('status')
        # Return an object of this model
        return cls(
            delete_marker_replication,
            destination,
            existing_object_replication,
            p_filter,
            p_id,
            priority,
            source_selection_criteria,
            status,
        )
