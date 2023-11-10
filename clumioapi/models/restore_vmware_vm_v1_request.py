#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import vm_restore_options
from clumioapi.models import vm_restore_source
from clumioapi.models import vm_restore_target

T = TypeVar('T', bound='RestoreVmwareVmV1Request')


class RestoreVmwareVmV1Request:
    """Implementation of the 'RestoreVmwareVmV1Request' model.

    Attributes:
        options:
            Additional VM restore options.
        source:
            The VM backup to be restored.
        target:
            The configuration of the VM to be restored.
    """

    # Create a mapping from Model property names to API property names
    _names = {'options': 'options', 'source': 'source', 'target': 'target'}

    def __init__(
        self,
        options: vm_restore_options.VMRestoreOptions = None,
        source: vm_restore_source.VMRestoreSource = None,
        target: vm_restore_target.VMRestoreTarget = None,
    ) -> None:
        """Constructor for the RestoreVmwareVmV1Request class."""

        # Initialize members of the class
        self.options: vm_restore_options.VMRestoreOptions = options
        self.source: vm_restore_source.VMRestoreSource = source
        self.target: vm_restore_target.VMRestoreTarget = target

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
        key = 'options'
        options = (
            vm_restore_options.VMRestoreOptions.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'source'
        source = (
            vm_restore_source.VMRestoreSource.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'target'
        target = (
            vm_restore_target.VMRestoreTarget.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(options, source, target)
