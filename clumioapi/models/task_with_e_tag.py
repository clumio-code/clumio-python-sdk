#
# Copyright 2023. Clumio, A Commvault Company.
#
import dataclasses
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar

from clumioapi.api_helper import camel_to_snake
from clumioapi.models import task_links as task_links_
from clumioapi.models import task_parent_entity as task_parent_entity_
from clumioapi.models import task_primary_entity as task_primary_entity_
import requests

T = TypeVar('T', bound='TaskWithETag')


@dataclasses.dataclass
class TaskWithETag:
    """Implementation of the 'TaskWithETag' model.

        Attributes:
            Etag:
                The etag value.

            Links:
                Urls to pages related to the resource.

            Category:
                The task category. examples of task types include "backup", "restore", "snapshot", and "system".

    +-------------------+----------------------------------------------------------+
    |     category      |                       description                        |
    +===================+==========================================================+
    | backup            | encompasses all modes of backups. this does not include  |
    |                   | in-account snapshots.                                    |
    +-------------------+----------------------------------------------------------+
    | restore           | encompasses all modes of restores. this does not include |
    |                   | restores of in-account snapshots.                        |
    +-------------------+----------------------------------------------------------+
    | snapshot          | encompasses all modes of in-account snapshots.           |
    +-------------------+----------------------------------------------------------+
    | snapshot_restore  | encompasses all modes of snapshot restores.              |
    +-------------------+----------------------------------------------------------+
    | system            | encompasses a variety of system-initiated tasks, such as |
    |                   | aws_rds_backup_target_setup and                          |
    |                   | aws_ec2_instance_backup_indexing.                        |
    +-------------------+----------------------------------------------------------+
    | report_generation | encompasses task types which generate reports, such as   |
    |                   | activity_report_file_download.                           |
    +-------------------+----------------------------------------------------------+
    | management        | encompasses user-initiated tasks which manage clumio     |
    |                   | resources, such as organizational_unit_update and        |
    |                   | policy_update.                                           |
    +-------------------+----------------------------------------------------------+
    .

            CreatedTimestamp:
                The timestamp of when the task was created. represented in rfc-3339 format.

            EndTimestamp:
                The timestamp of when the task ended. if this task has not yet ended,
    then this field has a value of `null`. represented in rfc-3339 format.

            Genre:
                The task genre. a genre is a high-level collection of task categories.

    +----------------+-------------------------------------------------------------+
    |     genre      |                         description                         |
    +================+=============================================================+
    | operational    | encompasses all backup, restore, snapshot, and              |
    |                | snapshot_restore tasks.                                     |
    +----------------+-------------------------------------------------------------+
    | administrative | encompasses management, system, and report_generation       |
    |                | tasks.                                                      |
    +----------------+-------------------------------------------------------------+
    .

            Id:
                The clumio-assigned id of the task.

            IsAbortable:
                Determines whether or not this task can be aborted.
    a task can be aborted if its status is either "queued" or "in_progress".
    tasks of certain types including "aws_ebs_volume_backup_indexing" cannot be aborted.

            ParentEntity:
                The parent entity associated with the task.

            PrimaryEntity:
                The primary entity associated with the task.

            ProgressPercentage:
                The percentage progress of task completion. measured as an integer value between 0 and 100.

            StartTimestamp:
                The timestamp of when the task started. if this task has not started yet,
    then this field has a value of `null`. represented in rfc-3339 format.

            Status:
                The task status. examples of task statuses include, "queued", "in_progress", and "completed".
    refer to the task status table for a complete list of task statuses.

            Type:
                Refer to the task type table for a complete list of task types.

    """

    Etag: str | None = None
    Links: task_links_.TaskLinks | None = None
    Category: str | None = None
    CreatedTimestamp: str | None = None
    EndTimestamp: str | None = None
    Genre: str | None = None
    Id: str | None = None
    IsAbortable: bool | None = None
    ParentEntity: task_parent_entity_.TaskParentEntity | None = None
    PrimaryEntity: task_primary_entity_.TaskPrimaryEntity | None = None
    ProgressPercentage: int | None = None
    StartTimestamp: str | None = None
    Status: str | None = None
    Type: str | None = None

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
        val_id = val

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
        val_type = val

        # Return an object of this model
        return cls(
            val_etag,
            val_links,
            val_category,
            val_created_timestamp,
            val_end_timestamp,
            val_genre,
            val_id,
            val_is_abortable,
            val_parent_entity,
            val_primary_entity,
            val_progress_percentage,
            val_start_timestamp,
            val_status,
            val_type,
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
