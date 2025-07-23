#
# Copyright 2023. Clumio, A Commvault Company.
#

from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import task_links as task_links_
from clumioapi.models import task_parent_entity as task_parent_entity_
from clumioapi.models import task_primary_entity as task_primary_entity_

T = TypeVar('T', bound='TaskWithETag')


class TaskWithETag:
    """Implementation of the 'TaskWithETag' model.

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
        etag: str | None = None,
        links: task_links_.TaskLinks | None = None,
        category: str | None = None,
        created_timestamp: str | None = None,
        end_timestamp: str | None = None,
        genre: str | None = None,
        p_id: str | None = None,
        is_abortable: bool | None = None,
        parent_entity: task_parent_entity_.TaskParentEntity | None = None,
        primary_entity: task_primary_entity_.TaskPrimaryEntity | None = None,
        progress_percentage: int | None = None,
        start_timestamp: str | None = None,
        status: str | None = None,
        p_type: str | None = None,
    ) -> None:
        """Constructor for the TaskWithETag class."""

        # Initialize members of the class
        self.etag: str | None = etag
        self.links: task_links_.TaskLinks | None = links
        self.category: str | None = category
        self.created_timestamp: str | None = created_timestamp
        self.end_timestamp: str | None = end_timestamp
        self.genre: str | None = genre
        self.p_id: str | None = p_id
        self.is_abortable: bool | None = is_abortable
        self.parent_entity: task_parent_entity_.TaskParentEntity | None = parent_entity
        self.primary_entity: task_primary_entity_.TaskPrimaryEntity | None = primary_entity
        self.progress_percentage: int | None = progress_percentage
        self.start_timestamp: str | None = start_timestamp
        self.status: str | None = status
        self.p_type: str | None = p_type

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
        val = dictionary.get('_etag', None)
        val_etag = val

        val = dictionary.get('_links', None)
        val_links = task_links_.TaskLinks.from_dictionary(val)

        val = dictionary.get('category', None)
        val_category = val

        val = dictionary.get('created_timestamp', None)
        val_created_timestamp = val

        val = dictionary.get('end_timestamp', None)
        val_end_timestamp = val

        val = dictionary.get('genre', None)
        val_genre = val

        val = dictionary.get('id', None)
        val_p_id = val

        val = dictionary.get('is_abortable', None)
        val_is_abortable = val

        val = dictionary.get('parent_entity', None)
        val_parent_entity = task_parent_entity_.TaskParentEntity.from_dictionary(val)

        val = dictionary.get('primary_entity', None)
        val_primary_entity = task_primary_entity_.TaskPrimaryEntity.from_dictionary(val)

        val = dictionary.get('progress_percentage', None)
        val_progress_percentage = val

        val = dictionary.get('start_timestamp', None)
        val_start_timestamp = val

        val = dictionary.get('status', None)
        val_status = val

        val = dictionary.get('type', None)
        val_p_type = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_category,
            val_created_timestamp,
            val_end_timestamp,
            val_genre,
            val_p_id,
            val_is_abortable,
            val_parent_entity,
            val_primary_entity,
            val_progress_percentage,
            val_start_timestamp,
            val_status,
            val_p_type,
        )
