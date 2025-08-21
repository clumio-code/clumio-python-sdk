#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import \
    auto_user_provisioning_rule_list_embedded as auto_user_provisioning_rule_list_embedded_
from clumioapi.models import \
    auto_user_provisioning_rule_list_links as auto_user_provisioning_rule_list_links_

T = TypeVar('T', bound='ListAutoUserProvisioningRulesResponse')


class ListAutoUserProvisioningRulesResponse:
    """Implementation of the 'ListAutoUserProvisioningRulesResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        current_count:
            The number of items listed on the current page.
        limit:
            The maximum number of items displayed per page in the response.
        start:
            The page token used to get this response.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'current_count': 'current_count',
        'limit': 'limit',
        'start': 'start',
    }

    def __init__(
        self,
        embedded: (
            auto_user_provisioning_rule_list_embedded_.AutoUserProvisioningRuleListEmbedded | None
        ) = None,
        links: (
            auto_user_provisioning_rule_list_links_.AutoUserProvisioningRuleListLinks | None
        ) = None,
        current_count: int | None = None,
        limit: int | None = None,
        start: str | None = None,
    ) -> None:
        """Constructor for the ListAutoUserProvisioningRulesResponse class."""

        # Initialize members of the class
        self.embedded: (
            auto_user_provisioning_rule_list_embedded_.AutoUserProvisioningRuleListEmbedded | None
        ) = embedded
        self.links: (
            auto_user_provisioning_rule_list_links_.AutoUserProvisioningRuleListLinks | None
        ) = links
        self.current_count: int | None = current_count
        self.limit: int | None = limit
        self.start: str | None = start

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
        val_embedded = auto_user_provisioning_rule_list_embedded_.AutoUserProvisioningRuleListEmbedded.from_dictionary(
            val
        )

        val = dictionary.get('_links', None)
        val_links = auto_user_provisioning_rule_list_links_.AutoUserProvisioningRuleListLinks.from_dictionary(
            val
        )

        val = dictionary.get('current_count', None)
        val_current_count = val

        val = dictionary.get('limit', None)
        val_limit = val

        val = dictionary.get('start', None)
        val_start = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_current_count,
            val_limit,
            val_start,
        )
