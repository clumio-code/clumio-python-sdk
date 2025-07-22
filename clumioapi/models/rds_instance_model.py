#
# Copyright 2023. Clumio, A Commvault Company.
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
    _names: dict[str, str] = {
        'p_class': 'class',
        'is_publicly_accessible': 'is_publicly_accessible',
        'name': 'name',
    }

    def __init__(self, p_class: str, is_publicly_accessible: bool, name: str) -> None:
        """Constructor for the RdsInstanceModel class."""

        # Initialize members of the class
        self.p_class: str = p_class
        self.is_publicly_accessible: bool = is_publicly_accessible
        self.name: str = name

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
        val = dictionary['class']
        val_p_class = val

        val = dictionary['is_publicly_accessible']
        val_is_publicly_accessible = val

        val = dictionary['name']
        val_name = val

        # Return an object of this model
        return cls(
            val_p_class,  # type: ignore
            val_is_publicly_accessible,  # type: ignore
            val_name,  # type: ignore
        )
