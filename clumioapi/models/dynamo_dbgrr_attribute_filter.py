#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='DynamoDBGRRAttributeFilter')


class DynamoDBGRRAttributeFilter:
    """Implementation of the 'DynamoDBGRRAttributeFilter' model.

    Attributes:
        condition:
            Filter condition on the DynamoDB attribute.

            +----------------------+-------------------------------------------------------+
            |      Condition       |                         Usage                         |
            +======================+=======================================================+
            | EqualTo              | Compares the filter attribute to be equal to the      |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number, Binary and Boolean.              |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | NotEqualTo           | Compares the filter attribute to not be equal to the  |
            |                      | operand value.                                        |
            |                      | It expects only one operand value. Supported types    |
            |                      | are: String, Number, Binary and Boolean.              |
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
            |                      | are: String, Number, Binary, Boolean and Null.        |
            |                      |                                                       |
            +----------------------+-------------------------------------------------------+
            | NotExists            | Checks the filter attribute to not exist.             |
            |                      | It does not expect any operand value. Supported types |
            |                      | are: String, Number, Binary, Boolean and Null.        |
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
        name:
            DynamoDB attribute name.
        p_type:
            Data-type of the DynamoDB attribute.

            +----------------+
            | Allowed values |
            +================+
            | String         |
            +----------------+
            | Number         |
            +----------------+
            | Binary         |
            +----------------+
            | Boolean        |
            +----------------+
            | Null           |
            +----------------+
        values:
            Values for the attribute filter.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'condition': 'condition',
        'name': 'name',
        'p_type': 'type',
        'values': 'values',
    }

    def __init__(
        self,
        condition: str | None = None,
        name: str | None = None,
        p_type: str | None = None,
        values: Sequence[str] | None = None,
    ) -> None:
        """Constructor for the DynamoDBGRRAttributeFilter class."""

        # Initialize members of the class
        self.condition: str | None = condition
        self.name: str | None = name
        self.p_type: str | None = p_type
        self.values: Sequence[str] | None = values

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
        val = dictionary.get('condition', None)
        val_condition = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('values', None)
        val_values = val

        # Return an object of this model
        return cls(
            val_condition,
            val_name,
            val_p_type,
            val_values,
        )
