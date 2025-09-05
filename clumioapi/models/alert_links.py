#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='AlertLinks')


class AlertLinks:
    """Implementation of the 'AlertLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        read_consolidated_alert:
            A resource-specific HATEOAS link.
        update_individual_alert:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'read_consolidated_alert': 'read-consolidated-alert',
        'update_individual_alert': 'update-individual-alert',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink | None = None,
        read_consolidated_alert: hateoas_link_.HateoasLink | None = None,
        update_individual_alert: hateoas_link_.HateoasLink | None = None,
    ) -> None:
        """Constructor for the AlertLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink | None = p_self
        self.read_consolidated_alert: hateoas_link_.HateoasLink | None = read_consolidated_alert
        self.update_individual_alert: hateoas_link_.HateoasLink | None = update_individual_alert

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
        val = dictionary.get('_self', None)
        val_p_self = hateoas_self_link_.HateoasSelfLink.from_dictionary(val)

        val = dictionary.get('read-consolidated-alert', None)
        val_read_consolidated_alert = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary.get('update-individual-alert', None)
        val_update_individual_alert = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,
            val_read_consolidated_alert,
            val_update_individual_alert,
        )
