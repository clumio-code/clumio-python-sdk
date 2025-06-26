#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import aws_tag_model
from clumioapi.models import backup_status_info
from clumioapi.models import ec2_instance_embedded
from clumioapi.models import ec2_instance_links
from clumioapi.models import protection_info_with_rule

T = TypeVar('T', bound='EC2')


class EC2:
    """Implementation of the 'EC2' model.

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
    _names = {
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
        embedded: ec2_instance_embedded.Ec2InstanceEmbedded = None,
        links: ec2_instance_links.Ec2InstanceLinks = None,
        account_native_id: str = None,
        aws_az: str = None,
        aws_region: str = None,
        backup_status_info: backup_status_info.BackupStatusInfo = None,
        deletion_timestamp: str = None,
        direct_assignment_policy_id: str = None,
        ena_support: bool = None,
        environment_id: str = None,
        has_direct_assignment: bool = None,
        p_id: str = None,
        instance_native_id: str = None,
        is_deleted: bool = None,
        is_supported: bool = None,
        last_backup_timestamp: str = None,
        last_snapshot_timestamp: str = None,
        name: str = None,
        organizational_unit_id: str = None,
        protection_info: protection_info_with_rule.ProtectionInfoWithRule = None,
        protection_status: str = None,
        state: str = None,
        subnet_id: str = None,
        tags: Sequence[aws_tag_model.AwsTagModel] = None,
        p_type: str = None,
        unsupported_reason: str = None,
        vpc_id: str = None,
    ) -> None:
        """Constructor for the EC2 class."""

        # Initialize members of the class
        self.embedded: ec2_instance_embedded.Ec2InstanceEmbedded = embedded
        self.links: ec2_instance_links.Ec2InstanceLinks = links
        self.account_native_id: str = account_native_id
        self.aws_az: str = aws_az
        self.aws_region: str = aws_region
        self.backup_status_info: backup_status_info.BackupStatusInfo = backup_status_info
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
        self.protection_info: protection_info_with_rule.ProtectionInfoWithRule = protection_info
        self.protection_status: str = protection_status
        self.state: str = state
        self.subnet_id: str = subnet_id
        self.tags: Sequence[aws_tag_model.AwsTagModel] = tags
        self.p_type: str = p_type
        self.unsupported_reason: str = unsupported_reason
        self.vpc_id: str = vpc_id

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
        key = '_embedded'
        embedded = (
            ec2_instance_embedded.Ec2InstanceEmbedded.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = '_links'
        links = (
            ec2_instance_links.Ec2InstanceLinks.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        account_native_id = dictionary.get('account_native_id')
        aws_az = dictionary.get('aws_az')
        aws_region = dictionary.get('aws_region')
        key = 'backup_status_info'
        p_backup_status_info = (
            backup_status_info.BackupStatusInfo.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        deletion_timestamp = dictionary.get('deletion_timestamp')
        direct_assignment_policy_id = dictionary.get('direct_assignment_policy_id')
        ena_support = dictionary.get('ena_support')
        environment_id = dictionary.get('environment_id')
        has_direct_assignment = dictionary.get('has_direct_assignment')
        p_id = dictionary.get('id')
        instance_native_id = dictionary.get('instance_native_id')
        is_deleted = dictionary.get('is_deleted')
        is_supported = dictionary.get('is_supported')
        last_backup_timestamp = dictionary.get('last_backup_timestamp')
        last_snapshot_timestamp = dictionary.get('last_snapshot_timestamp')
        name = dictionary.get('name')
        organizational_unit_id = dictionary.get('organizational_unit_id')
        key = 'protection_info'
        protection_info = (
            protection_info_with_rule.ProtectionInfoWithRule.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        protection_status = dictionary.get('protection_status')
        state = dictionary.get('state')
        subnet_id = dictionary.get('subnet_id')
        tags = None
        if dictionary.get('tags'):
            tags = list()
            for value in dictionary.get('tags'):
                tags.append(aws_tag_model.AwsTagModel.from_dictionary(value))

        p_type = dictionary.get('type')
        unsupported_reason = dictionary.get('unsupported_reason')
        vpc_id = dictionary.get('vpc_id')
        # Return an object of this model
        return cls(
            embedded,
            links,
            account_native_id,
            aws_az,
            aws_region,
            p_backup_status_info,
            deletion_timestamp,
            direct_assignment_policy_id,
            ena_support,
            environment_id,
            has_direct_assignment,
            p_id,
            instance_native_id,
            is_deleted,
            is_supported,
            last_backup_timestamp,
            last_snapshot_timestamp,
            name,
            organizational_unit_id,
            protection_info,
            protection_status,
            state,
            subnet_id,
            tags,
            p_type,
            unsupported_reason,
            vpc_id,
        )
