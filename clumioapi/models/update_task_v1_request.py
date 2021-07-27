#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='UpdateTaskV1Request')


class UpdateTaskV1Request:
    """Implementation of the 'UpdateTaskV1Request' model.

    Attributes:
        status:
            The task status. Set this parameter to `aborting` to abort a task
            that is in queue ("queued") or in progress ("in_progress").
            Tasks with other statuses cannot be aborted.
    """

    # Create a mapping from Model property names to API property names
    _names = {'status': 'status'}

    def __init__(self, status: str = None) -> None:
        """Constructor for the UpdateTaskV1Request class."""

        # Initialize members of the class
        self.status: str = status

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
        status = dictionary.get('status')
        # Return an object of this model
        return cls(status)
