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
    _names = {'attributes': 'attributes', 'items': 'items'}

    def __init__(
        self, attributes: Sequence[str] = None, items: Sequence[Sequence[str]] = None
    ) -> None:
        """Constructor for the DynamoDBQueryPreviewResult class."""

        # Initialize members of the class
        self.attributes: Sequence[str] = attributes
        self.items: Sequence[Sequence[str]] = items

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
        attributes = dictionary.get('attributes')
        items = dictionary.get('items')
        # Return an object of this model
        return cls(attributes, items)
