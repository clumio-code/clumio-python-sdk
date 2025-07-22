#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import task_links as task_links_
from clumioapi.models import task_parent_entity as task_parent_entity_
from clumioapi.models import task_primary_entity as task_primary_entity_

T = TypeVar('T', bound='ReadTaskResponse')


class ReadTaskResponse:
    """Implementation of the 'ReadTaskResponse' model.

    Attributes:
        etag:
            The ETag value.
        links:
            URLs to pages related to the resource.
        category:
            The task category. Examples of task types include "backup", "restore",
            "snapshot", and "system".

            +-------------------+----------------------------------------------------------+
            |     Category      |                       Description                        |
            +===================+==========================================================+
            | backup            | Encompasses all modes of backups. This does not include  |
            |                   | in-account snapshots.                                    |
            +-------------------+----------------------------------------------------------+
            | restore           | Encompasses all modes of restores. This does not include |
            |                   | restores of in-account snapshots.                        |
            +-------------------+----------------------------------------------------------+
            | snapshot          | Encompasses all modes of in-account snapshots.           |
            +-------------------+----------------------------------------------------------+
            | snapshot_restore  | Encompasses all modes of snapshot restores.              |
            +-------------------+----------------------------------------------------------+
            | system            | Encompasses a variety of system-initiated tasks, such as |
            |                   | aws_rds_backup_target_setup and                          |
            |                   | aws_ec2_instance_backup_indexing.                        |
            +-------------------+----------------------------------------------------------+
            | report_generation | Encompasses task types which generate reports, such as   |
            |                   | activity_report_file_download.                           |
            +-------------------+----------------------------------------------------------+
            | management        | Encompasses user-initiated tasks which manage Clumio     |
            |                   | resources, such as organizational_unit_update and        |
            |                   | policy_update.                                           |
            +-------------------+----------------------------------------------------------+
        created_timestamp:
            The timestamp of when the task was created. Represented in RFC-3339 format.
        end_timestamp:
            The timestamp of when the task ended. If this task has not yet ended,
            then this field has a value of `null`. Represented in RFC-3339 format.
        genre:
            The task genre. A genre is a high-level collection of task categories.

            +----------------+-------------------------------------------------------------+
            |     Genre      |                         Description                         |
            +================+=============================================================+
            | operational    | Encompasses all backup, restore, snapshot, and              |
            |                | snapshot_restore tasks.                                     |
            +----------------+-------------------------------------------------------------+
            | administrative | Encompasses management, system, and report_generation       |
            |                | tasks.                                                      |
            +----------------+-------------------------------------------------------------+
        p_id:
            The Clumio-assigned ID of the task.
        is_abortable:
            Determines whether or not this task can be aborted.
            A task can be aborted if its status is either "queued" or "in_progress".
            Tasks of certain types including "aws_ebs_volume_backup_indexing" cannot be
            aborted.
        parent_entity:
            The parent entity associated with the task.
        primary_entity:
            The primary entity associated with the task.
        progress_percentage:
            The percentage progress of task completion. Measured as an integer value between
            0 and 100.
        start_timestamp:
            The timestamp of when the task started. If this task has not started yet,
            then this field has a value of `null`. Represented in RFC-3339 format.
        status:
            The task status. Examples of task statuses include, "queued", "in_progress", and
            "completed".
            Refer to the Task Status table for a complete list of task statuses.
        p_type:
            Refer to the Task Type table for a complete list of task types.
    """

    # Create a mapping from Model property names to API property names
    _names: dict[str, str] = {
        'etag': '_etag',
        'links': '_links',
        'category': 'category',
        'created_timestamp': 'created_timestamp',
        'end_timestamp': 'end_timestamp',
        'genre': 'genre',
        'p_id': 'id',
        'is_abortable': 'is_abortable',
        'parent_entity': 'parent_entity',
        'primary_entity': 'primary_entity',
        'progress_percentage': 'progress_percentage',
        'start_timestamp': 'start_timestamp',
        'status': 'status',
        'p_type': 'type',
    }

    def __init__(
        self,
        etag: str,
        links: task_links_.TaskLinks,
        category: str,
        created_timestamp: str,
        end_timestamp: str,
        genre: str,
        p_id: str,
        is_abortable: bool,
        parent_entity: task_parent_entity_.TaskParentEntity,
        primary_entity: task_primary_entity_.TaskPrimaryEntity,
        progress_percentage: int,
        start_timestamp: str,
        status: str,
        p_type: str,
    ) -> None:
        """Constructor for the ReadTaskResponse class."""

        # Initialize members of the class
        self.etag: str = etag
        self.links: task_links_.TaskLinks = links
        self.category: str = category
        self.created_timestamp: str = created_timestamp
        self.end_timestamp: str = end_timestamp
        self.genre: str = genre
        self.p_id: str = p_id
        self.is_abortable: bool = is_abortable
        self.parent_entity: task_parent_entity_.TaskParentEntity = parent_entity
        self.primary_entity: task_primary_entity_.TaskPrimaryEntity = primary_entity
        self.progress_percentage: int = progress_percentage
        self.start_timestamp: str = start_timestamp
        self.status: str = status
        self.p_type: str = p_type

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
        val = dictionary['_etag']
        val_etag = val

        val = dictionary['_links']
        val_links = task_links_.TaskLinks.from_dictionary(val)

        val = dictionary['category']
        val_category = val

        val = dictionary['created_timestamp']
        val_created_timestamp = val

        val = dictionary['end_timestamp']
        val_end_timestamp = val

        val = dictionary['genre']
        val_genre = val

        val = dictionary['id']
        val_p_id = val

        val = dictionary['is_abortable']
        val_is_abortable = val

        val = dictionary['parent_entity']
        val_parent_entity = task_parent_entity_.TaskParentEntity.from_dictionary(val)

        val = dictionary['primary_entity']
        val_primary_entity = task_primary_entity_.TaskPrimaryEntity.from_dictionary(val)

        val = dictionary['progress_percentage']
        val_progress_percentage = val

        val = dictionary['start_timestamp']
        val_start_timestamp = val

        val = dictionary['status']
        val_status = val

        val = dictionary['type']
        val_p_type = val

        # Return an object of this model
        return cls(
            val_etag,  # type: ignore
            val_links,  # type: ignore
            val_category,  # type: ignore
            val_created_timestamp,  # type: ignore
            val_end_timestamp,  # type: ignore
            val_genre,  # type: ignore
            val_p_id,  # type: ignore
            val_is_abortable,  # type: ignore
            val_parent_entity,  # type: ignore
            val_primary_entity,  # type: ignore
            val_progress_percentage,  # type: ignore
            val_start_timestamp,  # type: ignore
            val_status,  # type: ignore
            val_p_type,  # type: ignore
        )
