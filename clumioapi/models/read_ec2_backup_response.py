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
        links: ec2_backup_links_.EC2BackupLinks,
        account_native_id: str,
        ami: ami_model_.AmiModel,
        attached_backup_ebs_volumes: Sequence[
            attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel
        ],
        aws_az: str,
        aws_region: str,
        backup_ami: ami_model_.AmiModel,
        backup_tier: str,
        browsing_failed_reason: str,
        expiration_timestamp: str,
        iam_instance_profile: iam_instance_profile_model_.IamInstanceProfileModel,
        p_id: str,
        instance_id: str,
        instance_native_id: str,
        instance_store_block_device_mappings: Sequence[
            instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping
        ],
        instance_type: str,
        is_browsable: bool,
        key_pair_name: str,
        key_pair_native_id: str,
        migration_timestamp: str,
        network_interfaces: Sequence[network_interface_.NetworkInterface],
        public_ip_address: str,
        size: int,
        start_timestamp: str,
        subnet_native_id: str,
        tags: Sequence[aws_tag_common_model_.AwsTagCommonModel],
        p_type: str,
        utilized_size_in_bytes: int,
        vpc_native_id: str,
    ) -> None:
        """Constructor for the ReadEC2BackupResponse class."""

        # Initialize members of the class
        self.links: ec2_backup_links_.EC2BackupLinks = links
        self.account_native_id: str = account_native_id
        self.ami: ami_model_.AmiModel = ami
        self.attached_backup_ebs_volumes: Sequence[
            attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel
        ] = attached_backup_ebs_volumes
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.backup_ami: ami_model_.AmiModel = backup_ami
        self.backup_tier: str = backup_tier
        self.browsing_failed_reason: str = browsing_failed_reason
        self.expiration_timestamp: str = expiration_timestamp
        self.iam_instance_profile: iam_instance_profile_model_.IamInstanceProfileModel = (
            iam_instance_profile
        )
        self.p_id: str = p_id
        self.instance_id: str = instance_id
        self.instance_native_id: str = instance_native_id
        self.instance_store_block_device_mappings: Sequence[
            instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping
        ] = instance_store_block_device_mappings
        self.instance_type: str = instance_type
        self.is_browsable: bool = is_browsable
        self.key_pair_name: str = key_pair_name
        self.key_pair_native_id: str = key_pair_native_id
        self.migration_timestamp: str = migration_timestamp
        self.network_interfaces: Sequence[network_interface_.NetworkInterface] = network_interfaces
        self.public_ip_address: str = public_ip_address
        self.size: int = size
        self.start_timestamp: str = start_timestamp
        self.subnet_native_id: str = subnet_native_id
        self.tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] = tags
        self.p_type: str = p_type
        self.utilized_size_in_bytes: int = utilized_size_in_bytes
        self.vpc_native_id: str = vpc_native_id

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
        val = dictionary['_links']
        val_links = ec2_backup_links_.EC2BackupLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['ami']
        val_ami = ami_model_.AmiModel.from_dictionary(val)

        val = dictionary['attached_backup_ebs_volumes']

        val_attached_backup_ebs_volumes = None
        if val:
            val_attached_backup_ebs_volumes = list()
            for value in val:
                val_attached_backup_ebs_volumes.append(
                    attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel.from_dictionary(
                        value
                    )
                )

        val = dictionary['aws_az']
        val_aws_az = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_ami']
        val_backup_ami = ami_model_.AmiModel.from_dictionary(val)

        val = dictionary['backup_tier']
        val_backup_tier = val

        val = dictionary['browsing_failed_reason']
        val_browsing_failed_reason = val

        val = dictionary['expiration_timestamp']
        val_expiration_timestamp = val

        val = dictionary['iam_instance_profile']
        val_iam_instance_profile = (
            iam_instance_profile_model_.IamInstanceProfileModel.from_dictionary(val)
        )

        val = dictionary['id']
        val_p_id = val

        val = dictionary['instance_id']
        val_instance_id = val

        val = dictionary['instance_native_id']
        val_instance_native_id = val

        val = dictionary['instance_store_block_device_mappings']

        val_instance_store_block_device_mappings = None
        if val:
            val_instance_store_block_device_mappings = list()
            for value in val:
                val_instance_store_block_device_mappings.append(
                    instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping.from_dictionary(
                        value
                    )
                )

        val = dictionary['instance_type']
        val_instance_type = val

        val = dictionary['is_browsable']
        val_is_browsable = val

        val = dictionary['key_pair_name']
        val_key_pair_name = val

        val = dictionary['key_pair_native_id']
        val_key_pair_native_id = val

        val = dictionary['migration_timestamp']
        val_migration_timestamp = val

        val = dictionary['network_interfaces']

        val_network_interfaces = None
        if val:
            val_network_interfaces = list()
            for value in val:
                val_network_interfaces.append(
                    network_interface_.NetworkInterface.from_dictionary(value)
                )

        val = dictionary['public_ip_address']
        val_public_ip_address = val

        val = dictionary['size']
        val_size = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['subnet_native_id']
        val_subnet_native_id = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary['type']
        val_p_type = val

        val = dictionary['utilized_size_in_bytes']
        val_utilized_size_in_bytes = val

        val = dictionary['vpc_native_id']
        val_vpc_native_id = val

        # Return an object of this model
        return cls(
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_ami,  # type: ignore
            val_attached_backup_ebs_volumes,  # type: ignore
            val_aws_az,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_ami,  # type: ignore
            val_backup_tier,  # type: ignore
            val_browsing_failed_reason,  # type: ignore
            val_expiration_timestamp,  # type: ignore
            val_iam_instance_profile,  # type: ignore
            val_p_id,  # type: ignore
            val_instance_id,  # type: ignore
            val_instance_native_id,  # type: ignore
            val_instance_store_block_device_mappings,  # type: ignore
            val_instance_type,  # type: ignore
            val_is_browsable,  # type: ignore
            val_key_pair_name,  # type: ignore
            val_key_pair_native_id,  # type: ignore
            val_migration_timestamp,  # type: ignore
            val_network_interfaces,  # type: ignore
            val_public_ip_address,  # type: ignore
            val_size,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_subnet_native_id,  # type: ignore
            val_tags,  # type: ignore
            val_p_type,  # type: ignore
            val_utilized_size_in_bytes,  # type: ignore
            val_vpc_native_id,  # type: ignore
        )
