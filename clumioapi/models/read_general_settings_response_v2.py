#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import general_settings_links as general_settings_links_
from clumioapi.models import ou_grouping_criteria as ou_grouping_criteria_
import requests

T = TypeVar('T', bound='ReadGeneralSettingsResponseV2')


@dataclasses.dataclass
class ReadGeneralSettingsResponseV2:
    """Implementation of the 'ReadGeneralSettingsResponseV2' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        AutoLogoutDuration:
            The length of time before a user is logged out of the clumio system due to
            inactivity. measured in seconds.
            the valid range is between 600 seconds (10 minutes) and 3600 seconds (60
            minutes).
            if not configured, the value defaults to 900 seconds (15 minutes).

        IpAllowlist:
            The designated range of ip addresses that are allowed to access the clumio rest
            api.
            api requests that originate from outside this list will be blocked.
            the ip address of the server from which this request is being made must be in
            this list; otherwise, the request will fail.
            set the parameter to individual ip addresses and/or a range of ip addresses in
            cidr notation.
            for example, ["193.168.1.0/24", "193.172.1.1"].
            if not configured, the value defaults to ["0.0.0.0/0"] meaning all addresses
            will be allowed.

        OrganizationalUnitDataGroups:
            This struct is deprecated and will be removed in the future.
            it is being kept for backward compatibility.

        PasswordExpirationDuration:
            The length of time a user password is valid before it must be changed. measured
            in seconds.
            the valid range is between 2592000 seconds (30 days) and 15552000 seconds (180
            days).
            if not configured, the value defaults to 7776000 seconds (90 days).

    """

    Links: general_settings_links_.GeneralSettingsLinks | None = None
    AutoLogoutDuration: int | None = None
    IpAllowlist: Sequence[str] | None = None
    OrganizationalUnitDataGroups: ou_grouping_criteria_.OUGroupingCriteria | None = None
    PasswordExpirationDuration: int | None = None
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
        val = dictionary.get('_links', None)
        val_links = general_settings_links_.GeneralSettingsLinks.from_dictionary(val)

        val = dictionary.get('auto_logout_duration', None)
        val_auto_logout_duration = val

        val = dictionary.get('ip_allowlist', None)
        val_ip_allowlist = val

        val = dictionary.get('organizational_unit_data_groups', None)
        val_organizational_unit_data_groups = (
            ou_grouping_criteria_.OUGroupingCriteria.from_dictionary(val)
        )

        val = dictionary.get('password_expiration_duration', None)
        val_password_expiration_duration = val

        # Return an object of this model
        return cls(
            val_links,
            val_auto_logout_duration,
            val_ip_allowlist,
            val_organizational_unit_data_groups,
            val_password_expiration_duration,
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
