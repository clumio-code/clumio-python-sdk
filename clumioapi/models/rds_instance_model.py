#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='RdsInstanceModel')


class RdsInstanceModel:
    """Implementation of the 'RdsInstanceModel' model.

    Attributes:
        p_class:
            The class of the RDS instance at the time of backup. Possible values include
            `db.r5.2xlarge` and `db.t2.small`.
            For a full list of possible values, refer to the Amazon documentation at
            https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.
            html.
        is_publicly_accessible:
            Determines whether the RDS instance had a public IP address in addition to the
            private IP address at the time of backup.
            For more information about the public access option, refer to the Amazon
            documentation at
            https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSIn
            stanceinaVPC.html.
        name:
            The AWS-assigned name of the RDS instance at the time of backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'p_class': 'class',
        'is_publicly_accessible': 'is_publicly_accessible',
        'name': 'name',
    }

    def __init__(
        self, p_class: str = None, is_publicly_accessible: bool = None, name: str = None
    ) -> None:
        """Constructor for the RdsInstanceModel class."""

        # Initialize members of the class
        self.p_class: str = p_class
        self.is_publicly_accessible: bool = is_publicly_accessible
        self.name: str = name

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
        p_class = dictionary.get('class')
        is_publicly_accessible = dictionary.get('is_publicly_accessible')
        name = dictionary.get('name')
        # Return an object of this model
        return cls(p_class, is_publicly_accessible, name)
