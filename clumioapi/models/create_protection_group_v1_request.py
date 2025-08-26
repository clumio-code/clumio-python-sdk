#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import object_filter as object_filter_
import requests

T = TypeVar('T', bound='CreateProtectionGroupV1Request')


@dataclasses.dataclass
class CreateProtectionGroupV1Request:
    """Implementation of the 'CreateProtectionGroupV1Request' model.

        Attributes:
            BucketRule:
                `{'$in':[{'key':'environment','value':'prod'}, {'key':'hello', 'value':'world'}]}`.

    +-------------------+-----------------------------+----------------------------+
    |       field       |       rule condition        |        description         |
    +===================+=============================+============================+
    | aws_tag           | $eq, $not_eq, $contains,    | supports filtering by aws  |
    |                   | $not_contains, $all,        | tag(s) using the following |
    |                   | $not_all, $in, $not_in      | operators. for example,    |
    |                   |                             |                            |
    |                   |                             | {"aws_tag":{"$eq":{"key":" |
    |                   |                             | environment",              |
    |                   |                             | "value":"prod"}}}          |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    | account_native_id | $eq, $in                    |                            |
    |                   |                             | this will be deprecated    |
    |                   |                             | and use                    |
    |                   |                             | aws_account_native_id      |
    |                   |                             | instead.                   |
    |                   |                             | supports filtering by aws  |
    |                   |                             | account(s) using the       |
    |                   |                             | following operators. for   |
    |                   |                             | example,                   |
    |                   |                             |                            |
    |                   |                             | {"account_native_id":{"$in |
    |                   |                             | ":["111111111111"]}}       |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    | aws_region        | $eq, $in                    | supports filtering by aws  |
    |                   |                             | region(s) using the        |
    |                   |                             | following operators. for   |
    |                   |                             | example,                   |
    |                   |                             |                            |
    |                   |                             | {"aws_region":{"$eq":"us-  |
    |                   |                             | west-2"}}                  |
    |                   |                             |                            |
    |                   |                             |                            |
    +-------------------+-----------------------------+----------------------------+
    .

            Description:
                The user-assigned description of the protection group.

            Name:
                The user-assigned name of the protection group.

            ObjectFilter:
                Objectfilter
    defines which objects will be backed up.

    """

    BucketRule: str | None = None
    Description: str | None = None
    Name: str | None = None
    ObjectFilter: object_filter_.ObjectFilter | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x if v is not None}
        )

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T:
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
        val = dictionary.get('bucket_rule', None)
        val_bucket_rule = val

        val = dictionary.get('description', None)
        val_description = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('object_filter', None)
        val_object_filter = object_filter_.ObjectFilter.from_dictionary(val)

        # Return an object of this model
        return cls(
            val_bucket_rule,
            val_description,
            val_name,
            val_object_filter,
        )

    @classmethod
    def from_response(
        cls: type[T],
        response: requests.Response,
    ) -> T:
        """Creates an instance of this model from a response object.

        Args:
            response: The response object from which the model is to be created.

        Returns:
            object: An instance of this structure class.
        """
        model_instance = cls.from_dictionary(response.json())
        return model_instance
