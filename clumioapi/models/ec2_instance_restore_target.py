#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model
from clumioapi.models import ec2_restore_ebs_block_device_mapping
from clumioapi.models import ec2_restore_network_interface

T = TypeVar('T', bound='EC2InstanceRestoreTarget')


class EC2InstanceRestoreTarget:
    """Implementation of the 'EC2InstanceRestoreTarget' model.

    The configuration of an EC2 instance to be restored.

    Attributes:
        ami_native_id:
            The AWS-assigned ID of the Amazon Machine Image (AMI) used to launch the EC2
            instance.
        aws_az:
            The availability zone for the instance. This is determined by the subnet chosen
            to
            restore the EC2 instance into.
        ebs_block_device_mappings:
            Block device mappings for the EBS volumes to restore.
        environment_id:
            The Clumio-assigned ID of the AWS environment to be used as the restore
            destination.
            Use the [GET /datasources/aws/environments](#operation/list-aws-environments)
            endpoint
            to fetch valid values.
        iam_instance_profile_name:
            The name of IAM instance profile to launch the instance with.
        key_pair_name:
            The name of SSH KeyPair to be used.
        network_interfaces:
            The network interfaces to associate with the instance.
        should_power_on:
            Whether or not to power the instance on at the end of restore. If this is set
            to true, the instance state will be 'running.' If it is set to false, the state
            will be 'stopped.'
        subnet_native_id:
            The AWS-assigned ID of the subnet to launch the instance into.
        tags:
            The AWS tags to be applied to the restored instance.
        vpc_native_id:
            The AWS-assigned ID of the vpc to launch the instance into.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'ami_native_id': 'ami_native_id',
        'aws_az': 'aws_az',
        'ebs_block_device_mappings': 'ebs_block_device_mappings',
        'environment_id': 'environment_id',
        'iam_instance_profile_name': 'iam_instance_profile_name',
        'key_pair_name': 'key_pair_name',
        'network_interfaces': 'network_interfaces',
        'should_power_on': 'should_power_on',
        'subnet_native_id': 'subnet_native_id',
        'tags': 'tags',
        'vpc_native_id': 'vpc_native_id',
    }

    def __init__(
        self,
        ami_native_id: str = None,
        aws_az: str = None,
        ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = None,
        environment_id: str = None,
        iam_instance_profile_name: str = None,
        key_pair_name: str = None,
        network_interfaces: Sequence[
            ec2_restore_network_interface.EC2RestoreNetworkInterface
        ] = None,
        should_power_on: bool = None,
        subnet_native_id: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        vpc_native_id: str = None,
    ) -> None:
        """Constructor for the EC2InstanceRestoreTarget class."""

        # Initialize members of the class
        self.ami_native_id: str = ami_native_id
        self.aws_az: str = aws_az
        self.ebs_block_device_mappings: Sequence[
            ec2_restore_ebs_block_device_mapping.EC2RestoreEbsBlockDeviceMapping
        ] = ebs_block_device_mappings
        self.environment_id: str = environment_id
        self.iam_instance_profile_name: str = iam_instance_profile_name
        self.key_pair_name: str = key_pair_name
        self.network_interfaces: Sequence[
            ec2_restore_network_interface.EC2RestoreNetworkInterface
        ] = network_interfaces
        self.should_power_on: bool = should_power_on
        self.subnet_native_id: str = subnet_native_id
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.vpc_native_id: str = vpc_native_id

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
        ami_native_id = dictionary.get('ami_native_id')
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
        iam_instance_profile_name = dictionary.get('iam_instance_profile_name')
        key_pair_name = dictionary.get('key_pair_name')
        network_interfaces = None
        if dictionary.get('network_interfaces'):
            network_interfaces = list()
            for value in dictionary.get('network_interfaces'):
                network_interfaces.append(
                    ec2_restore_network_interface.EC2RestoreNetworkInterface.from_dictionary(value)
                )

        should_power_on = dictionary.get('should_power_on')
        subnet_native_id = dictionary.get('subnet_native_id')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        vpc_native_id = dictionary.get('vpc_native_id')
        # Return an object of this model
        return cls(
            ami_native_id,
            aws_az,
            ebs_block_device_mappings,
            environment_id,
            iam_instance_profile_name,
            key_pair_name,
            network_interfaces,
            should_power_on,
            subnet_native_id,
            tags,
            vpc_native_id,
        )
