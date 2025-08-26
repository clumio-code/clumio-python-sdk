#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlServiceInstanceProfiles')


class MssqlServiceInstanceProfiles:
    """Implementation of the 'MssqlServiceInstanceProfiles' model.

    Attributes:
        ec2_ssm_instance_profile_arn:
            Policy created for ec2 instance profile role
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {'ec2_ssm_instance_profile_arn': 'ec2_ssm_instance_profile_arn'}

    def __init__(self, ec2_ssm_instance_profile_arn: str | None = None) -> None:
        """Constructor for the MssqlServiceInstanceProfiles class."""

        # Initialize members of the class
        self.ec2_ssm_instance_profile_arn: str | None = ec2_ssm_instance_profile_arn

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

        dictionary = dictionary or {}
        # Extract variables from the dictionary
        val = dictionary.get('ec2_ssm_instance_profile_arn', None)
        val_ec2_ssm_instance_profile_arn = val

        # Return an object of this model
        return cls(
            val_ec2_ssm_instance_profile_arn,
        )
