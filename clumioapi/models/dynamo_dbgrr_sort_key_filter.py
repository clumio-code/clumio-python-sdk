#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamoDBGRRSortKeyFilter')


class DynamoDBGRRSortKeyFilter:
    """Implementation of the 'DynamoDBGRRSortKeyFilter' model.

    Sort Key filter of the DynamoDB table.

    Attributes:
        condition:
            Filter condition on the DynamoDB sort key.

            +----------------------+-------------------------------------------------------+
            |      Condition       |                         Usage                         |
            +======================+=======================================================+
            | EqualTo              | Compares the filter attribute to be equal to the      |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | NotEqualTo           | Compares the filter attribute to not be equal to the  |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | LessThanOrEqualTo    | Compares the filter attribute to be less than or      |
            |                      | equal to the operand value.                           |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | LessThan             | Compares the filter attribute to be less than the     |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | GreaterThanOrEqualTo | Compares the filter attribute to be greater than or   |
            |                      | equal to the operand value.                           |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | GreaterThan          | Compares the filter attribute to be greater than the  |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | Between              | Compares the filter attribute to be between the       |
            |                      | operand values.                                       |
            |                      | It expects two operand values. Supported types are:   |
            |                      | String, Number and Binary.                            |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | Exists               | Checks the filter attribute to exist.                 |
            |                      | It does not expect any operand value. Supported types |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | NotExists            | Checks the filter attribute to not exist.             |
            |                      | It does not expect any operand value. Supported types |
            |                      | are: String, Number and Binary.                       |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | Contains             | Checks the filter attribute to contain the operand    |
            |                      | value.                                                |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String and Binary.                               |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | NotContains          | Checks the filter attribute to not contain the        |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String and Binary.                               |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | BeginsWith           | Checks the filter attribute to begin with the operand |
            |                      | value.                                                |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String and Binary.                               |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
        values:
            Values for the attribute filter.
    """

    # Create a mapping from Model property names to API property names
    _names = {'condition': 'condition', 'values': 'values'}

    def __init__(self, condition: str = None, values: Sequence[str] = None) -> None:
        """Constructor for the DynamoDBGRRSortKeyFilter class."""

        # Initialize members of the class
        self.condition: str = condition
        self.values: Sequence[str] = values

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
        condition = dictionary.get('condition')
        values = dictionary.get('values')
        # Return an object of this model
        return cls(condition, values)
