#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link as hateoas_link_
from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='OULinks')


class OULinks:
    """Implementation of the 'OULinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        delete_organizational_unit:
            A resource-specific HATEOAS link.
        patch_organizational_unit:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'p_self': '_self',
        'delete_organizational_unit': 'delete-organizational-unit',
        'patch_organizational_unit': 'patch-organizational-unit',
    }

    def __init__(
        self,
        p_self: hateoas_self_link_.HateoasSelfLink,
        delete_organizational_unit: hateoas_link_.HateoasLink,
        patch_organizational_unit: hateoas_link_.HateoasLink,
    ) -> None:
        """Constructor for the OULinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self
        self.delete_organizational_unit: hateoas_link_.HateoasLink = delete_organizational_unit
        self.patch_organizational_unit: hateoas_link_.HateoasLink = patch_organizational_unit

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

        val = dictionary['delete-organizational-unit']
        val_delete_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        val = dictionary['patch-organizational-unit']
        val_patch_organizational_unit = hateoas_link_.HateoasLink.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
            val_delete_organizational_unit,  # type: ignore
            val_patch_organizational_unit,  # type: ignore
        )
