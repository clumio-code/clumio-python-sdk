#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import user_embedded_v1
from clumioapi.models import user_links

T = TypeVar('T', bound='EditProfileResponseV1')


class EditProfileResponseV1:
    """Implementation of the 'EditProfileResponseV1' model.

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
            The first and last name of the Clumio user. The name appears in the User
            Management screen and is used to identify the user.
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
            invitation and the invitation
            is pending acceptance from the user.
            If `false`, the user has been manually suspended and cannot log in to Clumio
            until another Clumio user reactivates the account.
        last_activity_timestamp:
            The timestamp of when the user was last active in the Clumio system. Represented
            in RFC-3339 format.
        organizational_unit_count:
            The number of organizational units accessible to the user.
    """

    # Create a mapping from Model property names to API property names
    _names = {
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
        embedded: user_embedded_v1.UserEmbeddedV1 = None,
        links: user_links.UserLinks = None,
        assigned_organizational_unit_ids: Sequence[str] = None,
        assigned_role: str = None,
        email: str = None,
        full_name: str = None,
        p_id: str = None,
        inviter: str = None,
        is_confirmed: bool = None,
        is_enabled: bool = None,
        last_activity_timestamp: str = None,
        organizational_unit_count: int = None,
    ) -> None:
        """Constructor for the EditProfileResponseV1 class."""

        # Initialize members of the class
        self.embedded: user_embedded_v1.UserEmbeddedV1 = embedded
        self.links: user_links.UserLinks = links
        self.assigned_organizational_unit_ids: Sequence[str] = assigned_organizational_unit_ids
        self.assigned_role: str = assigned_role
        self.email: str = email
        self.full_name: str = full_name
        self.p_id: str = p_id
        self.inviter: str = inviter
        self.is_confirmed: bool = is_confirmed
        self.is_enabled: bool = is_enabled
        self.last_activity_timestamp: str = last_activity_timestamp
        self.organizational_unit_count: int = organizational_unit_count

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
            user_embedded_v1.UserEmbeddedV1.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            user_links.UserLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        assigned_organizational_unit_ids = dictionary.get('assigned_organizational_unit_ids')
        assigned_role = dictionary.get('assigned_role')
        email = dictionary.get('email')
        full_name = dictionary.get('full_name')
        p_id = dictionary.get('id')
        inviter = dictionary.get('inviter')
        is_confirmed = dictionary.get('is_confirmed')
        is_enabled = dictionary.get('is_enabled')
        last_activity_timestamp = dictionary.get('last_activity_timestamp')
        organizational_unit_count = dictionary.get('organizational_unit_count')
        # Return an object of this model
        return cls(
            embedded,
            links,
            assigned_organizational_unit_ids,
            assigned_role,
            email,
            full_name,
            p_id,
            inviter,
            is_confirmed,
            is_enabled,
            last_activity_timestamp,
            organizational_unit_count,
        )
