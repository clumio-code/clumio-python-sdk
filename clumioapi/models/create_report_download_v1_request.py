#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='CreateReportDownloadV1Request')

TypeValues = [
    'activity',
    'audit',
    'consumption',
]


@dataclasses.dataclass
class CreateReportDownloadV1Request:
    """Implementation of the 'CreateReportDownloadV1Request' model.

    Attributes:
        FileName:
            The name of the report. field cannot be empty.

        Filter:
            "{"status" |
            |                      |                  |             | :{"$in":["success"]} |
            |                      |                  |             | }"                   |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+
            | primary_entity.id    | $in              | any         | the system-generated |
            |                      |                  |             | ids of the primary   |
            |                      |                  |             | entities affected by |
            |                      |                  |             | the activity.        |
            |                      |                  |             | for example,         |
            |                      |                  |             |                      |
            |                      |                  |             | filter={"primary_ent |
            |                      |                  |             | ity.id":{"$in":["9c2 |
            |                      |                  |             | 934fc-ff4d-11e9-     |
            |                      |                  |             | 8e11-                |
            |                      |                  |             | 76706df7fe01"]}}     |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+
            | primary_entity.type  | $eq              | any         | the type of primary  |
            |                      |                  |             | entities affected by |
            |                      |                  |             | the activity.        |
            |                      |                  |             | examples of primary  |
            |                      |                  |             | entity types include |
            |                      |                  |             | "aws_ebs_volume",    |
            |                      |                  |             | "aws_ec2_instance",  |
            |                      |                  |             | "microsoft365_mailbo |
            |                      |                  |             | x". for example,     |
            |                      |                  |             |                      |
            |                      |                  |             | filter={"primary_ent |
            |                      |                  |             | ity.type":{"$in":["a |
            |                      |                  |             | ws_ebs_volume"]}}    |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+
            | primary_entity.value | $in              | any         | the value or name    |
            |                      |                  |             | associated with the  |
            |                      |                  |             | primary entities     |
            |                      |                  |             | affected by          |
            |                      |                  |             | the compliance       |
            |                      |                  |             | event. for example,  |
            |                      |                  |             | the primary entity   |
            |                      |                  |             | value associated     |
            |                      |                  |             | with                 |
            |                      |                  |             | primary entity type  |
            |                      |                  |             | "aws_ebs_volume" is  |
            |                      |                  |             | "vol-                |
            |                      |                  |             | 0a5f2e52d6decd664"   |
            |                      |                  |             | representing         |
            |                      |                  |             | the name of the ebs  |
            |                      |                  |             | volume. the filter   |
            |                      |                  |             | supports substring   |
            |                      |                  |             | search for all       |
            |                      |                  |             | elements in the      |
            |                      |                  |             | array for example,   |
            |                      |                  |             |                      |
            |                      |                  |             | filter={"primary_ent |
            |                      |                  |             | ity.value":{"$in":[" |
            |                      |                  |             | vol-0a"]}}           |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+
            | parent_entity.type   | $in              | any         |  the types of the    |
            |                      |                  |             | parent entities      |
            |                      |                  |             | which are associated |
            |                      |                  |             | with the primary     |
            |                      |                  |             | entity affected by   |
            |                      |                  |             | the activity.        |
            |                      |                  |             | examples of the      |
            |                      |                  |             | parent entity types  |
            |                      |                  |             | include              |
            |                      |                  |             | "aws_environment",   |
            |                      |                  |             | "microsoft365_domain |
            |                      |                  |             | ". for example,      |
            |                      |                  |             |                      |
            |                      |                  |             | filter={"parent_enti |
            |                      |                  |             | ty.type":{"$in":["aw |
            |                      |                  |             | s_environment"]}}    |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+
            | parent_entity.id     | $in              | any         |                      |
            |                      |                  |             | the value or name    |
            |                      |                  |             | associated with the  |
            |                      |                  |             | parent entities      |
            |                      |                  |             | affected by          |
            |                      |                  |             | the compliance       |
            |                      |                  |             | event. for example,  |
            |                      |                  |             | the parent entity    |
            |                      |                  |             | value associated     |
            |                      |                  |             | with                 |
            |                      |                  |             | primary entity type  |
            |                      |                  |             | "aws_ebs_volume" is  |
            |                      |                  |             | "891106093485/us-    |
            |                      |                  |             | west-2" representing |
            |                      |                  |             | the name of the aws  |
            |                      |                  |             | account region. for  |
            |                      |                  |             | example,             |
            |                      |                  |             |                      |
            |                      |                  |             | filter={"parent_enti |
            |                      |                  |             | ty.id":{"$in":["9c29 |
            |                      |                  |             | 34fc-ff4d-11e9-8e11- |
            |                      |                  |             | 76706df7fe01"]}}     |
            |                      |                  |             |                      |
            |                      |                  |             |                      |
            +----------------------+------------------+-------------+----------------------+

            for more information about filtering, refer to the
            filtering section of this guide.

        Type:
            The report type. examples of report types include, "activity", "audit", and
            "consumption".

    """

    FileName: str | None = None
    Filter: str | None = None

    Type: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('file_name', None)
        val_file_name = val

        val = dictionary.get('filter', None)
        val_filter = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_file_name,
            val_filter,
            val_type,
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
