#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import audit_parent_entity as audit_parent_entity_
from clumioapi.models import audit_primary_entity as audit_primary_entity_

T = TypeVar('T', bound='AuditTrails')


class AuditTrails:
    """Implementation of the 'AuditTrails' model.

    Attributes:
        action:
            The action performed by the user.

            +-------------------------+----------------------------------------------------+
            |         Action          |                      Details                       |
            +=========================+====================================================+
            | create                  | Creating or adding new entities like new policy,   |
            |                         | configuration, user, etc                           |
            +-------------------------+----------------------------------------------------+
            | update                  | Updating an existing entity like policy, settings, |
            |                         | passwords, etc                                     |
            +-------------------------+----------------------------------------------------+
            | delete                  | Delete an existing entity like policy, settings,   |
            |                         | users, etc                                         |
            +-------------------------+----------------------------------------------------+
            | enable                  | Enabling a feature like single sign on or multi    |
            |                         | factor authentication settings                     |
            +-------------------------+----------------------------------------------------+
            | disable                 | Disabling features like single sign on or multi    |
            |                         | factor authentication settings                     |
            +-------------------------+----------------------------------------------------+
            | browse                  | Browsing through entities in the system like       |
            |                         | mailboxes or backups, etc                          |
            +-------------------------+----------------------------------------------------+
            | search                  | Searching through entities in the system like      |
            |                         | mailboxes or backups, etc                          |
            +-------------------------+----------------------------------------------------+
            | login                   | User logs in or tries to login                     |
            +-------------------------+----------------------------------------------------+
            | logout                  | User explicitly logged out.                        |
            +-------------------------+----------------------------------------------------+
            | register                | When new registrations happen like new             |
            |                         | datasource registration or user registering for    |
            |                         | MFA                                                |
            +-------------------------+----------------------------------------------------+
            | unregister              | When unregistering like unregistering              |
            |                         | datasource or user unregistering MFA               |
            +-------------------------+----------------------------------------------------+
            | apply                   | Apply policy to protect entities, tags, etc        |
            +-------------------------+----------------------------------------------------+
            | remove                  | Remove protection for entities, tags, etc          |
            +-------------------------+----------------------------------------------------+
            | invite                  | Inviting a user                                    |
            +-------------------------+----------------------------------------------------+
            | suspend                 | Suspend an existing user                           |
            +-------------------------+----------------------------------------------------+
            | full_restore            | Full restore of the VM, volume, mailbox, database  |
            |                         | or other entities                                  |
            +-------------------------+----------------------------------------------------+
            | granular_retrieval      | Restoring individual files, mails or records       |
            +-------------------------+----------------------------------------------------+
            | redirected              | When cross region restore occurs.                  |
            +-------------------------+----------------------------------------------------+
            | unapply                 | Assets removed from a rule.                        |
            +-------------------------+----------------------------------------------------+
            | batch_activate          | Activate multiple policies.                        |
            +-------------------------+----------------------------------------------------+
            | batch_deactivate        | Deactivate multiple policies.                      |
            +-------------------------+----------------------------------------------------+
            | grant_email_access      | Grant email access for a file level object. This   |
            |                         | is mutually exclusive with grant_download_access   |
            +-------------------------+----------------------------------------------------+
            | download                | File was download.                                 |
            +-------------------------+----------------------------------------------------+
            | validate_tda_passcode   | Validate passcode that is entered for a download.  |
            +-------------------------+----------------------------------------------------+
            | regenerate_tda_passcode | Regenerate a new passcode used for download.       |
            +-------------------------+----------------------------------------------------+
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
            | ecosystem_changes       | Changes in the ecosystem like adding or removing   |
            |                         | VMs                                                |
            +-------------------------+----------------------------------------------------+
            | organizational_unit     | Changes in the Organizational Unit/Entity group    |
            |                         | such as creation, deletion, patch.                 |
            +-------------------------+----------------------------------------------------+
        details:
            Additional details about the activity provided in JSON format.
        p_id:
            The Clumio-assigned ID of the audit event.
        interface:
            The interface used to make the request i.e. 'UI','API'
        ip_address:
            The IP address from which the activity was requested.
        parent_entity:
            The parent object of the primary entity associated with or affected by the
            audit.
        primary_entity:
            The primary object associated with the audit event. Examples of primary entities
            include "aws_connection", "aws_ebs_volume" and "aws_ec2_instance". In some cases
            like
            global settings, the primary entity may be null.
        status:
            The status of the performed action. 'success', 'failure', 'partial_success'
        timestamp:
            The Timestamp of when the activity began. Represented in RFC-3339 format.
        user_email:
            The email address of the logged in user making the request.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'action': 'action',
        'category': 'category',
        'details': 'details',
        'p_id': 'id',
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
        action: str,
        category: str,
        details: str,
        p_id: str,
        interface: str,
        ip_address: str,
        parent_entity: audit_parent_entity_.AuditParentEntity,
        primary_entity: audit_primary_entity_.AuditPrimaryEntity,
        status: str,
        timestamp: str,
        user_email: str,
    ) -> None:
        """Constructor for the AuditTrails class."""

        # Initialize members of the class
        self.action: str = action
        self.category: str = category
        self.details: str = details
        self.p_id: str = p_id
        self.interface: str = interface
        self.ip_address: str = ip_address
        self.parent_entity: audit_parent_entity_.AuditParentEntity = parent_entity
        self.primary_entity: audit_primary_entity_.AuditPrimaryEntity = primary_entity
        self.status: str = status
        self.timestamp: str = timestamp
        self.user_email: str = user_email

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
        val = dictionary['action']
        val_action = val

        val = dictionary['category']
        val_category = val

        val = dictionary['details']
        val_details = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['interface']
        val_interface = val

        val = dictionary['ip_address']
        val_ip_address = val

        val = dictionary['parent_entity']
        val_parent_entity = audit_parent_entity_.AuditParentEntity.from_dictionary(val)

        val = dictionary['primary_entity']
        val_primary_entity = audit_primary_entity_.AuditPrimaryEntity.from_dictionary(val)

        val = dictionary['status']
        val_status = val

        val = dictionary['timestamp']
        val_timestamp = val

        val = dictionary['user_email']
        val_user_email = val

        # Return an object of this model
        return cls(
            val_action,  # type: ignore
            val_category,  # type: ignore
            val_details,  # type: ignore
            val_p_id,  # type: ignore
            val_interface,  # type: ignore
            val_ip_address,  # type: ignore
            val_parent_entity,  # type: ignore
            val_primary_entity,  # type: ignore
            val_status,  # type: ignore
            val_timestamp,  # type: ignore
            val_user_email,  # type: ignore
        )
