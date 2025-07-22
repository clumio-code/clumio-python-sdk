#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_self_link as hateoas_self_link_

T = TypeVar('T', bound='PreviewProtectionGroupS3AssetSyncLinks')


class PreviewProtectionGroupS3AssetSyncLinks:
    """Implementation of the 'PreviewProtectionGroupS3AssetSyncLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_self': '_self'}

    def __init__(self, p_self: hateoas_self_link_.HateoasSelfLink) -> None:
        """Constructor for the PreviewProtectionGroupS3AssetSyncLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link_.HateoasSelfLink = p_self

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

        # Return an object of this model
        return cls(
            val_p_self,  # type: ignore
        )
