#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='CreateS3InstantAccessEndpointResponseEmbedded')


class CreateS3InstantAccessEndpointResponseEmbedded:
    """Implementation of the 'CreateS3InstantAccessEndpointResponseEmbedded' model.

    Embedded responses related to the resource.

    Attributes:
        read_task:
            Embeds the associated task of a resource in the response if requested using the
            `embed` query parameter.
    """

    # Create a mapping from Model property names to API property names
    _names = {'read_task': 'read-task'}

    def __init__(self, read_task: object = None) -> None:
        """Constructor for the CreateS3InstantAccessEndpointResponseEmbedded class."""

        # Initialize members of the class
        self.read_task: object = read_task

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
        read_task = dictionary.get('read-task')
        # Return an object of this model
        return cls(read_task)
