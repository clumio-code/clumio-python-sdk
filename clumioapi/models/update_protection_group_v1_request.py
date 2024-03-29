#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object_filter

T = TypeVar('T', bound='UpdateProtectionGroupV1Request')


class UpdateProtectionGroupV1Request:
    """Implementation of the 'UpdateProtectionGroupV1Request' model.

    Attributes:
        bucket_rule:
            The following table describes the possible conditions for a bucket to be
            automatically added to a protection group.

            +---------+----------------+---------------------------------------------------+
            |  Field  | Rule Condition |                    Description                    |
            +=========+================+===================================================+
            | aws_tag | $eq            | Denotes the AWS tag(s) to conditionalize on       |
            |         |                |                                                   |
            |         |                | {"aws_tag":{"$eq":{"key":"Environment",           |
            |         |                | "value":"Prod"}}}                                 |
            |         |                |                                                   |
            |         |                |                                                   |
            +---------+----------------+---------------------------------------------------+
        description:
            The user-assigned description of the protection group.
        name:
            The user-assigned name of the protection group.
        object_filter:
            ObjectFilter
            defines which objects will be backed up.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'bucket_rule': 'bucket_rule',
        'description': 'description',
        'name': 'name',
        'object_filter': 'object_filter',
    }

    def __init__(
        self,
        bucket_rule: str = None,
        description: str = None,
        name: str = None,
        object_filter: object_filter.ObjectFilter = None,
    ) -> None:
        """Constructor for the UpdateProtectionGroupV1Request class."""

        # Initialize members of the class
        self.bucket_rule: str = bucket_rule
        self.description: str = description
        self.name: str = name
        self.object_filter: object_filter.ObjectFilter = object_filter

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
        bucket_rule = dictionary.get('bucket_rule')
        description = dictionary.get('description')
        name = dictionary.get('name')
        key = 'object_filter'
        p_object_filter = (
            object_filter.ObjectFilter.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        # Return an object of this model
        return cls(bucket_rule, description, name, p_object_filter)
