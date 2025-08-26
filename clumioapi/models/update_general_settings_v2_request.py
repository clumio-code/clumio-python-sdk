#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ou_grouping_criteria as ou_grouping_criteria_
import requests

T = TypeVar('T', bound='UpdateGeneralSettingsV2Request')


@dataclasses.dataclass
class UpdateGeneralSettingsV2Request:
    """Implementation of the 'UpdateGeneralSettingsV2Request' model.

        Attributes:
            AutoLogoutDuration:
                The length of time before a user is logged out of the clumio system due to inactivity. measured in seconds.
    the valid range is between 600 seconds (10 minutes) and 3600 seconds (60 minutes).
    if not configured, the value defaults to 900 seconds (15 minutes).

            IpAllowlist:
                The designated range of ip addresses that are allowed to access the clumio rest api.
    api requests that originate from outside this list will be blocked.
    the ip address of the server from which this request is being made must be in this list; otherwise, the request will fail.
    set the parameter to individual ip addresses and/or a range of ip addresses in cidr notation.
    for example, ["193.168.1.0/24", "193.172.1.1"].
    if not configured, the value defaults to ["0.0.0.0/0"] meaning all addresses will be allowed.

            OrganizationalUnitDataGroups:
                The grouping criteria for each datasource type.
    these can only be edited for datasource types which do not have any
    organizational units configured.

            PasswordExpirationDuration:
                The length of time a user password is valid before it must be changed. measured in seconds.
    the valid range is between 2592000 seconds (30 days) and 15552000 seconds (180 days).
    if not configured, the value defaults to 7776000 seconds (90 days).

    """

    AutoLogoutDuration: int | None = None
    IpAllowlist: Sequence[str] | None = None
    OrganizationalUnitDataGroups: ou_grouping_criteria_.OUGroupingCriteria | None = None
    PasswordExpirationDuration: int | None = None

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
        return model_instance
