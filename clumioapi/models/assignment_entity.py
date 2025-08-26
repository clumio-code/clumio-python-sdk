#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
import requests

T = TypeVar('T', bound='AssignmentEntity')


@dataclasses.dataclass
class AssignmentEntity:
    """Implementation of the 'AssignmentEntity' model.

        An entity being assigned or unassigned a policy.

        Attributes:
            Id:
                A system-generated id assigned of an entity being assigned or unassigned to a policy.

            Type:

    the type of an entity being associated or disassociated with a policy.
    valid primary entity types include the following:

    +---------------------+---------------------+
    | primary entity type |       details       |
    +=====================+=====================+
    | aws_ebs_volume      | aws ebs volume.     |
    +---------------------+---------------------+
    | aws_ec2_instance    | aws ec2 instance.   |
    +---------------------+---------------------+
    | aws_rds_cluster     | aws rds cluster.    |
    +---------------------+---------------------+
    | aws_rds_instance    | aws rds instance.   |
    +---------------------+---------------------+
    | aws_dynamodb_table  | aws dynamodb table. |
    +---------------------+---------------------+
    | protection_group    | protection group.   |
    +---------------------+---------------------+
    .

    """

    Id: str | None = None
    Type: str | None = None

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
        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('type', None)
        val_type = val

        # Return an object of this model
        return cls(
            val_id,
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
