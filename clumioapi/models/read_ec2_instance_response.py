#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, overload, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ec2_instance_embedded as ec2_instance_embedded_
from clumioapi.models import ec2_instance_links as ec2_instance_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_
import requests

T = TypeVar('T', bound='ReadEc2InstanceResponse')


@dataclasses.dataclass
class ReadEc2InstanceResponse:
    """Implementation of the 'ReadEc2InstanceResponse' model.

    Attributes:
        Embedded:
            Embedded responses related to the resource.

        Links:
            Urls to pages related to the resource.

        AccountNativeId:
            The aws-assigned id of the account associated with the ec2 instance.

        AwsAz:
            The aws availability zone in which the ec2 instance resides. for example,
            `us-west-2a`.

        AwsRegion:
            Determines whether the ec2 instance has been deleted. if `true`, the instance
            has
            been deleted.

        BackupStatusInfo:
            The backup status information applied to this resource.

        DeletionTimestamp:
            The timestamp of when the instance was deleted. represented in rfc-3339 format.
            if this instance has not been deleted, then this field has a value of `null`.

        DirectAssignmentPolicyId:
            The clumio-assigned id of the policy directly assigned to the entity.

        EnaSupport:
            Enasupport indicates whether the elastic network adapter (ena) is enabled for
            the
            instance.

        EnvironmentId:
            The clumio-assigned id of the aws environment associated with the ec2 instance.

        HasDirectAssignment:
            Determines whether the table has a direct assignment.

        Id:
            The clumio-assigned id of the ec2 instance.

        InstanceNativeId:
            The aws-assigned id of the ec2 instance.

        IsDeleted:
            Determines whether the ec2 instance has been deleted. if `true`, the instance
            has
            been deleted.

        IsSupported:
            Determines whether the ec2 instance is supported for backups.

        LastBackupTimestamp:
            The timestamp of the most recent backup of the ec2 instance. represented in
            rfc-3339 format. if the instance has never been backed up, then this field has a
            value of `null`.

        LastSnapshotTimestamp:
            The timestamp of the most recent snapshot of the ec2 instance taken as part of
            the
            ec2 snapshot manager. represented in rfc-3339 format. if the instance has never
            been backed up, then this field has a value of `null`.

        Name:
            The aws-assigned name of the ec2 instance.

        OrganizationalUnitId:
            The clumio-assigned id of the organizational unit associated with the ec2
            instance.

        ProtectionInfo:
            The protection policy applied to this resource. if the resource is not
            protected, then this field has a value of `null`.

        ProtectionStatus:
            The protection status of the ec2 instance. possible values include "protected",
            "unprotected", and "unsupported". if the ec2 instance does not support backups,
            then this field has a value of `unsupported`. if the instance has been deleted,
            then this field has a value of `null`.

        State:
            Pending, running,
            terminated, stopped, stopping, shutting-down, rebooting.

        SubnetId:
            The aws subnet id of the ec2 instance.

        Tags:
            The aws tags applied to the ec2 instance.

        Type:
            Https://docs.aws.amazon.com/awsec2/latest/userguide/instance-types.html.

        UnsupportedReason:
            The reason why protection is not available. if the volume is supported,
            then this field has a value of `null`.

        VpcId:
            Aws-assigned id of the vpc associated with the ec2 instance.

    """

    Embedded: ec2_instance_embedded_.Ec2InstanceEmbedded | None = None
    Links: ec2_instance_links_.Ec2InstanceLinks | None = None
    AccountNativeId: str | None = None
    AwsAz: str | None = None
    AwsRegion: str | None = None
    BackupStatusInfo: backup_status_info_.BackupStatusInfo | None = None
    DeletionTimestamp: str | None = None
    DirectAssignmentPolicyId: str | None = None
    EnaSupport: bool | None = None
    EnvironmentId: str | None = None
    HasDirectAssignment: bool | None = None
    Id: str | None = None
    InstanceNativeId: str | None = None
    IsDeleted: bool | None = None
    IsSupported: bool | None = None
    LastBackupTimestamp: str | None = None
    LastSnapshotTimestamp: str | None = None
    Name: str | None = None
    OrganizationalUnitId: str | None = None
    ProtectionInfo: protection_info_with_rule_.ProtectionInfoWithRule | None = None
    ProtectionStatus: str | None = None
    State: str | None = None
    SubnetId: str | None = None
    Tags: Sequence[aws_tag_model_.AwsTagModel] | None = None
    Type: str | None = None
    UnsupportedReason: str | None = None
    VpcId: str | None = None
    raw_response: Optional[requests.Response] = None

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
        val = dictionary.get('_embedded', None)
        val_embedded = ec2_instance_embedded_.Ec2InstanceEmbedded.from_dictionary(val)

        val = dictionary.get('_links', None)
        val_links = ec2_instance_links_.Ec2InstanceLinks.from_dictionary(val)

        val = dictionary.get('account_native_id', None)
        val_account_native_id = val

        val = dictionary.get('aws_az', None)
        val_aws_az = val

        val = dictionary.get('aws_region', None)
        val_aws_region = val

        val = dictionary.get('backup_status_info', None)
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary.get('deletion_timestamp', None)
        val_deletion_timestamp = val

        val = dictionary.get('direct_assignment_policy_id', None)
        val_direct_assignment_policy_id = val

        val = dictionary.get('ena_support', None)
        val_ena_support = val

        val = dictionary.get('environment_id', None)
        val_environment_id = val

        val = dictionary.get('has_direct_assignment', None)
        val_has_direct_assignment = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('instance_native_id', None)
        val_instance_native_id = val

        val = dictionary.get('is_deleted', None)
        val_is_deleted = val

        val = dictionary.get('is_supported', None)
        val_is_supported = val

        val = dictionary.get('last_backup_timestamp', None)
        val_last_backup_timestamp = val

        val = dictionary.get('last_snapshot_timestamp', None)
        val_last_snapshot_timestamp = val

        val = dictionary.get('name', None)
        val_name = val

        val = dictionary.get('organizational_unit_id', None)
        val_organizational_unit_id = val

        val = dictionary.get('protection_info', None)
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary.get('protection_status', None)
        val_protection_status = val

        val = dictionary.get('state', None)
        val_state = val

        val = dictionary.get('subnet_id', None)
        val_subnet_id = val

        val = dictionary.get('tags', None)

        val_tags = []
        if val:
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary.get('type', None)
        val_type = val

        val = dictionary.get('unsupported_reason', None)
        val_unsupported_reason = val

        val = dictionary.get('vpc_id', None)
        val_vpc_id = val

        # Return an object of this model
        return cls(
            val_embedded,
            val_links,
            val_account_native_id,
            val_aws_az,
            val_aws_region,
            val_backup_status_info,
            val_deletion_timestamp,
            val_direct_assignment_policy_id,
            val_ena_support,
            val_environment_id,
            val_has_direct_assignment,
            val_id,
            val_instance_native_id,
            val_is_deleted,
            val_is_supported,
            val_last_backup_timestamp,
            val_last_snapshot_timestamp,
            val_name,
            val_organizational_unit_id,
            val_protection_info,
            val_protection_status,
            val_state,
            val_subnet_id,
            val_tags,
            val_type,
            val_unsupported_reason,
            val_vpc_id,
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
        model_instance.raw_response = response
        return model_instance
