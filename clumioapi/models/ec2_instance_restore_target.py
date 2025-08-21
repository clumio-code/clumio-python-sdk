#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import \
    ec2_restore_ebs_block_device_mapping as ec2_restore_ebs_block_device_mapping_
from clumioapi.models import ec2_restore_network_interface as ec2_restore_network_interface_

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
    _names: dict[str, str] = {
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
        ami_native_id: str | None = None,
        aws_az: str | None = None,
        ebs_block_device_mappings: (
            Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
        ) = None,
        environment_id: str | None = None,
        iam_instance_profile_name: str | None = None,
        key_pair_name: str | None = None,
        network_interfaces: (
            Sequence[ec2_restore_network_interface_.EC2RestoreNetworkInterface] | None
        ) = None,
        should_power_on: bool | None = None,
        subnet_native_id: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        vpc_native_id: str | None = None,
    ) -> None:
        """Constructor for the EC2InstanceRestoreTarget class."""

        # Initialize members of the class
        self.ami_native_id: str | None = ami_native_id
        self.aws_az: str | None = aws_az
        self.ebs_block_device_mappings: (
            Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
        ) = ebs_block_device_mappings
        self.environment_id: str | None = environment_id
        self.iam_instance_profile_name: str | None = iam_instance_profile_name
        self.key_pair_name: str | None = key_pair_name
        self.network_interfaces: (
            Sequence[ec2_restore_network_interface_.EC2RestoreNetworkInterface] | None
        ) = network_interfaces
        self.should_power_on: bool | None = should_power_on
        self.subnet_native_id: str | None = subnet_native_id
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.vpc_native_id: str | None = vpc_native_id

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
        val = dictionary.get('ami_native_id', None)
        val_ami_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('ebs_block_device_mappings', None)

        val_ebs_block_device_mappings = None
        if val:
            val_ebs_block_device_mappings = list()
            for value in val:
                val_ebs_block_device_mappings.append(
                    ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('iam_instance_profile_name', None)
        val_iam_instance_profile_name = val

        val = dictionary.get('key_pair_name', None)
        val_key_pair_name = val

        val = dictionary.get('network_interfaces', None)

        val_network_interfaces = None
        if val:
            val_network_interfaces = list()
            for value in val:
                val_network_interfaces.append(
                    ec2_restore_network_interface_.EC2RestoreNetworkInterface.from_dictionary(value)
                )

        val = dictionary.get('should_power_on', None)
        val_should_power_on = val

        val = dictionary.get('subnet_native_id', None)
        val_subnet_native_id = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('vpc_native_id', None)
        val_vpc_native_id = val

        # Return an object of this model
        return cls(
            val_ami_native_id,
            val_aws_az,
            val_ebs_block_device_mappings,
            val_environment_id,
            val_iam_instance_profile_name,
            val_key_pair_name,
            val_network_interfaces,
            val_should_power_on,
            val_subnet_native_id,
            val_tags,
            val_vpc_native_id,
        )
