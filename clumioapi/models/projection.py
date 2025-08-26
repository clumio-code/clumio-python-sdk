#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='Projection')


class Projection:
    """Implementation of the 'Projection' model.

    Represents attributes that are copied (projected) from the table into an index.
    These are in addition to theprimary key attributes and index key attributes,
    which are automatically projected.

    Attributes:
        non_key_attributes:
            Represents the non-key attribute names which will be projected into the index.
            For [POST /restores/aws/dynamodb](#operation/restore-aws-dynamodb-table), this
            must be empty if
            'projection_type' is ALL or KEYS_ONLY, and non-empty if 'projection_type' is
            INCLUDE.
        projection_type:
            The set of attributes that are projected into the index. Valid Values: ALL,
            KEYS_ONLY, INCLUDE.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'non_key_attributes': 'non_key_attributes',
        'projection_type': 'projection_type',
    }

    def __init__(
        self, non_key_attributes: Sequence[str] | None = None, projection_type: str | None = None
    ) -> None:
        """Constructor for the Projection class."""

        # Initialize members of the class
        self.non_key_attributes: Sequence[str] | None = non_key_attributes
        self.projection_type: str | None = projection_type

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
        val = dictionary.get('non_key_attributes', None)
        val_non_key_attributes = val

        val = dictionary.get('projection_type', None)
        val_projection_type = val

        # Return an object of this model
        return cls(
            val_non_key_attributes,
            val_projection_type,
        )
