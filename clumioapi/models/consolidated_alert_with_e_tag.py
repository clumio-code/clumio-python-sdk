#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import consolidated_alert_details as consolidated_alert_details_
from clumioapi.models import consolidated_alert_links as consolidated_alert_links_
from clumioapi.models import consolidated_alert_parent_entity as consolidated_alert_parent_entity_
import requests

T = TypeVar('T', bound='ConsolidatedAlertWithETag')


@dataclasses.dataclass
class ConsolidatedAlertWithETag:
    """Implementation of the 'ConsolidatedAlertWithETag' model.

        Attributes:
            Etag:
                The etag value.

            Links:
                Urls to pages related to the resource.

            ActiveEntityCount:
                The number of currently active individual alerts associated with the consolidated alert.

            Cause:
                The issue that generated the alert. each alert cause is associated with an alert type.

            ClearedEntityCount:
                The number of cleared individual alerts associated with the consolidated alert.

            ClearedTimestamp:
                The timestamp of when the consolidated alert was cleared, if ever. represented in rfc-3339 format. if this alert has not been cleared, this field will have a value of `null`.
    a consolidated alert goes into "cleared" status when all of its associated individual alerts are in "cleared" status or when a clumio user manually clears it.

            Details:
                Additional information about the consolidated alert.

            Id:
                The clumio-assigned id of the consolidated alert.

            Notes:
                A record of user-provided information about the alert.

            ParentEntity:
                The entity associated with or affected by the alert.

            RaisedTimestamp:
                The timestamp of when the consolidated alert was initially raised. represented in rfc-3339 format.

            Severity:
                The alert severity level. values include "error" and "warning".

            Status:
                The consolidated alert status. a consolidated alert is in "active" status if one or more of its associated individual alerts is in "active" status.
    a consolidated alert goes into "cleared" status when all of its associated individual alerts are in "cleared" status or when a clumio user manually clears it.

            Type:
                The general alert category. an alert type may be associated with multiple alert causes. examples of alert types include "tag_conflict" and "policy_violated".
    refer to the alert type table for a complete list of alert types.

            UpdatedTimestamp:
                The timestamp of when the consolidated alert was last updated. represented in rfc-3339 format.
    raising a new individual alert will update its associated consolidated alert.

    """

    Etag: str | None = None
    Links: consolidated_alert_links_.ConsolidatedAlertLinks | None = None
    ActiveEntityCount: int | None = None
    Cause: str | None = None
    ClearedEntityCount: int | None = None
    ClearedTimestamp: str | None = None
    Details: consolidated_alert_details_.ConsolidatedAlertDetails | None = None
    Id: str | None = None
    Notes: str | None = None
    ParentEntity: consolidated_alert_parent_entity_.ConsolidatedAlertParentEntity | None = None
    RaisedTimestamp: str | None = None
    Severity: str | None = None
    Status: str | None = None
    Type: str | None = None
    UpdatedTimestamp: str | None = None

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = consolidated_alert_links_.ConsolidatedAlertLinks.from_dictionary(val)

        val = dictionary.get('active_entity_count', None)
        val_active_entity_count = val

        val = dictionary.get('cause', None)
        val_cause = val

        val = dictionary.get('cleared_entity_count', None)
        val_cleared_entity_count = val

        val = dictionary.get('cleared_timestamp', None)
        val_cleared_timestamp = val

        val = dictionary.get('details', None)
        val_details = consolidated_alert_details_.ConsolidatedAlertDetails.from_dictionary(val)

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('notes', None)
        val_notes = val

        val = dictionary.get('parent_entity', None)
        val_parent_entity = (
            consolidated_alert_parent_entity_.ConsolidatedAlertParentEntity.from_dictionary(val)
        )

        val = dictionary.get('raised_timestamp', None)
        val_raised_timestamp = val

        val = dictionary.get('severity', None)
        val_severity = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('updated_timestamp', None)
        val_updated_timestamp = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_active_entity_count,
            val_cause,
            val_cleared_entity_count,
            val_cleared_timestamp,
            val_details,
            val_id,
            val_notes,
            val_parent_entity,
            val_raised_timestamp,
            val_severity,
            val_status,
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
        return model_instance
