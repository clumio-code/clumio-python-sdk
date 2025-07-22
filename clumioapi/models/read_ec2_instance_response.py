#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model as aws_tag_model_
from clumioapi.models import backup_status_info as backup_status_info_
from clumioapi.models import ec2_instance_embedded as ec2_instance_embedded_
from clumioapi.models import ec2_instance_links as ec2_instance_links_
from clumioapi.models import protection_info_with_rule as protection_info_with_rule_

T = TypeVar('T', bound='ReadEc2InstanceResponse')


class ReadEc2InstanceResponse:
    """Implementation of the 'ReadEc2InstanceResponse' model.

    Attributes:
        embedded:
            Embedded responses related to the resource.
        links:
            URLs to pages related to the resource.
        account_native_id:
            The AWS-assigned ID of the account associated with the EC2 instance.
        aws_az:
            The AWS availability zone in which the EC2 instance resides. For example,
            `us-west-2a`.
        aws_region:
            Determines whether the EC2 instance has been deleted. If `true`, the instance
            has
            been deleted.
        backup_status_info:
            The backup status information applied to this resource.
        deletion_timestamp:
            The timestamp of when the instance was deleted. Represented in RFC-3339 format.
            If this instance has not been deleted, then this field has a value of `null`.
        direct_assignment_policy_id:
            The Clumio-assigned ID of the policy directly assigned to the entity.
        ena_support:
            EnaSupport indicates whether the Elastic Network Adapter (ENA) is enabled for
            the
            instance.
        environment_id:
            The Clumio-assigned ID of the AWS environment associated with the EC2 instance.
        has_direct_assignment:
            Determines whether the table has a direct assignment.
        p_id:
            The Clumio-assigned ID of the EC2 instance.
        instance_native_id:
            The AWS-assigned ID of the EC2 instance.
        is_deleted:
            Determines whether the EC2 instance has been deleted. If `true`, the instance
            has
            been deleted.
        is_supported:
            Determines whether the EC2 instance is supported for backups.
        last_backup_timestamp:
            The timestamp of the most recent backup of the EC2 instance. Represented in
            RFC-3339 format. If the instance has never been backed up, then this field has a
            value of `null`.
        last_snapshot_timestamp:
            The timestamp of the most recent snapshot of the EC2 instance taken as part of
            the
            EC2 Snapshot Manager. Represented in RFC-3339 format. If the instance has never
            been backed up, then this field has a value of `null`.
        name:
            The AWS-assigned name of the EC2 instance.
        organizational_unit_id:
            The Clumio-assigned ID of the organizational unit associated with the EC2
            instance.
        protection_info:
            The protection policy applied to this resource. If the resource is not
            protected, then this field has a value of `null`.
        protection_status:
            The protection status of the EC2 instance. Possible values include "protected",
            "unprotected", and "unsupported". If the EC2 instance does not support backups,
            then this field has a value of `unsupported`. If the instance has been deleted,
            then this field has a value of `null`.
        state:
            The state of the EC2 instance. Possible values include: pending, running,
            terminated, stopped, stopping, shutting-down, rebooting
        subnet_id:
            The AWS Subnet ID of the EC2 instance
        tags:
            The AWS tags applied to the EC2 instance.
        p_type:
            The AWS region associated with the EC2 instance. Possible instances types can be
            found in: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-
            types.html
        unsupported_reason:
            The reason why protection is not available. If the volume is supported,
            then this field has a value of `null`.
        vpc_id:
            AWS-assigned ID of the VPC associated with the EC2 instance.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'embedded': '_embedded',
        'links': '_links',
        'account_native_id': 'account_native_id',
        'aws_az': 'aws_az',
        'aws_region': 'aws_region',
        'backup_status_info': 'backup_status_info',
        'deletion_timestamp': 'deletion_timestamp',
        'direct_assignment_policy_id': 'direct_assignment_policy_id',
        'ena_support': 'ena_support',
        'environment_id': 'environment_id',
        'has_direct_assignment': 'has_direct_assignment',
        'p_id': 'id',
        'instance_native_id': 'instance_native_id',
        'is_deleted': 'is_deleted',
        'is_supported': 'is_supported',
        'last_backup_timestamp': 'last_backup_timestamp',
        'last_snapshot_timestamp': 'last_snapshot_timestamp',
        'name': 'name',
        'organizational_unit_id': 'organizational_unit_id',
        'protection_info': 'protection_info',
        'protection_status': 'protection_status',
        'state': 'state',
        'subnet_id': 'subnet_id',
        'tags': 'tags',
        'p_type': 'type',
        'unsupported_reason': 'unsupported_reason',
        'vpc_id': 'vpc_id',
    }

    def __init__(
        self,
        embedded: ec2_instance_embedded_.Ec2InstanceEmbedded,
        links: ec2_instance_links_.Ec2InstanceLinks,
        account_native_id: str,
        aws_az: str,
        aws_region: str,
        backup_status_info: backup_status_info_.BackupStatusInfo,
        deletion_timestamp: str,
        direct_assignment_policy_id: str,
        ena_support: bool,
        environment_id: str,
        has_direct_assignment: bool,
        p_id: str,
        instance_native_id: str,
        is_deleted: bool,
        is_supported: bool,
        last_backup_timestamp: str,
        last_snapshot_timestamp: str,
        name: str,
        organizational_unit_id: str,
        protection_info: protection_info_with_rule_.ProtectionInfoWithRule,
        protection_status: str,
        state: str,
        subnet_id: str,
        tags: Sequence[aws_tag_model_.AwsTagModel],
        p_type: str,
        unsupported_reason: str,
        vpc_id: str,
    ) -> None:
        """Constructor for the ReadEc2InstanceResponse class."""

        # Initialize members of the class
        self.embedded: ec2_instance_embedded_.Ec2InstanceEmbedded = embedded
        self.links: ec2_instance_links_.Ec2InstanceLinks = links
        self.account_native_id: str = account_native_id
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info_.BackupStatusInfo = backup_status_info
        self.deletion_timestamp: str = deletion_timestamp
        self.direct_assignment_policy_id: str = direct_assignment_policy_id
        self.ena_support: bool = ena_support
        self.environment_id: str = environment_id
        self.has_direct_assignment: bool = has_direct_assignment
        self.p_id: str = p_id
        self.instance_native_id: str = instance_native_id
        self.is_deleted: bool = is_deleted
        self.is_supported: bool = is_supported
        self.last_backup_timestamp: str = last_backup_timestamp
        self.last_snapshot_timestamp: str = last_snapshot_timestamp
        self.name: str = name
        self.organizational_unit_id: str = organizational_unit_id
        self.protection_info: protection_info_with_rule_.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.state: str = state
        self.subnet_id: str = subnet_id
        self.tags: Sequence[aws_tag_model_.AwsTagModel] = tags
        self.p_type: str = p_type
        self.unsupported_reason: str = unsupported_reason
        self.vpc_id: str = vpc_id

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
        val = dictionary['_embedded']
        val_embedded = ec2_instance_embedded_.Ec2InstanceEmbedded.from_dictionary(val)

        val = dictionary['_links']
        val_links = ec2_instance_links_.Ec2InstanceLinks.from_dictionary(val)

        val = dictionary['account_native_id']
        val_account_native_id = val

        val = dictionary['aws_az']
        val_aws_az = val

        val = dictionary['aws_region']
        val_aws_region = val

        val = dictionary['backup_status_info']
        val_backup_status_info = backup_status_info_.BackupStatusInfo.from_dictionary(val)

        val = dictionary['deletion_timestamp']
        val_deletion_timestamp = val

        val = dictionary['direct_assignment_policy_id']
        val_direct_assignment_policy_id = val

        val = dictionary['ena_support']
        val_ena_support = val

        val = dictionary['environment_id']
        val_environment_id = val

        val = dictionary['has_direct_assignment']
        val_has_direct_assignment = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['instance_native_id']
        val_instance_native_id = val

        val = dictionary['is_deleted']
        val_is_deleted = val

        val = dictionary['is_supported']
        val_is_supported = val

        val = dictionary['last_backup_timestamp']
        val_last_backup_timestamp = val

        val = dictionary['last_snapshot_timestamp']
        val_last_snapshot_timestamp = val

        val = dictionary['name']
        val_name = val

        val = dictionary['organizational_unit_id']
        val_organizational_unit_id = val

        val = dictionary['protection_info']
        val_protection_info = protection_info_with_rule_.ProtectionInfoWithRule.from_dictionary(val)

        val = dictionary['protection_status']
        val_protection_status = val

        val = dictionary['state']
        val_state = val

        val = dictionary['subnet_id']
        val_subnet_id = val

        val = dictionary['tags']

        val_tags = None
        if val:
            val_tags = list()
            for value in val:
                val_tags.append(aws_tag_model_.AwsTagModel.from_dictionary(value))

        val = dictionary['type']
        val_p_type = val

        val = dictionary['unsupported_reason']
        val_unsupported_reason = val

        val = dictionary['vpc_id']
        val_vpc_id = val

        # Return an object of this model
        return cls(
            val_embedded,  # type: ignore
            val_links,  # type: ignore
            val_account_native_id,  # type: ignore
            val_aws_az,  # type: ignore
            val_aws_region,  # type: ignore
            val_backup_status_info,  # type: ignore
            val_deletion_timestamp,  # type: ignore
            val_direct_assignment_policy_id,  # type: ignore
            val_ena_support,  # type: ignore
            val_environment_id,  # type: ignore
            val_has_direct_assignment,  # type: ignore
            val_p_id,  # type: ignore
            val_instance_native_id,  # type: ignore
            val_is_deleted,  # type: ignore
            val_is_supported,  # type: ignore
            val_last_backup_timestamp,  # type: ignore
            val_last_snapshot_timestamp,  # type: ignore
            val_name,  # type: ignore
            val_organizational_unit_id,  # type: ignore
            val_protection_info,  # type: ignore
            val_protection_status,  # type: ignore
            val_state,  # type: ignore
            val_subnet_id,  # type: ignore
            val_tags,  # type: ignore
            val_p_type,  # type: ignore
            val_unsupported_reason,  # type: ignore
            val_vpc_id,  # type: ignore
        )
