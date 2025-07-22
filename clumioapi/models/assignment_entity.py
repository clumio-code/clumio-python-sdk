#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='AssignmentEntity')


class AssignmentEntity:
    """Implementation of the 'AssignmentEntity' model.

    An entity being assigned or unassigned a policy.

    Attributes:
        p_id:
            A system-generated ID assigned of an entity being assigned or unassigned to a
            policy.
        p_type:

            The type of an entity being associated or disassociated with a policy.
            Valid primary entity types include the following:

            +---------------------+---------------------+
            | Primary Entity Type |       Details       |
            +=====================+=====================+
            | aws_ebs_volume      | AWS EBS volume.     |
            +---------------------+---------------------+
            | aws_ec2_instance    | AWS EC2 instance.   |
            +---------------------+---------------------+
            | aws_rds_cluster     | AWS RDS cluster.    |
            +---------------------+---------------------+
            | aws_rds_instance    | AWS RDS instance.   |
            +---------------------+---------------------+
            | aws_dynamodb_table  | AWS DynamoDB table. |
            +---------------------+---------------------+
            | protection_group    | Protection group.   |
            +---------------------+---------------------+
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'p_id': 'id', 'p_type': 'type'}

    def __init__(self, p_id: str, p_type: str) -> None:
        """Constructor for the AssignmentEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
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
        val = dictionary['id']
        val_p_id = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_p_id,  # type: ignore
            val_p_type,  # type: ignore
        )
