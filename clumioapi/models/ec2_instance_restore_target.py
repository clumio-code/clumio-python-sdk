#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import \
    ec2_restore_ebs_block_device_mapping as ec2_restore_ebs_block_device_mapping_
from clumioapi.models import ec2_restore_network_interface as ec2_restore_network_interface_
import requests

T = TypeVar('T', bound='EC2InstanceRestoreTarget')


@dataclasses.dataclass
class EC2InstanceRestoreTarget:
    """Implementation of the 'EC2InstanceRestoreTarget' model.

        The configuration of an EC2 instance to be restored.

        Attributes:
            AmiNativeId:
                The aws-assigned id of the amazon machine image (ami) used to launch the ec2 instance.

            AwsAz:
                The availability zone for the instance. this is determined by the subnet chosen to
    restore the ec2 instance into.

            EbsBlockDeviceMappings:
                Block device mappings for the ebs volumes to restore.

            EnvironmentId:
                The clumio-assigned id of the aws environment to be used as the restore destination.
    use the [get /datasources/aws/environments](#operation/list-aws-environments) endpoint
    to fetch valid values.

            IamInstanceProfileName:
                The name of iam instance profile to launch the instance with.

            KeyPairName:
                The name of ssh keypair to be used.

            NetworkInterfaces:
                The network interfaces to associate with the instance.

            ShouldPowerOn:
                Whether or not to power the instance on at the end of restore. if this is set
    to true, the instance state will be 'running.' if it is set to false, the state
    will be 'stopped.'.

            SubnetNativeId:
                The aws-assigned id of the subnet to launch the instance into.

            Tags:
                The aws tags to be applied to the restored instance.

            VpcNativeId:
                The aws-assigned id of the vpc to launch the instance into.

    """

    AmiNativeId: str | None = None
    AwsAz: str | None = None
    EbsBlockDeviceMappings: (
        Sequence[ec2_restore_ebs_block_device_mapping_.EC2RestoreEbsBlockDeviceMapping] | None
    ) = None
    EnvironmentId: str | None = None
    IamInstanceProfileName: str | None = None
    KeyPairName: str | None = None
    NetworkInterfaces: (
        Sequence[ec2_restore_network_interface_.EC2RestoreNetworkInterface] | None
    ) = None
    ShouldPowerOn: bool | None = None
    SubnetNativeId: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    VpcNativeId: str | None = None

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
        val = dictionary.get('ami_native_id', None)
        val_ami_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('ebs_block_device_mappings', None)

        val_ebs_block_device_mappings = []
        if val:
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

        val_network_interfaces = []
        if val:
            for value in val:
                val_network_interfaces.append(
                    ec2_restore_network_interface_.EC2RestoreNetworkInterface.from_dictionary(value)
                )

        val = dictionary.get('should_power_on', None)
        val_should_power_on = val

        val = dictionary.get('subnet_native_id', None)
        val_subnet_native_id = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
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
