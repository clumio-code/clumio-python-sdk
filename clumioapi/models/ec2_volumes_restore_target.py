#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ec2_restore_ebs_block_device_mapping

T = TypeVar('T', bound='EC2VolumesRestoreTarget')


class EC2VolumesRestoreTarget:
    """Implementation of the 'EC2VolumesRestoreTarget' model.

    The target configuration for the volumes to be restored.

    Attributes:
        aws_az:
            The availability zone for restoring the volumes unattached. Either this or
            target_instance_native_id needs to be specified.
        ebs_block_device_mappings:
            Block device mappings chosen for the EBS volumes being restored.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint
            to fetch valid values.
        target_instance_native_id:
            The aws native ID of the EC2 instance to be used to attach the restored volumes.
            If not present, then aws_az need to be specified.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'aws_az': 'aws_az',
        'ebs_block_device_mappings': 'ebs_block_device_mappings',
        'environment_id': 'environment_id',
        'target_instance_native_id': 'target_instance_native_id',
    }

    def __init__(
        self,
        aws_az: str = None,
        ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = None,
        environment_id: str = None,
        target_instance_native_id: str = None,
    ) -> None:
        """Constructor for the EC2VolumesRestoreTarget class."""

        # Initialize members of the class
        self.aws_az: str = aws_az
        self.ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = ebs_block_device_mappings
        self.environment_id: str = environment_id
        self.target_instance_native_id: str = target_instance_native_id

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
        aws_az = dictionary.get('aws_az')
        ebs_block_device_mappings = None
        if dictionary.get('ebs_block_device_mappings'):
            ebs_block_device_mappings = list()
            for value in dictionary.get('ebs_block_device_mappings'):
                ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        environment_id = dictionary.get('environment_id')
        target_instance_native_id = dictionary.get('target_instance_native_id')
        # Return an object of this model
        return cls(aws_az, ebs_block_device_mappings, environment_id, target_instance_native_id)
