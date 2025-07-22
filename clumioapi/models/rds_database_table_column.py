#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RDSDatabaseTableColumn')


class RDSDatabaseTableColumn:
    """Implementation of the 'RDSDatabaseTableColumn' model.

    RDSDatabaseTableColumn denotes the model for rds database column

    Attributes:
        name:
            The name of the column.
        p_type:
            The Hive data type of the column. Possible values include `int`, `bigint`,
            `string`, and `boolean`.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'name': 'name', 'p_type': 'type'}

    def __init__(self, name: str, p_type: str) -> None:
        """Constructor for the RDSDatabaseTableColumn class."""

        # Initialize members of the class
        self.name: str = name
        self.p_type: str = p_type

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

        # Extract variables from the dictionary
        val = dictionary['name']
        val_name = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_name,  # type: ignore
            val_p_type,  # type: ignore
        )
