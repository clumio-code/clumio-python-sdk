#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ou_grouping_criteria as ou_grouping_criteria_

T = TypeVar('T', bound='UpdateGeneralSettingsV2Request')


class UpdateGeneralSettingsV2Request:
    """Implementation of the 'UpdateGeneralSettingsV2Request' model.

    Attributes:
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
            The grouping criteria for each datasource type.
            These can only be edited for datasource types which do not have any
            organizational units configured.
        password_expiration_duration:
            The length of time a user password is valid before it must be changed. Measured
            in seconds.
            The valid range is between 2592000 seconds (30 days) and 15552000 seconds (180
            days).
            If not configured, the value defaults to 7776000 seconds (90 days).
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'auto_logout_duration': 'auto_logout_duration',
        'ip_allowlist': 'ip_allowlist',
        'organizational_unit_data_groups': 'organizational_unit_data_groups',
        'password_expiration_duration': 'password_expiration_duration',
    }

    def __init__(
        self,
        auto_logout_duration: int,
        ip_allowlist: Sequence[str],
        organizational_unit_data_groups: ou_grouping_criteria_.OUGroupingCriteria,
        password_expiration_duration: int,
    ) -> None:
        """Constructor for the UpdateGeneralSettingsV2Request class."""

        # Initialize members of the class
        self.auto_logout_duration: int = auto_logout_duration
        self.ip_allowlist: Sequence[str] = ip_allowlist
        self.organizational_unit_data_groups: ou_grouping_criteria_.OUGroupingCriteria = (
            organizational_unit_data_groups
        )
        self.password_expiration_duration: int = password_expiration_duration

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

        # Extract variables from the dictionary
        val = dictionary['auto_logout_duration']
        val_auto_logout_duration = val

        val = dictionary['ip_allowlist']
        val_ip_allowlist = val

        val = dictionary['organizational_unit_data_groups']
        val_organizational_unit_data_groups = (
            ou_grouping_criteria_.OUGroupingCriteria.from_dictionary(val)
        )

        val = dictionary['password_expiration_duration']
        val_password_expiration_duration = val

        # Return an object of this model
        return cls(
            val_auto_logout_duration,  # type: ignore
            val_ip_allowlist,  # type: ignore
            val_organizational_unit_data_groups,  # type: ignore
            val_password_expiration_duration,  # type: ignore
        )
