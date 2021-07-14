#
# Copyright 2021. Clumio, Inc.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import audit_parent_entity
from clumioapi.models import audit_primary_entity

T = TypeVar('T', bound='AuditTrails')


class AuditTrails:
    """Implementation of the 'AuditTrails' model.

    Attributes:
        action:
            The action performed by the user.

            +------------------+-----------------------------------------------------------+
            |      Action      |                          Details                          |
            +==================+===========================================================+
            | create           | Creating or adding new entities like new policy,          |
            |                  | configuration, user, etc                                  |
            +------------------+-----------------------------------------------------------+
            | update           | Updating an existing entity like policy, settings,        |
            |                  | passwords, etc                                            |
            +------------------+-----------------------------------------------------------+
            | delete           | Delete an existing entity like policy, settings, users,   |
            |                  | etc                                                       |
            +------------------+-----------------------------------------------------------+
            | enable           | Enabling a feature like single sign on or multi factor    |
            |                  | authentication settings                                   |
            +------------------+-----------------------------------------------------------+
            | disable          | Disabling features like single sign on or multi factor    |
            |                  | authentication settings                                   |
            +------------------+-----------------------------------------------------------+
            | browse           | Browsing through entities in the system like mailboxes or |
            |                  | backups, etc                                              |
            +------------------+-----------------------------------------------------------+
            | search           | Searching through entities in the system like mailboxes   |
            |                  | or backups, etc                                           |
            +------------------+-----------------------------------------------------------+
            | login            | User logs in or tries to login                            |
            +------------------+-----------------------------------------------------------+
            | logout           | User explicitly logged out.                               |
            +------------------+-----------------------------------------------------------+
            | register         | When new registrations happen like new                    |
            |                  | datasource registration or user registering for MFA       |
            +------------------+-----------------------------------------------------------+
            | unregister       | When unregistering like unregistering                     |
            |                  | datasource or user unregistering MFA                      |
            +------------------+-----------------------------------------------------------+
            | apply            | Apply policy to protect entities, tags, etc               |
            +------------------+-----------------------------------------------------------+
            | remove           | Remove protection for entities, tags, etc                 |
            +------------------+-----------------------------------------------------------+
            | invite           | Inviting a user                                           |
            +------------------+-----------------------------------------------------------+
            | suspend          | Suspend an existing user                                  |
            +------------------+-----------------------------------------------------------+
            | full_restore     | Full restore of the VM, volume, mailbox, database or      |
            |                  | other entities                                            |
            +------------------+-----------------------------------------------------------+
            | granular_restore | Restoring individual files, mails or records              |
            +------------------+-----------------------------------------------------------+
        category:
            The category of the auditable action performed by the user.

            +-------------------------+----------------------------------------------------+
            |        Category         |                      Details                       |
            +=========================+====================================================+
            | authentication          | Activities related to Authentication               |
            +-------------------------+----------------------------------------------------+
            | data_source             | Data source changes                                |
            +-------------------------+----------------------------------------------------+
            | policy                  | Policy related actions                             |
            +-------------------------+----------------------------------------------------+
            | protection              | Applying and removing protection                   |
            +-------------------------+----------------------------------------------------+
            | restore                 | Restore related operations                         |
            +-------------------------+----------------------------------------------------+
            | tasks                   | Tasks                                              |
            +-------------------------+----------------------------------------------------+
            | backup                  | Backup related operations                          |
            +-------------------------+----------------------------------------------------+
            | users                   | User related operations                            |
            +-------------------------+----------------------------------------------------+
            | api_tokens              | API Token related operations like creating,        |
            |                         | revoking or deleting tokens                        |
            +-------------------------+----------------------------------------------------+
            | kms_config              | Key Management Service(KMS) related operations     |
            +-------------------------+----------------------------------------------------+
            | sso                     | Single sign-on (SSO) related operations            |
            +-------------------------+----------------------------------------------------+
            | mfa                     | Multi Factor Authentication(MFA) related           |
            |                         | operations                                         |
            +-------------------------+----------------------------------------------------+
            | reports                 | Reports related operations                         |
            +-------------------------+----------------------------------------------------+
            | alerts                  | Alerts related operations                          |
            +-------------------------+----------------------------------------------------+
            | cloud_connector         | Cloud connector related operations                 |
            +-------------------------+----------------------------------------------------+
            | cloudformation_template | Cloud Formation Template related operations        |
            +-------------------------+----------------------------------------------------+
            | bandwidth_config        | Bandwidth configuration related changes            |
            +-------------------------+----------------------------------------------------+
            | partner_ecosystem       | Changes to partner ecosystem                       |
            +-------------------------+----------------------------------------------------+
            | ecosystem_changes       | Changes in the ecosystem like adding or remvoings  |
            |                         | VMs                                                |
            +-------------------------+----------------------------------------------------+
        details:
            Additional details about the activity provided in JSON format.
        id:
            The Clumio-assigned ID of the audit event.
        interface:
            The interface used to make the request i.e. 'UI','API'
        ip_address:
            The IP address from which the activity was requested.
        parent_entity:
            The parent object of the primary entity associated with or affected by the
            audit.
            If the primary entity is not a vmware entity, this field will have a value of
            null
            For example, "vmware_vcenter" is the parent entity of primary entity
            "vmware_vm".
        primary_entity:
            The primary object associated with the audit event. Examples of primary entities
            include "aws_connection", "aws_ebs_volume" and "vmware_vm". In some cases like
            global settings, the primary entity may be null.
        status:
            The status of the performed action. 'success', 'failure', 'partial_success'
        timestamp:
            The Timestamp of when the activity began. Represented in RFC-3339 format.
        user_email:
            The email address of the logged in user making the request.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        'action': 'action',
        'category': 'category',
        'details': 'details',
        'id': 'id',
        'interface': 'interface',
        'ip_address': 'ip_address',
        'parent_entity': 'parent_entity',
        'primary_entity': 'primary_entity',
        'status': 'status',
        'timestamp': 'timestamp',
        'user_email': 'user_email',
    }

    def __init__(
        self,
        action: str = None,
        category: str = None,
        details: str = None,
        id: str = None,
        interface: str = None,
        ip_address: str = None,
        parent_entity: audit_parent_entity.AuditParentEntity = None,
        primary_entity: audit_primary_entity.AuditPrimaryEntity = None,
        status: str = None,
        timestamp: str = None,
        user_email: str = None,
    ) -> None:
        """Constructor for the AuditTrails class."""

        # Initialize members of the class
        self.action: str = action
        self.category: str = category
        self.details: str = details
        self.id: str = id
        self.interface: str = interface
        self.ip_address: str = ip_address
        self.parent_entity: audit_parent_entity.AuditParentEntity = parent_entity
        self.primary_entity: audit_primary_entity.AuditPrimaryEntity = primary_entity
        self.status: str = status
        self.timestamp: str = timestamp
        self.user_email: str = user_email

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
        action = dictionary.get('action')
        category = dictionary.get('category')
        details = dictionary.get('details')
        id = dictionary.get('id')
        interface = dictionary.get('interface')
        ip_address = dictionary.get('ip_address')
        key = 'parent_entity'
        parent_entity = (
            audit_parent_entity.AuditParentEntity.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        key = 'primary_entity'
        primary_entity = (
            audit_primary_entity.AuditPrimaryEntity.from_dictionary(dictionary.get(key))
            if dictionary.get(key)
            else None
        )

        status = dictionary.get('status')
        timestamp = dictionary.get('timestamp')
        user_email = dictionary.get('user_email')
        # Return an object of this model
        return cls(
            action,
            category,
            details,
            id,
            interface,
            ip_address,
            parent_entity,
            primary_entity,
            status,
            timestamp,
            user_email,
        )
