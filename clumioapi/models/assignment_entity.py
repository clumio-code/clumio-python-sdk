#
# Copyright 2023. Clumio, Inc.
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
    _names = {'p_id': 'id', 'p_type': 'type'}

    def __init__(self, p_id: str = None, p_type: str = None) -> None:
        """Constructor for the AssignmentEntity class."""

        # Initialize members of the class
        self.p_id: str = p_id
        self.p_type: str = p_type

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
        p_id = dictionary.get('id')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(p_id, p_type)
