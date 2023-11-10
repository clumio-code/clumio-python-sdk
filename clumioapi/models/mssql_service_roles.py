#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

T = TypeVar('T', bound='MssqlServiceRoles')


class MssqlServiceRoles:
    """Implementation of the 'MssqlServiceRoles' model.

    Attributes:
        ec2_instance_profile_role_arn:
            Role assumable by ec2 service.
        ec2_ssm_instance_profile_arn:
            Instance created for ec2 instance profile role
        ssm_notification_role_arn:
            Role assumable by ssm service.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'ec2_instance_profile_role_arn': 'ec2_instance_profile_role_arn',
        'ec2_ssm_instance_profile_arn': 'ec2_ssm_instance_profile_arn',
        'ssm_notification_role_arn': 'ssm_notification_role_arn',
    }

    def __init__(
        self,
        ec2_instance_profile_role_arn: str = None,
        ec2_ssm_instance_profile_arn: str = None,
        ssm_notification_role_arn: str = None,
    ) -> None:
        """Constructor for the MssqlServiceRoles class."""

        # Initialize members of the class
        self.ec2_instance_profile_role_arn: str = ec2_instance_profile_role_arn
        self.ec2_ssm_instance_profile_arn: str = ec2_ssm_instance_profile_arn
        self.ssm_notification_role_arn: str = ssm_notification_role_arn

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
        ec2_instance_profile_role_arn = dictionary.get('ec2_instance_profile_role_arn')
        ec2_ssm_instance_profile_arn = dictionary.get('ec2_ssm_instance_profile_arn')
        ssm_notification_role_arn = dictionary.get('ssm_notification_role_arn')
        # Return an object of this model
        return cls(
            ec2_instance_profile_role_arn, ec2_ssm_instance_profile_arn, ssm_notification_role_arn
        )
