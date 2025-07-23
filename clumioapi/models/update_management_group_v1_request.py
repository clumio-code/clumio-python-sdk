#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateManagementGroupV1Request')


class UpdateManagementGroupV1Request:
    """Implementation of the 'UpdateManagementGroupV1Request' model.

    Attributes:
        backup_across_subgroups:
            Determines whether backups are allowed to occur across different subgroups or
            cloud connectors.
        name:
            The name of the management group.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'backup_across_subgroups': 'backup_across_subgroups', 'name': 'name'}

    def __init__(
        self, backup_across_subgroups: bool | None = None, name: str | None = None
    ) -> None:
        """Constructor for the UpdateManagementGroupV1Request class."""

        # Initialize members of the class
        self.backup_across_subgroups: bool | None = backup_across_subgroups
        self.name: str | None = name

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
        val = dictionary.get('backup_across_subgroups', None)
        val_backup_across_subgroups = val

        val = dictionary.get('name', None)
        val_name = val

        # Return an object of this model
        return cls(
            val_backup_across_subgroups,
            val_name,
        )
