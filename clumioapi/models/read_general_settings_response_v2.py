#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import eg_grouping_criteria as eg_grouping_criteria_
from clumioapi.models import general_settings_links as general_settings_links_

T = TypeVar('T', bound='ReadGeneralSettingsResponseV2')


class ReadGeneralSettingsResponseV2:
    """Implementation of the 'ReadGeneralSettingsResponseV2' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        auto_logout_duration:
            The length of time before a user is logged out of the Clumio system due to
            inactivity. Measured in seconds.
            The valid range is between 600 seconds (10 minutes) and 3600 seconds (60
            minutes).
            If not configured, the value defaults to 900 seconds (15 minutes).
        ip_allowlist:
            The designated range of IP addresses that are allowed to access the Clumio REST
            API.
            API requests that originate from outside this list will be blocked.
            The IP address of the server from which this request is being made must be in
            this list; otherwise, the request will fail.
            Set the parameter to individual IP addresses and/or a range of IP addresses in
            CIDR notation.
            For example, ["193.168.1.0/24", "193.172.1.1"].
            If not configured, the value defaults to ["0.0.0.0/0"] meaning all addresses
            will be allowed.
        organizational_unit_data_groups:
            Deprecated: This struct is deprecated and will be removed in the future
            it is being kept for backward compatibility of settings public API
        password_expiration_duration:
            The length of time a user password is valid before it must be changed. Measured
            in seconds.
            The valid range is between 2592000 seconds (30 days) and 15552000 seconds (180
            days).
            If not configured, the value defaults to 7776000 seconds (90 days).
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'links': '_links',
        'auto_logout_duration': 'auto_logout_duration',
        'ip_allowlist': 'ip_allowlist',
        'organizational_unit_data_groups': 'organizational_unit_data_groups',
        'password_expiration_duration': 'password_expiration_duration',
    }

    def __init__(
        self,
        links: general_settings_links_.GeneralSettingsLinks | None = None,
        auto_logout_duration: int | None = None,
        ip_allowlist: Sequence[str] | None = None,
        organizational_unit_data_groups: eg_grouping_criteria_.EgGroupingCriteria | None = None,
        password_expiration_duration: int | None = None,
    ) -> None:
        """Constructor for the ReadGeneralSettingsResponseV2 class."""

        # Initialize members of the class
        self.links: general_settings_links_.GeneralSettingsLinks | None = links
        self.auto_logout_duration: int | None = auto_logout_duration
        self.ip_allowlist: Sequence[str] | None = ip_allowlist
        self.organizational_unit_data_groups: eg_grouping_criteria_.EgGroupingCriteria | None = (
            organizational_unit_data_groups
        )
        self.password_expiration_duration: int | None = password_expiration_duration

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
        val = dictionary.get('_links', None)
        val_links = general_settings_links_.GeneralSettingsLinks.from_dictionary(val)

        val = dictionary.get('auto_logout_duration', None)
        val_auto_logout_duration = val

        val = dictionary.get('ip_allowlist', None)
        val_ip_allowlist = val

        val = dictionary.get('organizational_unit_data_groups', None)
        val_organizational_unit_data_groups = (
            eg_grouping_criteria_.EgGroupingCriteria.from_dictionary(val)
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
