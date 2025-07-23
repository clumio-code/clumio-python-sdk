#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamoDBQueryPreviewResult')


class DynamoDBQueryPreviewResult:
    """Implementation of the 'DynamoDBQueryPreviewResult' model.

    If preview was not set to true in the request, then the result of the query will
    beavailable for download asynchronously and this field has a value of `null`.

    Attributes:
        attributes:
            The columns of the previewed query result.
        items:
            The rows of the previewed query result.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'attributes': 'attributes', 'items': 'items'}

    def __init__(
        self, attributes: Sequence[str] | None = None, items: Sequence[Sequence[str]] | None = None
    ) -> None:
        """Constructor for the DynamoDBQueryPreviewResult class."""

        # Initialize members of the class
        self.attributes: Sequence[str] | None = attributes
        self.items: Sequence[Sequence[str]] | None = items

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
        val = dictionary.get('attributes', None)
        val_attributes = val

        val = dictionary.get('items', None)
        val_items = val

        # Return an object of this model
        return cls(
            val_attributes,
            val_items,
        )
