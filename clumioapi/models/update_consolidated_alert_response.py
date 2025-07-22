#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import consolidated_alert_details as consolidated_alert_details_
from clumioapi.models import consolidated_alert_links as consolidated_alert_links_
from clumioapi.models import consolidated_alert_parent_entity as consolidated_alert_parent_entity_

T = TypeVar('T', bound='UpdateConsolidatedAlertResponse')


class UpdateConsolidatedAlertResponse:
    """Implementation of the 'UpdateConsolidatedAlertResponse' model.

    Attributes:
        etag:
            The ETag value.
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
        p_id:
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
        p_type:
            The general alert category. An alert type may be associated with multiple alert
            causes. Examples of alert types include "tag_conflict" and "policy_violated".
            Refer to the Alert Type table for a complete list of alert types.
        updated_timestamp:
            The timestamp of when the consolidated alert was last updated. Represented in
            RFC-3339 format.
            Raising a new individual alert will update its associated consolidated alert.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'etag': '_etag',
        'links': '_links',
        'active_entity_count': 'active_entity_count',
        'cause': 'cause',
        'cleared_entity_count': 'cleared_entity_count',
        'cleared_timestamp': 'cleared_timestamp',
        'details': 'details',
        'p_id': 'id',
        'notes': 'notes',
        'parent_entity': 'parent_entity',
        'raised_timestamp': 'raised_timestamp',
        'severity': 'severity',
        'status': 'status',
        'p_type': 'type',
        'updated_timestamp': 'updated_timestamp',
    }

    def __init__(
        self,
        etag: str,
        links: consolidated_alert_links_.ConsolidatedAlertLinks,
        active_entity_count: int,
        cause: str,
        cleared_entity_count: int,
        cleared_timestamp: str,
        details: consolidated_alert_details_.ConsolidatedAlertDetails,
        p_id: str,
        notes: str,
        parent_entity: consolidated_alert_parent_entity_.ConsolidatedAlertParentEntity,
        raised_timestamp: str,
        severity: str,
        status: str,
        p_type: str,
        updated_timestamp: str,
    ) -> None:
        """Constructor for the UpdateConsolidatedAlertResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: consolidated_alert_links_.ConsolidatedAlertLinks = links
        self.active_entity_count: int = active_entity_count
        self.cause: str = cause
        self.cleared_entity_count: int = cleared_entity_count
        self.cleared_timestamp: str = cleared_timestamp
        self.details: consolidated_alert_details_.ConsolidatedAlertDetails = details
        self.p_id: str = p_id
        self.notes: str = notes
        self.parent_entity: consolidated_alert_parent_entity_.ConsolidatedAlertParentEntity = (
            parent_entity
        )
        self.raised_timestamp: str = raised_timestamp
        self.severity: str = severity
        self.status: str = status
        self.p_type: str = p_type
        self.updated_timestamp: str = updated_timestamp

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
        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = consolidated_alert_links_.ConsolidatedAlertLinks.from_dictionary(val)

        val = dictionary['active_entity_count']
        val_active_entity_count = val

        val = dictionary['cause']
        val_cause = val

        val = dictionary['cleared_entity_count']
        val_cleared_entity_count = val

        val = dictionary['cleared_timestamp']
        val_cleared_timestamp = val

        val = dictionary['details']
        val_details = consolidated_alert_details_.ConsolidatedAlertDetails.from_dictionary(val)

        val = dictionary['id']
        val_p_id = val

        val = dictionary['notes']
        val_notes = val

        val = dictionary['parent_entity']
        val_parent_entity = (
            consolidated_alert_parent_entity_.ConsolidatedAlertParentEntity.from_dictionary(val)
        )

        val = dictionary['raised_timestamp']
        val_raised_timestamp = val

        val = dictionary['severity']
        val_severity = val

        val = dictionary['status']
        val_status = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['updated_timestamp']
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_active_entity_count,  # type: ignore
            val_cause,  # type: ignore
            val_cleared_entity_count,  # type: ignore
            val_cleared_timestamp,  # type: ignore
            val_details,  # type: ignore
            val_p_id,  # type: ignore
            val_notes,  # type: ignore
            val_parent_entity,  # type: ignore
            val_raised_timestamp,  # type: ignore
            val_severity,  # type: ignore
            val_status,  # type: ignore
            val_p_type,  # type: ignore
            val_updated_timestamp,  # type: ignore
        )
