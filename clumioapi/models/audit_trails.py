#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import audit_parent_entity as audit_parent_entity_
from clumioapi.models import audit_primary_entity as audit_primary_entity_
import requests

T = TypeVar('T', bound='AuditTrails')


@dataclasses.dataclass
class AuditTrails:
    """Implementation of the 'AuditTrails' model.

        Attributes:
            Action:
                The action performed by the user.

    +-------------------------+----------------------------------------------------+
    |         action          |                      details                       |
    +=========================+====================================================+
    | create                  | creating or adding new entities like new policy,   |
    |                         | configuration, user, etc                           |
    +-------------------------+----------------------------------------------------+
    | update                  | updating an existing entity like policy, settings, |
    |                         | passwords, etc                                     |
    +-------------------------+----------------------------------------------------+
    | delete                  | delete an existing entity like policy, settings,   |
    |                         | users, etc                                         |
    +-------------------------+----------------------------------------------------+
    | enable                  | enabling a feature like single sign on or multi    |
    |                         | factor authentication settings                     |
    +-------------------------+----------------------------------------------------+
    | disable                 | disabling features like single sign on or multi    |
    |                         | factor authentication settings                     |
    +-------------------------+----------------------------------------------------+
    | browse                  | browsing through entities in the system like       |
    |                         | mailboxes or backups, etc                          |
    +-------------------------+----------------------------------------------------+
    | search                  | searching through entities in the system like      |
    |                         | mailboxes or backups, etc                          |
    +-------------------------+----------------------------------------------------+
    | login                   | user logs in or tries to login                     |
    +-------------------------+----------------------------------------------------+
    | logout                  | user explicitly logged out.                        |
    +-------------------------+----------------------------------------------------+
    | register                | when new registrations happen like new             |
    |                         | datasource registration or user registering for    |
    |                         | mfa                                                |
    +-------------------------+----------------------------------------------------+
    | unregister              | when unregistering like unregistering              |
    |                         | datasource or user unregistering mfa               |
    +-------------------------+----------------------------------------------------+
    | apply                   | apply policy to protect entities, tags, etc        |
    +-------------------------+----------------------------------------------------+
    | remove                  | remove protection for entities, tags, etc          |
    +-------------------------+----------------------------------------------------+
    | invite                  | inviting a user                                    |
    +-------------------------+----------------------------------------------------+
    | suspend                 | suspend an existing user                           |
    +-------------------------+----------------------------------------------------+
    | full_restore            | full restore of the vm, volume, mailbox, database  |
    |                         | or other entities                                  |
    +-------------------------+----------------------------------------------------+
    | granular_retrieval      | restoring individual files, mails or records       |
    +-------------------------+----------------------------------------------------+
    | redirected              | when cross region restore occurs.                  |
    +-------------------------+----------------------------------------------------+
    | unapply                 | assets removed from a rule.                        |
    +-------------------------+----------------------------------------------------+
    | batch_activate          | activate multiple policies.                        |
    +-------------------------+----------------------------------------------------+
    | batch_deactivate        | deactivate multiple policies.                      |
    +-------------------------+----------------------------------------------------+
    | grant_email_access      | grant email access for a file level object. this   |
    |                         | is mutually exclusive with grant_download_access   |
    +-------------------------+----------------------------------------------------+
    | download                | file was download.                                 |
    +-------------------------+----------------------------------------------------+
    | validate_tda_passcode   | validate passcode that is entered for a download.  |
    +-------------------------+----------------------------------------------------+
    | regenerate_tda_passcode | regenerate a new passcode used for download.       |
    +-------------------------+----------------------------------------------------+
    .

            Category:
                The category of the auditable action performed by the user.

    +-------------------------+----------------------------------------------------+
    |        category         |                      details                       |
    +=========================+====================================================+
    | authentication          | activities related to authentication               |
    +-------------------------+----------------------------------------------------+
    | data_source             | data source changes                                |
    +-------------------------+----------------------------------------------------+
    | policy                  | policy related actions                             |
    +-------------------------+----------------------------------------------------+
    | protection              | applying and removing protection                   |
    +-------------------------+----------------------------------------------------+
    | restore                 | restore related operations                         |
    +-------------------------+----------------------------------------------------+
    | tasks                   | tasks                                              |
    +-------------------------+----------------------------------------------------+
    | backup                  | backup related operations                          |
    +-------------------------+----------------------------------------------------+
    | users                   | user related operations                            |
    +-------------------------+----------------------------------------------------+
    | api_tokens              | api token related operations like creating,        |
    |                         | revoking or deleting tokens                        |
    +-------------------------+----------------------------------------------------+
    | kms_config              | key management service(kms) related operations     |
    +-------------------------+----------------------------------------------------+
    | sso                     | single sign-on (sso) related operations            |
    +-------------------------+----------------------------------------------------+
    | mfa                     | multi factor authentication(mfa) related           |
    |                         | operations                                         |
    +-------------------------+----------------------------------------------------+
    | reports                 | reports related operations                         |
    +-------------------------+----------------------------------------------------+
    | alerts                  | alerts related operations                          |
    +-------------------------+----------------------------------------------------+
    | cloud_connector         | cloud connector related operations                 |
    +-------------------------+----------------------------------------------------+
    | cloudformation_template | cloud formation template related operations        |
    +-------------------------+----------------------------------------------------+
    | bandwidth_config        | bandwidth configuration related changes            |
    +-------------------------+----------------------------------------------------+
    | partner_ecosystem       | changes to partner ecosystem                       |
    +-------------------------+----------------------------------------------------+
    | ecosystem_changes       | changes in the ecosystem like adding or removing   |
    |                         | vms                                                |
    +-------------------------+----------------------------------------------------+
    | organizational_unit     | changes in the organizational unit/entity group    |
    |                         | such as creation, deletion, patch.                 |
    +-------------------------+----------------------------------------------------+
    .

            Details:
                Additional details about the activity provided in json format.

            Id:
                The clumio-assigned id of the audit event.

            Interface:
                The interface used to make the request i.e. 'ui','api'.

            IpAddress:
                The ip address from which the activity was requested.

            ParentEntity:
                The parent object of the primary entity associated with or affected by the audit.

            PrimaryEntity:
                The primary object associated with the audit event. examples of primary entities
    include "aws_connection", "aws_ebs_volume" and "aws_ec2_instance". in some cases like
    global settings, the primary entity may be null.

            Status:
                The status of the performed action. 'success', 'failure', 'partial_success'.

            Timestamp:
                The timestamp of when the activity began. represented in rfc-3339 format.

            UserEmail:
                The email address of the logged in user making the request.

    """

    Action: str | None = None
    Category: str | None = None
    Details: str | None = None
    Id: str | None = None
    Interface: str | None = None
    IpAddress: str | None = None
    ParentEntity: audit_parent_entity_.AuditParentEntity | None = None
    PrimaryEntity: audit_primary_entity_.AuditPrimaryEntity | None = None
    Status: str | None = None
    Timestamp: str | None = None
    UserEmail: str | None = None

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
        val = dictionary.get('action', None)
        val_action = val

        val = dictionary.get('category', None)
        val_category = val

        val = dictionary.get('details', None)
        val_details = val

        val = dictionary.get('id', None)
        val_id = val

        val = dictionary.get('interface', None)
        val_interface = val

        val = dictionary.get('ip_address', None)
        val_ip_address = val

        val = dictionary.get('parent_entity', None)
        val_parent_entity = audit_parent_entity_.AuditParentEntity.from_dictionary(val)

        val = dictionary.get('primary_entity', None)
        val_primary_entity = audit_primary_entity_.AuditPrimaryEntity.from_dictionary(val)

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('timestamp', None)
        val_timestamp = val

        val = dictionary.get('user_email', None)
        val_user_email = val

        # Return an object of this model
        return cls(
            val_action,
            val_category,
            val_details,
            val_id,
            val_interface,
            val_ip_address,
            val_parent_entity,
            val_primary_entity,
            val_status,
            val_timestamp,
            val_user_email,
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
