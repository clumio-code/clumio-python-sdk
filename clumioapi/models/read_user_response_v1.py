#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import user_embedded_v1 as user_embedded_v1_
from clumioapi.models import user_links as user_links_

T = TypeVar('T', bound='ReadUserResponseV1')


class ReadUserResponseV1:
    """Implementation of the 'ReadUserResponseV1' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        assigned_organizational_unit_ids:
            The list of organizational unit IDs assigned to the user.
            This attribute will be available when reading a single user and not when listing
            users.
        assigned_role:
            Assigned Role for the user.
        email:
            The email address of the Clumio user.
        full_name:
            The first and last name of the Clumio user. The name appears in the
            User Management screen and is used to identify the user.
        p_id:
            The Clumio-assigned ID of the Clumio user.
        inviter:
            The ID number of the user who sent the email invitation.
        is_confirmed:
            Determines whether the user has activated their Clumio account.
            If `true`, the user has activated the account.
        is_enabled:
            Determines whether the user is enabled (in "Activated" or "Invited" status) in
            Clumio.
            If `true`, the user is in "Activated" or "Invited" status in Clumio.
            Users in "Activated" status can log in to Clumio.
            Users in "Invited" status have been invited to log in to Clumio via an email
            invitation and
            the invitation is pending acceptance from the user.
            If `false`, the user has been manually suspended and cannot log in to Clumio
            until another Clumio user reactivates the account.
        last_activity_timestamp:
            The timestamp of when the user was last active in the Clumio system.
            Represented in RFC-3339 format.
        organizational_unit_count:
            The number of organizational units accessible to the user.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'assigned_organizational_unit_ids': 'assigned_organizational_unit_ids',
        'assigned_role': 'assigned_role',
        'email': 'email',
        'full_name': 'full_name',
        'p_id': 'id',
        'inviter': 'inviter',
        'is_confirmed': 'is_confirmed',
        'is_enabled': 'is_enabled',
        'last_activity_timestamp': 'last_activity_timestamp',
        'organizational_unit_count': 'organizational_unit_count',
    }

    def __init__(
        self,
        embedded: user_embedded_v1_.UserEmbeddedV1 | None = None,
        links: user_links_.UserLinks | None = None,
        assigned_organizational_unit_ids: Sequence[str] | None = None,
        assigned_role: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        p_id: str | None = None,
        inviter: str | None = None,
        is_confirmed: bool | None = None,
        is_enabled: bool | None = None,
        last_activity_timestamp: str | None = None,
        organizational_unit_count: int | None = None,
    ) -> None:
        """Constructor for the ReadUserResponseV1 class."""

        # Initialize members of the class
        self.embedded: user_embedded_v1_.UserEmbeddedV1 | None = embedded
        self.links: user_links_.UserLinks | None = links
        self.assigned_organizational_unit_ids: Sequence[str] | None = (
            assigned_organizational_unit_ids
        )
        self.assigned_role: str | None = assigned_role
        self.email: str | None = email
        self.full_name: str | None = full_name
        self.p_id: str | None = p_id
        self.inviter: str | None = inviter
        self.is_confirmed: bool | None = is_confirmed
        self.is_enabled: bool | None = is_enabled
        self.last_activity_timestamp: str | None = last_activity_timestamp
        self.organizational_unit_count: int | None = organizational_unit_count

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
        val_embedded = user_embedded_v1_.UserEmbeddedV1.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = user_links_.UserLinks.from_dictionary(val)

        val = dictionary.get('assigned_organizational_unit_ids', None)
        val_assigned_organizational_unit_ids = val

        val = dictionary.get('assigned_role', None)
        val_assigned_role = val

        val = dictionary.get('email', None)
        val_email = val

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('inviter', None)
        val_inviter = val

        val = dictionary.get('is_confirmed', None)
        val_is_confirmed = val

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        val = dictionary.get('last_activity_timestamp', None)
        val_last_activity_timestamp = val

        val = dictionary.get('organizational_unit_count', None)
        val_organizational_unit_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_assigned_organizational_unit_ids,
            val_assigned_role,
            val_email,
            val_full_name,
            val_p_id,
            val_inviter,
            val_is_confirmed,
            val_is_enabled,
            val_last_activity_timestamp,
            val_organizational_unit_count,
        )
