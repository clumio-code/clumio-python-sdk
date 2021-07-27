#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import consolidated_alert_details
from clumioapi.models import consolidated_alert_links
from clumioapi.models import consolidated_alert_parent_entity

T = TypeVar('T', bound='UpdateConsolidatedAlertResponse')


class UpdateConsolidatedAlertResponse:
    """Implementation of the 'UpdateConsolidatedAlertResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        active_entity_count:
            The number of currently active individual alerts associated with the
            consolidated alert.
        cause:
            The issue that generated the alert. Each alert cause is associated with an alert
            type.
        cleared_entity_count:
            The number of cleared individual alerts associated with the consolidated alert.
        cleared_timestamp:
            The timestamp of when the consolidated alert was cleared, if ever. Represented
            in RFC-3339 format. If this alert has not been cleared, this field will have a
            value of `null`.
            A consolidated alert goes into "cleared" status when all of its associated
            individual alerts are in "cleared" status or when a Clumio user manually clears
            it.
        details:
            Additional information about the consolidated alert.
        id:
            The Clumio-assigned ID of the consolidated alert.
        notes:
            A record of user-provided information about the alert.
        parent_entity:
            The entity associated with or affected by the alert.
        raised_timestamp:
            The timestamp of when the consolidated alert was initially raised. Represented
            in RFC-3339 format.
        severity:
            The alert severity level. Values include "error" and "warning".
        status:
            The consolidated alert status. A consolidated alert is in "active" status if one
            or more of its associated individual alerts is in "active" status.
            A consolidated alert goes into "cleared" status when all of its associated
            individual alerts are in "cleared" status or when a Clumio user manually clears
            it.
        type:
            The general alert category. An alert type may be associated with multiple alert
            causes. Examples of alert types include "tag_conflict" and "policy_violated".
            Refer to the Alert Type table for a complete list of alert types.
        updated_timestamp:
            The timestamp of when the consolidated alert was last updated. Represented in
            RFC-3339 format.
            Raising a new individual alert will update its associated consolidated alert.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'active_entity_count': 'active_entity_count',
        'cause': 'cause',
        'cleared_entity_count': 'cleared_entity_count',
        'cleared_timestamp': 'cleared_timestamp',
        'details': 'details',
        'id': 'id',
        'notes': 'notes',
        'parent_entity': 'parent_entity',
        'raised_timestamp': 'raised_timestamp',
        'severity': 'severity',
        'status': 'status',
        'type': 'type',
        'updated_timestamp': 'updated_timestamp',
    }

    def __init__(
        self,
        links: consolidated_alert_links.ConsolidatedAlertLinks = None,
        active_entity_count: int = None,
        cause: str = None,
        cleared_entity_count: int = None,
        cleared_timestamp: str = None,
        details: consolidated_alert_details.ConsolidatedAlertDetails = None,
        id: str = None,
        notes: str = None,
        parent_entity: consolidated_alert_parent_entity.ConsolidatedAlertParentEntity = None,
        raised_timestamp: str = None,
        severity: str = None,
        status: str = None,
        type: str = None,
        updated_timestamp: str = None,
    ) -> None:
        """Constructor for the UpdateConsolidatedAlertResponse class."""

        # Initialize members of the class
        self.links: consolidated_alert_links.ConsolidatedAlertLinks = links
        self.active_entity_count: int = active_entity_count
        self.cause: str = cause
        self.cleared_entity_count: int = cleared_entity_count
        self.cleared_timestamp: str = cleared_timestamp
        self.details: consolidated_alert_details.ConsolidatedAlertDetails = details
        self.id: str = id
        self.notes: str = notes
        self.parent_entity: consolidated_alert_parent_entity.ConsolidatedAlertParentEntity = (
            parent_entity
        )
        self.raised_timestamp: str = raised_timestamp
        self.severity: str = severity
        self.status: str = status
        self.type: str = type
        self.updated_timestamp: str = updated_timestamp

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
        key = '_links'
        links = (
            consolidated_alert_links.ConsolidatedAlertLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        active_entity_count = dictionary.get('active_entity_count')
        cause = dictionary.get('cause')
        cleared_entity_count = dictionary.get('cleared_entity_count')
        cleared_timestamp = dictionary.get('cleared_timestamp')
        key = 'details'
        details = (
            consolidated_alert_details.ConsolidatedAlertDetails.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        id = dictionary.get('id')
        notes = dictionary.get('notes')
        key = 'parent_entity'
        parent_entity = (
            consolidated_alert_parent_entity.ConsolidatedAlertParentEntity.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        raised_timestamp = dictionary.get('raised_timestamp')
        severity = dictionary.get('severity')
        status = dictionary.get('status')
        type = dictionary.get('type')
        updated_timestamp = dictionary.get('updated_timestamp')
        # Return an object of this model
        return cls(
            links,
            active_entity_count,
            cause,
            cleared_entity_count,
            cleared_timestamp,
            details,
            id,
            notes,
            parent_entity,
            raised_timestamp,
            severity,
            status,
            type,
            updated_timestamp,
        )
