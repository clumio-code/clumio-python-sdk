#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='ConsolidatedAlertLinks')


class ConsolidatedAlertLinks:
    """Implementation of the 'ConsolidatedAlertLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        update_consolidated_alert:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'update_consolidated_alert': 'update-consolidated-alert',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        update_consolidated_alert: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the ConsolidatedAlertLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.update_consolidated_alert: hateoas_link_.HateoasLink = update_consolidated_alert

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
        val = dictionary['_self']
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary['update-consolidated-alert']
        val_update_consolidated_alert = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_update_consolidated_alert,  # type: ignore
        )
