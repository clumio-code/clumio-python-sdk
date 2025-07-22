#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='ConsolidatedAlertParentEntity')


class ConsolidatedAlertParentEntity:
    """Implementation of the 'ConsolidatedAlertParentEntity' model.

    The entity associated with or affected by the alert.

    Attributes:
        p_id:
            A system-generated ID assigned to this entity.
        p_type:
            Type is mostly an asset type or the type of Entity. Some examples are
            "restored_file", "aws_ebs_volume",  etc.
        value:
            A system-generated value assigned to the entity. For example, if the primary
            entity type is "aws_ebs_volume", then the value is the name of the EBS.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_id': 'id', 'p_type': 'type', 'value': 'value'}

    def __init__(self, p_id: str, p_type: str, value: str) -> None:
        """Constructor for the ConsolidatedAlertParentEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.p_type: str = p_type
        self.value: str = value

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
        val = dictionary['id']
        val_p_id = val

        val = dictionary['type']
        val_p_type = val

        val = dictionary['value']
        val_value = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_p_type,  # type: ignore
            val_value,  # type: ignore
        )
