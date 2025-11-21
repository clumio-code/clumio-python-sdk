#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import alert_embedded as alert_embedded_
from clumioapi.models import alert_links as alert_links_
from clumioapi.models import alert_parent_entity as alert_parent_entity_
from clumioapi.models import alert_primary_entity as alert_primary_entity_
from clumioapi.models import individual_alert_details as individual_alert_details_
from clumioapi.models import rest_entity as rest_entity_
import requests

T = TypeVar('T', bound='UpdateAlertResponse')


@dataclasses.dataclass
class UpdateAlertResponse:
    """Implementation of the 'UpdateAlertResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Etag:
            The etag value.

        Links:
            Urls to pages related to the resource.

        Cause:
            The issue that generated the alert. each cause belongs to an alert type.

        ClearedTimestamp:
            The timestamp of when the alert was cleared, either automatically by clumio or
            manually by a clumio user.
            represented in rfc-3339 format. if this alert has not been cleared, then this
            field has a value of `null`.

        ConsolidatedAlertId:
            The clumio-assigned id of the consolidated alert associated with this individual
            alert. alerts are consolidated based on matching parent entity, alert type, and
            alert cause.

        Details:
            Additional information about the alert.

        Id:
            The clumio-assigned id of the individual alert.

        Notes:
            A record of user-provided information about the alert.

        ParentEntity:
            The parent object of the primary entity associated with or affected by the
            alert. for example, "aws_environment" is the parent entity of primary entity
            "aws_ebs_volume".

        PrimaryEntity:
            The primary object associated with or affected by the alert. examples of primary
            entities include "aws_connection", "aws_ebs_volume".

        RaisedCount:
            The number of times the alert has recurred for this primary entity.

        RaisedTimestamp:
            The timestamp of when the alert was raised. represented in rfc-3339 format.

        Severity:
            The alert severity level. values include "error" and "warning".

        Status:
            The individual alert status. an individual alert that is in "active" status is
            one that is still open and has yet to be addressed.
            an individual alert that is in "cleared" status is one that has been cleared,
            either automatically by clumio or manually by a clumio user.

        Tags:
            A list of associated objects for the alert.

        Type:
            The general alert category. some alert types may be associated with multiple
            causes.
            refer to the alert type table for a complete list of alert types.

        UpdatedTimestamp:
            The timestamp of when the alert was last updated. represented in rfc-3339
            format.
            the alert is updated whenever there is a new occurrence of the same alert within
            the same entity.

    """

    Embedded: alert_embedded_.AlertEmbedded | None = None
    Etag: str | None = None
    Links: alert_links_.AlertLinks | None = None
    Cause: str | None = None
    ClearedTimestamp: str | None = None
    ConsolidatedAlertId: str | None = None
    Details: individual_alert_details_.IndividualAlertDetails | None = None
    Id: str | None = None
    Notes: str | None = None
    ParentEntity: alert_parent_entity_.AlertParentEntity | None = None
    PrimaryEntity: alert_primary_entity_.AlertPrimaryEntity | None = None
    RaisedCount: int | None = None
    RaisedTimestamp: str | None = None
    Severity: str | None = None
    Status: str | None = None
    Tags: Sequence[rest_entity_.RestEntity] | None = None
    Type: str | None = None
    UpdatedTimestamp: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val_id = val

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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(rest_entity_.RestEntity.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
            val_notes,
            val_parent_entity,
            val_primary_entity,
            val_raised_count,
            val_raised_timestamp,
            val_severity,
            val_status,
            val_tags,
            val_type,
            val_updated_timestamp,
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
        model_instance.raw_response = response
        return model_instance
