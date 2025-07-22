#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import object_filter as object_filter_

T = TypeVar('T', bound='CreateProtectionGroupV1Request')


class CreateProtectionGroupV1Request:
    """Implementation of the 'CreateProtectionGroupV1Request' model.

    Attributes:
        bucket_rule:
            The following table describes the possible conditions for a bucket to be
            automatically added to a protection group.
            Denotes the properties to conditionalize on. For `$eq`, `$not_eq`, `$contains`
            and `$not_contains` a single element is provided: `{'$eq':{'key':'Environment',
            'value':'Prod'}}`. For all other operations, a list is provided:
            `{'$in':[{'key':'Environment','value':'Prod'}, {'key':'Hello',
            'value':'World'}]}`.

            +-------------------+-----------------------------+----------------------------+
            |       Field       |       Rule Condition        |        Description         |
            +===================+=============================+============================+
            | aws_tag           | $eq, $not_eq, $contains,    | Supports filtering by AWS  |
            |                   | $not_contains, $all,        | tag(s) using the following |
            |                   | $not_all, $in, $not_in      | operators. For example,    |
            |                   |                             |                            |
            |                   |                             | {"aws_tag":{"$eq":{"key":" |
            |                   |                             | Environment",              |
            |                   |                             | "value":"Prod"}}}          |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
            | account_native_id | $eq, $in                    |                            |
            |                   |                             | This will be deprecated    |
            |                   |                             | and use                    |
            |                   |                             | aws_account_native_id      |
            |                   |                             | instead.                   |
            |                   |                             | Supports filtering by AWS  |
            |                   |                             | account(s) using the       |
            |                   |                             | following operators. For   |
            |                   |                             | example,                   |
            |                   |                             |                            |
            |                   |                             | {"account_native_id":{"$in |
            |                   |                             | ":["111111111111"]}}       |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
            | aws_region        | $eq, $in                    | Supports filtering by AWS  |
            |                   |                             | region(s) using the        |
            |                   |                             | following operators. For   |
            |                   |                             | example,                   |
            |                   |                             |                            |
            |                   |                             | {"aws_region":{"$eq":"us-  |
            |                   |                             | west-2"}}                  |
            |                   |                             |                            |
            |                   |                             |                            |
            +-------------------+-----------------------------+----------------------------+
        description:
            The user-assigned description of the protection group.
        name:
            The user-assigned name of the protection group.
        object_filter:
            ObjectFilter
            defines which objects will be backed up.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'bucket_rule': 'bucket_rule',
        'description': 'description',
        'name': 'name',
        'object_filter': 'object_filter',
    }

    def __init__(
        self,
        bucket_rule: str,
        description: str,
        name: str,
        object_filter: object_filter_.ObjectFilter,
    ) -> None:
        """Constructor for the CreateProtectionGroupV1Request class."""

        # Initialize members of the class
        self.bucket_rule: str = bucket_rule
        self.description: str = description
        self.name: str = name
        self.object_filter: object_filter_.ObjectFilter = object_filter

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
        val = dictionary['bucket_rule']
        val_bucket_rule = val

        val = dictionary['description']
        val_description = val

        val = dictionary['name']
        val_name = val

        val = dictionary['object_filter']
        val_object_filter = object_filter_.ObjectFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_bucket_rule,  # type: ignore
            val_description,  # type: ignore
            val_name,  # type: ignore
            val_object_filter,  # type: ignore
        )
