#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import ami_model as ami_model_
from clumioapi.models import attached_ebs_volume_full_model as attached_ebs_volume_full_model_
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import ec2_backup_links as ec2_backup_links_
from clumioapi.models import iam_instance_profile_model as iam_instance_profile_model_
from clumioapi.models import \
    instance_store_block_device_mapping as instance_store_block_device_mapping_
from clumioapi.models import network_interface as network_interface_

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
        public_ip_address:
            The public IP v4 address of the instance if one was assigned.
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
    _names: dict[str, str] = {
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
        'public_ip_address': 'public_ip_address',
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
        links: ec2_backup_links_.EC2BackupLinks | None = None,
        account_native_id: str | None = None,
        ami: ami_model_.AmiModel | None = None,
        attached_backup_ebs_volumes: (
            Sequence[attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel] | None
        ) = None,
        aws_az: str | None = None,
        aws_region: str | None = None,
        backup_ami: ami_model_.AmiModel | None = None,
        backup_tier: str | None = None,
        browsing_failed_reason: str | None = None,
        expiration_timestamp: str | None = None,
        iam_instance_profile: iam_instance_profile_model_.IamInstanceProfileModel | None = None,
        p_id: str | None = None,
        instance_id: str | None = None,
        instance_native_id: str | None = None,
        instance_store_block_device_mappings: (
            Sequence[instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping] | None
        ) = None,
        instance_type: str | None = None,
        is_browsable: bool | None = None,
        key_pair_name: str | None = None,
        key_pair_native_id: str | None = None,
        migration_timestamp: str | None = None,
        network_interfaces: Sequence[network_interface_.NetworkInterface] | None = None,
        public_ip_address: str | None = None,
        size: int | None = None,
        start_timestamp: str | None = None,
        subnet_native_id: str | None = None,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None,
        p_type: str | None = None,
        utilized_size_in_bytes: int | None = None,
        vpc_native_id: str | None = None,
    ) -> None:
        """Constructor for the ReadEC2BackupResponse class."""

        # Initialize members of the class
        self.links: ec2_backup_links_.EC2BackupLinks | None = links
        self.account_native_id: str | None = account_native_id
        self.ami: ami_model_.AmiModel | None = ami
        self.attached_backup_ebs_volumes: (
            Sequence[attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel] | None
        ) = attached_backup_ebs_volumes
        self.aws_az: str | None = aws_az
        self.aws_region: str | None = aws_region
        self.backup_ami: ami_model_.AmiModel | None = backup_ami
        self.backup_tier: str | None = backup_tier
        self.browsing_failed_reason: str | None = browsing_failed_reason
        self.expiration_timestamp: str | None = expiration_timestamp
        self.iam_instance_profile: iam_instance_profile_model_.IamInstanceProfileModel | None = (
            iam_instance_profile
        )
        self.p_id: str | None = p_id
        self.instance_id: str | None = instance_id
        self.instance_native_id: str | None = instance_native_id
        self.instance_store_block_device_mappings: (
            Sequence[instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping] | None
        ) = instance_store_block_device_mappings
        self.instance_type: str | None = instance_type
        self.is_browsable: bool | None = is_browsable
        self.key_pair_name: str | None = key_pair_name
        self.key_pair_native_id: str | None = key_pair_native_id
        self.migration_timestamp: str | None = migration_timestamp
        self.network_interfaces: Sequence[network_interface_.NetworkInterface] | None = (
            network_interfaces
        )
        self.public_ip_address: str | None = public_ip_address
        self.size: int | None = size
        self.start_timestamp: str | None = start_timestamp
        self.subnet_native_id: str | None = subnet_native_id
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = tags
        self.p_type: str | None = p_type
        self.utilized_size_in_bytes: int | None = utilized_size_in_bytes
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
        val = dictionary.get('_links', None)
        val_links = ec2_backup_links_.EC2BackupLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('ami', None)
        val_ami = ami_model_.AmiModel.from_dictionary(val)

        val = dictionary.get('attached_backup_ebs_volumes', None)

        val_attached_backup_ebs_volumes = None
        if val:
            val_attached_backup_ebs_volumes = list()
            for value in val:
                val_attached_backup_ebs_volumes.append(
                    attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_ami', None)
        val_backup_ami = ami_model_.AmiModel.from_dictionary(val)

        val = dictionary.get('backup_tier', None)
        val_backup_tier = val

        val = dictionary.get('browsing_failed_reason', None)
        val_browsing_failed_reason = val

        val = dictionary.get('expiration_timestamp', None)
        val_expiration_timestamp = val

        val = dictionary.get('iam_instance_profile', None)
        val_iam_instance_profile = (
            iam_instance_profile_model_.IamInstanceProfileModel.from_dictionary(val)
        )

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('instance_native_id', None)
        val_instance_native_id = val

        val = dictionary.get('instance_store_block_device_mappings', None)

        val_instance_store_block_device_mappings = None
        if val:
            val_instance_store_block_device_mappings = list()
            for value in val:
                val_instance_store_block_device_mappings.append(
                    instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary.get('instance_type', None)
        val_instance_type = val

        val = dictionary.get('is_browsable', None)
        val_is_browsable = val

        val = dictionary.get('key_pair_name', None)
        val_key_pair_name = val

        val = dictionary.get('key_pair_native_id', None)
        val_key_pair_native_id = val

        val = dictionary.get('migration_timestamp', None)
        val_migration_timestamp = val

        val = dictionary.get('network_interfaces', None)

        val_network_interfaces = None
        if val:
            val_network_interfaces = list()
            for value in val:
                val_network_interfaces.append(
                    network_interface_.NetworkInterface.from_dictionary(value)
                )

        val = dictionary.get('public_ip_address', None)
        val_public_ip_address = val

        val = dictionary.get('size', None)
        val_size = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('subnet_native_id', None)
        val_subnet_native_id = val

        val = dictionary.get('tags', None)

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_p_type = val

        val = dictionary.get('utilized_size_in_bytes', None)
        val_utilized_size_in_bytes = val

        val = dictionary.get('vpc_native_id', None)
        val_vpc_native_id = val

        # Return an object of this model
        return cls(
            val_links,
            val_account_native_id,
            val_ami,
            val_attached_backup_ebs_volumes,
            val_aws_az,
            val_aws_region,
            val_backup_ami,
            val_backup_tier,
            val_browsing_failed_reason,
            val_expiration_timestamp,
            val_iam_instance_profile,
            val_p_id,
            val_instance_id,
            val_instance_native_id,
            val_instance_store_block_device_mappings,
            val_instance_type,
            val_is_browsable,
            val_key_pair_name,
            val_key_pair_native_id,
            val_migration_timestamp,
            val_network_interfaces,
            val_public_ip_address,
            val_size,
            val_start_timestamp,
            val_subnet_native_id,
            val_tags,
            val_p_type,
            val_utilized_size_in_bytes,
            val_vpc_native_id,
        )
