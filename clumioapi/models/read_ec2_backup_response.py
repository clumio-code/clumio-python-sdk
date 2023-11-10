#
# Copyright 2023. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ami_model
from clumioapi.models import attached_ebs_volume_full_model
from clumioapi.models import aws_tag_common_model
from clumioapi.models import ec2_backup_links
from clumioapi.models import iam_instance_profile_model
from clumioapi.models import instance_store_block_device_mapping
from clumioapi.models import network_interface

T = TypeVar('T', bound='ReadEC2BackupResponse')


class ReadEC2BackupResponse:
    """Implementation of the 'ReadEC2BackupResponse' model.

    Attributes:
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the backup.
        ami:
            An Amazon Machine Image is a supported and maintained image provided by AWS
            that provides the information required to launch an instance.
        attached_backup_ebs_volumes:
            The EBS volumes attached to the instance.
        aws_az:
            The availability zone of the instance.
        aws_region:
            The AWS region in which the instance backup resides. For example, `us-west-2`.
        backup_ami:
            An Amazon Machine Image is a supported and maintained image provided by AWS
            that provides the information required to launch an instance.
        backup_tier:
            The tier to which the backup is tagged to.
        browsing_failed_reason:
            The reason that browsing is unavailable for the backup.
            If browse indexing is successful, then this field has a value of `null`.
        expiration_timestamp:
            The timestamp of when this backup expires. Represented in RFC-3339 format.
        iam_instance_profile:
            Denotes an IAM instance profile. An instance profile is a container for an
            IAM role that you can use to pass role information to an EC2 instance when
            the instance starts.
        p_id:
            The Clumio-assigned ID of the instance backup.
        instance_id:
            The Clumio-assigned ID of the EC2 instance associated with the instance backup.
        instance_native_id:
            The AWS-assigned ID of the EC2 instance associated with the instance backup.
        instance_store_block_device_mappings:
            The InstanceStore volumes attached to the instance.
        instance_type:
            The instance type of the original EC2 instance before backup. For example,
            `m5.large`.
        is_browsable:
            Determines whether browsing is available for the backup. If `true`, then
            browsing is available for the backup.
        key_pair_name:
            The name of the key pair associated with this instance. If this instance was not
            launched with an associated key pair, then this field has a value of `null`.
        key_pair_native_id:
            The ID of the key pair associated with this instance. If this instance was not
            launched with an associated key pair, then this field has a value of `null`.
        migration_timestamp:
            The timestamp of when the migration was triggered. This field will be set only
            for
            migration backups. Represented in RFC-3339 format.
        network_interfaces:
            The network interfaces attached to the instance.
        size:
            The size of the instance backup. This is the sum of all the EBS volumes attached
            to the EC2 measured in gigabytes (GB).
        start_timestamp:
            The timestamp of when this backup started. Represented in RFC-3339 format.
        subnet_native_id:
            The AWS-assigned Subnet ID of the EC2 instance.
        tags:
            The instance tags applied to the original EC2 instance before backup.
        p_type:
            The type of the backup.
        utilized_size_in_bytes:
            The total number of bytes written in all the disks of the EC2 instance.
        vpc_native_id:
            The AWS-assigned ID of the VPC associated with the EC2 instance.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'links': '_links',
        'account_native_id': 'account_native_id',
        'ami': 'ami',
        'attached_backup_ebs_volumes': 'attached_backup_ebs_volumes',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'backup_ami': 'backup_ami',
        'backup_tier': 'backup_tier',
        'browsing_failed_reason': 'browsing_failed_reason',
        'expiration_timestamp': 'expiration_timestamp',
        'iam_instance_profile': 'iam_instance_profile',
        'p_id': 'id',
        'instance_id': 'instance_id',
        'instance_native_id': 'instance_native_id',
        'instance_store_block_device_mappings': 'instance_store_block_device_mappings',
        'instance_type': 'instance_type',
        'is_browsable': 'is_browsable',
        'key_pair_name': 'key_pair_name',
        'key_pair_native_id': 'key_pair_native_id',
        'migration_timestamp': 'migration_timestamp',
        'network_interfaces': 'network_interfaces',
        'size': 'size',
        'start_timestamp': 'start_timestamp',
        'subnet_native_id': 'subnet_native_id',
        'tags': 'tags',
        'p_type': 'type',
        'utilized_size_in_bytes': 'utilized_size_in_bytes',
        'vpc_native_id': 'vpc_native_id',
    }

    def __init__(
        self,
        links: ec2_backup_links.EC2BackupLinks = None,
        account_native_id: str = None,
        ami: ami_model.AmiModel = None,
        attached_backup_ebs_volumes: Sequence[
            attached_ebs_volume_full_model.AttachedEBSVolumeFullModel
        ] = None,
        aws_az: str = None,
        aws_region: str = None,
        backup_ami: ami_model.AmiModel = None,
        backup_tier: str = None,
        browsing_failed_reason: str = None,
        expiration_timestamp: str = None,
        iam_instance_profile: iam_instance_profile_model.IamInstanceProfileModel = None,
        p_id: str = None,
        instance_id: str = None,
        instance_native_id: str = None,
        instance_store_block_device_mappings: Sequence[
            instance_store_block_device_mapping.InstanceStoreBlockDeviceMapping
        ] = None,
        instance_type: str = None,
        is_browsable: bool = None,
        key_pair_name: str = None,
        key_pair_native_id: str = None,
        migration_timestamp: str = None,
        network_interfaces: Sequence[network_interface.NetworkInterface] = None,
        size: int = None,
        start_timestamp: str = None,
        subnet_native_id: str = None,
        tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = None,
        p_type: str = None,
        utilized_size_in_bytes: int = None,
        vpc_native_id: str = None,
    ) -> None:
        """Constructor for the ReadEC2BackupResponse class."""

        # Initialize members of the class
        self.links: ec2_backup_links.EC2BackupLinks = links
        self.account_native_id: str = account_native_id
        self.ami: ami_model.AmiModel = ami
        self.attached_backup_ebs_volumes: Sequence[
            attached_ebs_volume_full_model.AttachedEBSVolumeFullModel
        ] = attached_backup_ebs_volumes
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.backup_ami: ami_model.AmiModel = backup_ami
        self.backup_tier: str = backup_tier
        self.browsing_failed_reason: str = browsing_failed_reason
        self.expiration_timestamp: str = expiration_timestamp
        self.iam_instance_profile: iam_instance_profile_model.IamInstanceProfileModel = (
            iam_instance_profile
        )
        self.p_id: str = p_id
        self.instance_id: str = instance_id
        self.instance_native_id: str = instance_native_id
        self.instance_store_block_device_mappings: Sequence[
            instance_store_block_device_mapping.InstanceStoreBlockDeviceMapping
        ] = instance_store_block_device_mappings
        self.instance_type: str = instance_type
        self.is_browsable: bool = is_browsable
        self.key_pair_name: str = key_pair_name
        self.key_pair_native_id: str = key_pair_native_id
        self.migration_timestamp: str = migration_timestamp
        self.network_interfaces: Sequence[network_interface.NetworkInterface] = network_interfaces
        self.size: int = size
        self.start_timestamp: str = start_timestamp
        self.subnet_native_id: str = subnet_native_id
        self.tags: Sequence[aws_tag_common_model.AwsTagCommonModel] = tags
        self.p_type: str = p_type
        self.utilized_size_in_bytes: int = utilized_size_in_bytes
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
        key = '_links'
        links = (
            ec2_backup_links.EC2BackupLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        key = 'ami'
        ami = (
            ami_model.AmiModel.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None
        )

        attached_backup_ebs_volumes = None
        if dictionary.get('attached_backup_ebs_volumes'):
            attached_backup_ebs_volumes = list()
            for value in dictionary.get('attached_backup_ebs_volumes'):
                attached_backup_ebs_volumes.append(
                    attached_ebs_volume_full_model.AttachedEBSVolumeFullModel.from_dictionary(value)
                )

        aws_az = dictionary.get('aws_az')
        aws_region = dictionary.get('aws_region')
        key = 'backup_ami'
        backup_ami = (
            ami_model.AmiModel.from_dictionary(dictionary.get(key)) if dictionary.get(key) else None
        )

        backup_tier = dictionary.get('backup_tier')
        browsing_failed_reason = dictionary.get('browsing_failed_reason')
        expiration_timestamp = dictionary.get('expiration_timestamp')
        key = 'iam_instance_profile'
        iam_instance_profile = (
            iam_instance_profile_model.IamInstanceProfileModel.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        p_id = dictionary.get('id')
        instance_id = dictionary.get('instance_id')
        instance_native_id = dictionary.get('instance_native_id')
        instance_store_block_device_mappings = None
        if dictionary.get('instance_store_block_device_mappings'):
            instance_store_block_device_mappings = list()
            for value in dictionary.get('instance_store_block_device_mappings'):
                instance_store_block_device_mappings.append(
                    instance_store_block_device_mapping.InstanceStoreBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        instance_type = dictionary.get('instance_type')
        is_browsable = dictionary.get('is_browsable')
        key_pair_name = dictionary.get('key_pair_name')
        key_pair_native_id = dictionary.get('key_pair_native_id')
        migration_timestamp = dictionary.get('migration_timestamp')
        network_interfaces = None
        if dictionary.get('network_interfaces'):
            network_interfaces = list()
            for value in dictionary.get('network_interfaces'):
                network_interfaces.append(network_interface.NetworkInterface.from_dictionary(value))

        size = dictionary.get('size')
        start_timestamp = dictionary.get('start_timestamp')
        subnet_native_id = dictionary.get('subnet_native_id')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_common_model.AwsTagCommonModel.from_dictionary(value))

        p_type = dictionary.get('type')
        utilized_size_in_bytes = dictionary.get('utilized_size_in_bytes')
        vpc_native_id = dictionary.get('vpc_native_id')
        # Return an object of this model
        return cls(
            links,
            account_native_id,
            ami,
            attached_backup_ebs_volumes,
            aws_az,
            aws_region,
            backup_ami,
            backup_tier,
            browsing_failed_reason,
            expiration_timestamp,
            iam_instance_profile,
            p_id,
            instance_id,
            instance_native_id,
            instance_store_block_device_mappings,
            instance_type,
            is_browsable,
            key_pair_name,
            key_pair_native_id,
            migration_timestamp,
            network_interfaces,
            size,
            start_timestamp,
            subnet_native_id,
            tags,
            p_type,
            utilized_size_in_bytes,
            vpc_native_id,
        )
