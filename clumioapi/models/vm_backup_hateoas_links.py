#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import hateoas_link
from clumioapi.models import hateoas_self_link

T = TypeVar('T', bound='VMBackupHateoasLinks')


class VMBackupHateoasLinks:
    """Implementation of the 'VMBackupHateoasLinks' model.

    URLs to pages related to the resource.

    Attributes:
        p_self:
            The HATEOAS link to this resource.
        restore_vmware_vm:
            A resource-specific HATEOAS link.
    """

    # Create a mapping from Model property names to API property names
    _names = {'p_self': '_self', 'restore_vmware_vm': 'restore-vmware-vm'}

    def __init__(
        self,
        p_self: hateoas_self_link.HateoasSelfLink = None,
        restore_vmware_vm: hateoas_link.HateoasLink = None,
    ) -> None:
        """Constructor for the VMBackupHateoasLinks class."""

        # Initialize members of the class
        self.p_self: hateoas_self_link.HateoasSelfLink = p_self
        self.restore_vmware_vm: hateoas_link.HateoasLink = restore_vmware_vm

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
        key = '_self'
        p_self = (
            hateoas_self_link.HateoasSelfLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'restore-vmware-vm'
        restore_vmware_vm = (
            hateoas_link.HateoasLink.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(p_self, restore_vmware_vm)
