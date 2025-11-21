#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import ami_model as ami_model_
from clumioapi.models import attached_ebs_volume_full_model as attached_ebs_volume_full_model_
from clumioapi.models import aws_tag_common_model as aws_tag_common_model_
from clumioapi.models import ec2_backup_links as ec2_backup_links_
from clumioapi.models import iam_instance_profile_model as iam_instance_profile_model_
from clumioapi.models import \
    instance_store_block_device_mapping as instance_store_block_device_mapping_
from clumioapi.models import network_interface as network_interface_
import requests

T = TypeVar('T', bound='EC2Backup')


@dataclasses.dataclass
class EC2Backup:
    """Implementation of the 'EC2Backup' model.

    Attributes:
        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the backup.

        Ami:
            An amazon machine image is a supported and maintained image provided by aws
            that provides the information required to launch an instance.

        AttachedBackupEbsVolumes:
            The ebs volumes attached to the instance.

        AwsAz:
            The availability zone of the instance.

        AwsRegion:
            The aws region in which the instance backup resides. for example, `us-west-2`.

        BackupAmi:
            An amazon machine image is a supported and maintained image provided by aws
            that provides the information required to launch an instance.

        BackupTier:
            The tier to which the backup is tagged to.

        BrowsingFailedReason:
            The reason that browsing is unavailable for the backup.
            if browse indexing is successful, then this field has a value of `null`.

        ExpirationTimestamp:
            The timestamp of when this backup expires. represented in rfc-3339 format.

        IamInstanceProfile:
            Denotes an iam instance profile. an instance profile is a container for an
            iam role that you can use to pass role information to an ec2 instance when
            the instance starts.

        Id:
            The clumio-assigned id of the instance backup.

        InstanceId:
            The clumio-assigned id of the ec2 instance associated with the instance backup.

        InstanceNativeId:
            The aws-assigned id of the ec2 instance associated with the instance backup.

        InstanceStoreBlockDeviceMappings:
            The instancestore volumes attached to the instance.

        InstanceType:
            The instance type of the original ec2 instance before backup. for example,
            `m5.large`.

        IsBrowsable:
            Determines whether browsing is available for the backup. if `true`, then
            browsing is available for the backup.

        KeyPairName:
            The name of the key pair associated with this instance. if this instance was not
            launched with an associated key pair, then this field has a value of `null`.

        KeyPairNativeId:
            The id of the key pair associated with this instance. if this instance was not
            launched with an associated key pair, then this field has a value of `null`.

        MigrationTimestamp:
            The timestamp of when the migration was triggered. this field will be set only
            for
            migration backups. represented in rfc-3339 format.

        NetworkInterfaces:
            The network interfaces attached to the instance.

        PublicIpAddress:
            The public ip v4 address of the instance if one was assigned.

        Size:
            The size of the instance backup. this is the sum of all the ebs volumes attached
            to the ec2 measured in gigabytes (gb).

        StartTimestamp:
            The timestamp of when this backup started. represented in rfc-3339 format.

        SubnetNativeId:
            The aws-assigned subnet id of the ec2 instance.

        Tags:
            The instance tags applied to the original ec2 instance before backup.

        Type:
            The type of the backup.

        UtilizedSizeInBytes:
            The total number of bytes written in all the disks of the ec2 instance.

        VpcNativeId:
            The aws-assigned id of the vpc associated with the ec2 instance.

    """

    Links: ec2_backup_links_.EC2BackupLinks | None = None
    AccountNativeId: str | None = None
    Ami: ami_model_.AmiModel | None = None
    AttachedBackupEbsVolumes: (
        Sequence[attached_ebs_volume_full_model_.AttachedEBSVolumeFullModel] | None
    ) = None
    AwsAz: str | None = None
    AwsRegion: str | None = None
    BackupAmi: ami_model_.AmiModel | None = None
    BackupTier: str | None = None
    BrowsingFailedReason: str | None = None
    ExpirationTimestamp: str | None = None
    IamInstanceProfile: iam_instance_profile_model_.IamInstanceProfileModel | None = None
    Id: str | None = None
    InstanceId: str | None = None
    InstanceNativeId: str | None = None
    InstanceStoreBlockDeviceMappings: (
        Sequence[instance_store_block_device_mapping_.InstanceStoreBlockDeviceMapping] | None
    ) = None
    InstanceType: str | None = None
    IsBrowsable: bool | None = None
    KeyPairName: str | None = None
    KeyPairNativeId: str | None = None
    MigrationTimestamp: str | None = None
    NetworkInterfaces: Sequence[network_interface_.NetworkInterface] | None = None
    PublicIpAddress: str | None = None
    Size: int | None = None
    StartTimestamp: str | None = None
    SubnetNativeId: str | None = None
    Tags: Sequence[aws_tag_common_model_.AwsTagCommonModel] | None = None
    Type: str | None = None
    UtilizedSizeInBytes: int | None = None
    VpcNativeId: str | None = None

    def dict(self) -> Dict[str, Any]:
        """Returns the dictionary representation of the model."""
        return dataclasses.asdict(
            self, dict_factory=lambda x: {camel_to_snake(k): v for (k, v) in x}
        )

    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Mapping[str, Any],
    ) -> T: ...
    @overload
    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: None = None,
    ) -> None: ...

    @classmethod
    def from_dictionary(
        cls: type[T],
        dictionary: Optional[Mapping[str, Any]] = None,
    ) -> T | None:
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
        val = dictionary.get('_links', None)
        val_links = ec2_backup_links_.EC2BackupLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('ami', None)
        val_ami = ami_model_.AmiModel.from_dictionary(val)

        val = dictionary.get('attached_backup_ebs_volumes', None)

        val_attached_backup_ebs_volumes = []
        if val:
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
        val_id = val

        val = dictionary.get('instance_id', None)
        val_instance_id = val

        val = dictionary.get('instance_native_id', None)
        val_instance_native_id = val

        val = dictionary.get('instance_store_block_device_mappings', None)

        val_instance_store_block_device_mappings = []
        if val:
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

        val_network_interfaces = []
        if val:
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

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_common_model_.AwsTagCommonModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

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
            val_id,
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
            val_type,
            val_utilized_size_in_bytes,
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
