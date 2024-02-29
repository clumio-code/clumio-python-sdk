#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import v_mware_v_center_network_with_e_tag

T = TypeVar('T', bound='VMwareVCenterNetworkListEmbedded')


class VMwareVCenterNetworkListEmbedded:
    """Implementation of the 'VMwareVCenterNetworkListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A collection of requested items.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(
        self,
        items: Sequence[v_mware_v_center_network_with_e_tag.VMwareVCenterNetworkWithETag] = None,
    ) -> None:
        """Constructor for the VMwareVCenterNetworkListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[v_mware_v_center_network_with_e_tag.VMwareVCenterNetworkWithETag] = (
            items
        )

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
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
        items = None
        if dictionary.get('items'):
            items = list()
            for value in dictionary.get('items'):
                items.append(
                    v_mware_v_center_network_with_e_tag.VMwareVCenterNetworkWithETag.from_dictionary(
                        value
                    )
                )

        # Return an object of this model
        return cls(items)
