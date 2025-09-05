#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='EBSRestoreSource')


class EBSRestoreSource:
    """Implementation of the 'EBSRestoreSource' model.

    The EBS volume backup to be restored.

    Attributes:
        backup_id:
            The Clumio-assigned ID of the EBS volume backup to be restored. Use the [GET
            /backups/aws/ebs-volumes](#operation/list-aws-ebs-volumes) endpoint to fetch
            valid values.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'backup_id': 'backup_id'}

    def __init__(self, backup_id: str | None = None) -> None:
        """Constructor for the EBSRestoreSource class."""

        # Initialize members of the class
        self.backup_id: str | None = backup_id

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
        val = dictionary.get('backup_id', None)
        val_backup_id = val

        # Return an object of this model
        return cls(
            val_backup_id,
        )
