#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import role_for_organizational_units
from clumioapi.models import user_embedded
from clumioapi.models import user_links

T = TypeVar('T', bound='UserWithETag')


class UserWithETag:
    """Implementation of the 'UserWithETag' model.

    UserWithETag to support etag string to be calculated.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        etag:
            ETag value
        links:
            URLs to pages related to the resource.
        access_control_configuration:
            The list of organizational unit IDs along with role assigned to the user.
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
        'etag': '_etag',
        'links': '_links',
        'access_control_configuration': 'access_control_configuration',
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
        embedded: user_embedded.UserEmbedded = None,
        etag: str = None,
        links: user_links.UserLinks = None,
        access_control_configuration: Sequence[
            role_for_organizational_units.RoleForOrganizationalUnits
        ] = None,
        email: str = None,
        full_name: str = None,
        p_id: str = None,
        inviter: str = None,
        is_confirmed: bool = None,
        is_enabled: bool = None,
        last_activity_timestamp: str = None,
        organizational_unit_count: int = None,
    ) -> None:
        """Constructor for the UserWithETag class."""

        # Initialize members of the class
        self.embedded: user_embedded.UserEmbedded = embedded
        self.etag: str = etag
        self.links: user_links.UserLinks = links
        self.access_control_configuration: Sequence[
            role_for_organizational_units.RoleForOrganizationalUnits
        ] = access_control_configuration
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
            user_embedded.UserEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        etag = dictionary.get('_etag')
        key = '_links'
        links = (
            user_links.UserLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        access_control_configuration = None
        if dictionary.get('access_control_configuration'):
            access_control_configuration = list()
            for value in dictionary.get('access_control_configuration'):
                access_control_configuration.append(
                    role_for_organizational_units.RoleForOrganizationalUnits.from_dictionary(value)
                )

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
            etag,
            links,
            access_control_configuration,
            email,
            full_name,
            p_id,
            inviter,
            is_confirmed,
            is_enabled,
            last_activity_timestamp,
            organizational_unit_count,
        )
