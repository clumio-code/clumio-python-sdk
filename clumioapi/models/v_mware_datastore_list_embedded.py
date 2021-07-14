#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import v_mware_datastore_with_e_tag

T = TypeVar('T', bound='VMwareDatastoreListEmbedded')


class VMwareDatastoreListEmbedded:
    """Implementation of the 'VMwareDatastoreListEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        items:
            A list of VMware datastores.
    """

    # Create a mapping from Model property names to API property names
    _names = {'items': 'items'}

    def __init__(
        self, items: Sequence[v_mware_datastore_with_e_tag.VMwareDatastoreWithETag] = None
    ) -> None:
        """Constructor for the VMwareDatastoreListEmbedded class."""

        # Initialize members of the class
        self.items: Sequence[v_mware_datastore_with_e_tag.VMwareDatastoreWithETag] = items

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
                    v_mware_datastore_with_e_tag.VMwareDatastoreWithETag.from_dictionary(value)
                )

        # Return an object of this model
        return cls(items)
