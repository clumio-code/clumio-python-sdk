#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import alert_embedded
from clumioapi.models import alert_links
from clumioapi.models import alert_parent_entity
from clumioapi.models import alert_primary_entity
from clumioapi.models import individual_alert_details
from clumioapi.models import rest_entity

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
    _names = {
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
        embedded: alert_embedded.AlertEmbedded = None,
        etag: str = None,
        links: alert_links.AlertLinks = None,
        cause: str = None,
        cleared_timestamp: str = None,
        consolidated_alert_id: str = None,
        details: individual_alert_details.IndividualAlertDetails = None,
        p_id: str = None,
        notes: str = None,
        parent_entity: alert_parent_entity.AlertParentEntity = None,
        primary_entity: alert_primary_entity.AlertPrimaryEntity = None,
        raised_count: int = None,
        raised_timestamp: str = None,
        severity: str = None,
        status: str = None,
        tags: Sequence[rest_entity.RestEntity] = None,
        p_type: str = None,
        updated_timestamp: str = None,
    ) -> None:
        """Constructor for the ReadAlertResponse class."""

        # Initialize members of the class
        self.embedded: alert_embedded.AlertEmbedded = embedded
        self.etag: str = etag
        self.links: alert_links.AlertLinks = links
        self.cause: str = cause
        self.cleared_timestamp: str = cleared_timestamp
        self.consolidated_alert_id: str = consolidated_alert_id
        self.details: individual_alert_details.IndividualAlertDetails = details
        self.p_id: str = p_id
        self.notes: str = notes
        self.parent_entity: alert_parent_entity.AlertParentEntity = parent_entity
        self.primary_entity: alert_primary_entity.AlertPrimaryEntity = primary_entity
        self.raised_count: int = raised_count
        self.raised_timestamp: str = raised_timestamp
        self.severity: str = severity
        self.status: str = status
        self.tags: Sequence[rest_entity.RestEntity] = tags
        self.p_type: str = p_type
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
        key = '_embedded'
        embedded = (
            alert_embedded.AlertEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            alert_links.AlertLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        cause = dictionary.get('cause')
        cleared_timestamp = dictionary.get('cleared_timestamp')
        consolidated_alert_id = dictionary.get('consolidated_alert_id')
        key = 'details'
        details = (
            individual_alert_details.IndividualAlertDetails.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        notes = dictionary.get('notes')
        key = 'parent_entity'
        parent_entity = (
            alert_parent_entity.AlertParentEntity.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'primary_entity'
        primary_entity = (
            alert_primary_entity.AlertPrimaryEntity.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        raised_count = dictionary.get('raised_count')
        raised_timestamp = dictionary.get('raised_timestamp')
        severity = dictionary.get('severity')
        status = dictionary.get('status')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(rest_entity.RestEntity.from_dictionary(value))

        p_type = dictionary.get('type')
        updated_timestamp = dictionary.get('updated_timestamp')
        # Return an object of this model
        return cls(
            embedded,
            etag,
            links,
            cause,
            cleared_timestamp,
            consolidated_alert_id,
            details,
            p_id,
            notes,
            parent_entity,
            primary_entity,
            raised_count,
            raised_timestamp,
            severity,
            status,
            tags,
            p_type,
            updated_timestamp,
        )
