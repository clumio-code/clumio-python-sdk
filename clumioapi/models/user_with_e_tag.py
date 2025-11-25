#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import role_for_organizational_units as role_for_organizational_units_
from clumioapi.models import user_embedded as user_embedded_
from clumioapi.models import user_links as user_links_
import requests

T = TypeVar('T', bound='UserWithETag')


@dataclasses.dataclass
class UserWithETag:
    """Implementation of the 'UserWithETag' model.

    UserWithETag to support etag string to be calculated.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Etag:
            Etag value.

        Links:
            Urls to pages related to the resource.

        AccessControlConfiguration:
            The list of organizational unit ids along with role assigned to the user.

        Email:
            The email address of the clumio user.

        FullName:
            The first and last name of the clumio user. the name appears in the
            user management screen and is used to identify the user.

        Id:
            The clumio-assigned id of the clumio user.

        Inviter:
            The id number of the user who sent the email invitation.

        IsConfirmed:
            Determines whether the user has activated their clumio account.
            if `true`, the user has activated the account.

        IsEnabled:
            Determines whether the user is enabled (in "activated" or "invited" status) in
            clumio.
            if `true`, the user is in "activated" or "invited" status in clumio.
            users in "activated" status can log in to clumio.
            users in "invited" status have been invited to log in to clumio via an email
            invitation and
            the invitation is pending acceptance from the user.
            if `false`, the user has been manually suspended and cannot log in to clumio
            until another clumio user reactivates the account.

        LastActivityTimestamp:
            The timestamp of when the user was last active in the clumio system.
            represented in rfc-3339 format.

        LastPasswordChangeTimestamp:
            The last password change time of the clumio user. represented in rfc-3339
            format.

        OrganizationalUnitCount:
            The number of organizational units accessible to the user.

    """

    Embedded: user_embedded_.UserEmbedded | None = None
    Etag: str | None = None
    Links: user_links_.UserLinks | None = None
    AccessControlConfiguration: (
        Sequence[role_for_organizational_units_.RoleForOrganizationalUnits] | None
    ) = None
    Email: str | None = None
    FullName: str | None = None
    Id: str | None = None
    Inviter: str | None = None
    IsConfirmed: bool | None = None
    IsEnabled: bool | None = None
    LastActivityTimestamp: str | None = None
    LastPasswordChangeTimestamp: str | None = None
    OrganizationalUnitCount: int | None = None

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
        val_embedded = user_embedded_.UserEmbedded.from_dictionary(val)

        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = user_links_.UserLinks.from_dictionary(val)

        val = dictionary.get('access_control_configuration', None)

        val_access_control_configuration = []
        if val:
            for value in val:
                val_access_control_configuration.append(
                    role_for_organizational_units_.RoleForOrganizationalUnits.from_dictionary(value)
                )

        val = dictionary.get('email', None)
        val_email = val

        val = dictionary.get('full_name', None)
        val_full_name = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('inviter', None)
        val_inviter = val

        val = dictionary.get('is_confirmed', None)
        val_is_confirmed = val

        val = dictionary.get('is_enabled', None)
        val_is_enabled = val

        val = dictionary.get('last_activity_timestamp', None)
        val_last_activity_timestamp = val

        val = dictionary.get('last_password_change_timestamp', None)
        val_last_password_change_timestamp = val

        val = dictionary.get('organizational_unit_count', None)
        val_organizational_unit_count = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_etag,
            val_links,
            val_access_control_configuration,
            val_email,
            val_full_name,
            val_id,
            val_inviter,
            val_is_confirmed,
            val_is_enabled,
            val_last_activity_timestamp,
            val_last_password_change_timestamp,
            val_organizational_unit_count,
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
