#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import alert_embedded as alert_embedded_
from clumioapi.models import alert_links as alert_links_
from clumioapi.models import alert_parent_entity as alert_parent_entity_
from clumioapi.models import alert_primary_entity as alert_primary_entity_
from clumioapi.models import individual_alert_details as individual_alert_details_
from clumioapi.models import rest_entity as rest_entity_

T = TypeVar('T', bound='ReadAlertResponse')


class ReadAlertResponse:
    """Implementation of the 'ReadAlertResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        cause:
            The issue that generated the alert. Each cause belongs to an alert type.
        cleared_timestamp:
            The timestamp of when the alert was cleared, either automatically by Clumio or
            manually by a Clumio user.
            Represented in RFC-3339 format. If this alert has not been cleared, then this
            field has a value of `null`.
        consolidated_alert_id:
            The Clumio-assigned ID of the consolidated alert associated with this individual
            alert. Alerts are consolidated based on matching parent entity, alert type, and
            alert cause.
        details:
            Additional information about the alert.
        p_id:
            The Clumio-assigned ID of the individual alert.
        notes:
            A record of user-provided information about the alert.
        parent_entity:
            The parent object of the primary entity associated with or affected by the
            alert. For example, "aws_environment" is the parent entity of primary entity
            "aws_ebs_volume".
        primary_entity:
            The primary object associated with or affected by the alert. Examples of primary
            entities include "aws_connection", "aws_ebs_volume".
        raised_count:
            The number of times the alert has recurred for this primary entity.
        raised_timestamp:
            The timestamp of when the alert was raised. Represented in RFC-3339 format.
        severity:
            The alert severity level. Values include "error" and "warning".
        status:
            The individual alert status. An individual alert that is in "active" status is
            one that is still open and has yet to be addressed.
            An individual alert that is in "cleared" status is one that has been cleared,
            either automatically by Clumio or manually by a Clumio user.
        tags:
            A list of associated objects for the alert.
        p_type:
            The general alert category. Some alert types may be associated with multiple
            causes.
            Refer to the Alert Type table for a complete list of alert types.
        updated_timestamp:
            The timestamp of when the alert was last updated. Represented in RFC-3339
            format.
            The alert is updated whenever there is a new occurrence of the same alert within
            the same entity.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'etag': '_etag',
        'links': '_links',
        'cause': 'cause',
        'cleared_timestamp': 'cleared_timestamp',
        'consolidated_alert_id': 'consolidated_alert_id',
        'details': 'details',
        'p_id': 'id',
        'notes': 'notes',
        'parent_entity': 'parent_entity',
        'primary_entity': 'primary_entity',
        'raised_count': 'raised_count',
        'raised_timestamp': 'raised_timestamp',
        'severity': 'severity',
        'status': 'status',
        'tags': 'tags',
        'p_type': 'type',
        'updated_timestamp': 'updated_timestamp',
    }

    def __init__(
        self,
        embedded: alert_embedded_.AlertEmbedded | None = None,
        etag: str | None = None,
        links: alert_links_.AlertLinks | None = None,
        cause: str | None = None,
        cleared_timestamp: str | None = None,
        consolidated_alert_id: str | None = None,
        details: individual_alert_details_.IndividualAlertDetails | None = None,
        p_id: str | None = None,
        notes: str | None = None,
        parent_entity: alert_parent_entity_.AlertParentEntity | None = None,
        primary_entity: alert_primary_entity_.AlertPrimaryEntity | None = None,
        raised_count: int | None = None,
        raised_timestamp: str | None = None,
        severity: str | None = None,
        status: str | None = None,
        tags: Sequence[rest_entity_.RestEntity] | None = None,
        p_type: str | None = None,
        updated_timestamp: str | None = None,
    ) -> None:
        """Constructor for the ReadAlertResponse class."""

        # Initialize members of the class
        self.embedded: alert_embedded_.AlertEmbedded | None = embedded
        self.etag: str | None = etag
        self.links: alert_links_.AlertLinks | None = links
        self.cause: str | None = cause
        self.cleared_timestamp: str | None = cleared_timestamp
        self.consolidated_alert_id: str | None = consolidated_alert_id
        self.details: individual_alert_details_.IndividualAlertDetails | None = details
        self.p_id: str | None = p_id
        self.notes: str | None = notes
        self.parent_entity: alert_parent_entity_.AlertParentEntity | None = parent_entity
        self.primary_entity: alert_primary_entity_.AlertPrimaryEntity | None = primary_entity
        self.raised_count: int | None = raised_count
        self.raised_timestamp: str | None = raised_timestamp
        self.severity: str | None = severity
        self.status: str | None = status
        self.tags: Sequence[rest_entity_.RestEntity] | None = tags
        self.p_type: str | None = p_type
        self.updated_timestamp: str | None = updated_timestamp

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
        val = dictionary.get('_embedded', None)
        val_embedded = alert_embedded_.AlertEmbedded.from_dictionary(val)

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = alert_links_.AlertLinks.from_dictionary(val)

        val = dictionary.get('cause', None)
        val_cause = val

        val = dictionary.get('cleared_timestamp', None)
        val_cleared_timestamp = val

        val = dictionary.get('consolidated_alert_id', None)
        val_consolidated_alert_id = val

        val = dictionary.get('details', None)
        val_details = individual_alert_details_.IndividualAlertDetails.from_dictionary(val)

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('notes', None)
        val_notes = val

        val = dictionary.get('parent_entity', None)
        val_parent_entity = alert_parent_entity_.AlertParentEntity.from_dictionary(val)

        val = dictionary.get('primary_entity', None)
        val_primary_entity = alert_primary_entity_.AlertPrimaryEntity.from_dictionary(val)

        val = dictionary.get('raised_count', None)
        val_raised_count = val

        val = dictionary.get('raised_timestamp', None)
        val_raised_timestamp = val

        val = dictionary.get('severity', None)
        val_severity = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(rest_entity_.RestEntity.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_cause,
            val_cleared_timestamp,
            val_consolidated_alert_id,
            val_details,
            val_p_id,
            val_notes,
            val_parent_entity,
            val_primary_entity,
            val_raised_count,
            val_raised_timestamp,
            val_severity,
            val_status,
            val_tags,
            val_p_type,
            val_updated_timestamp,
        )
