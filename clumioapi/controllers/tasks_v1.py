#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
import re
from typing import Any, Iterator, Optional, Union
import urllib.parse

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.controllers.types import aws_s3_buckets_v1_bucket_matcher_types
from clumioapi.controllers.types import tasks_types
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_tasks_response
from clumioapi.models import read_task_response
from clumioapi.models import update_task_response
from clumioapi.models import update_task_v1_request
import requests
import retrying


class TasksV1Controller:
    """A Controller to access Endpoints for tasks resource."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller
        self.client = self.controller.client
        self.headers = {
            'accept': 'application/api.clumio.tasks=v1+json',
            'x-clumio-organizationalunit-context': self.controller.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if self.controller.config.custom_headers != None:
            self.headers.update(self.controller.config.custom_headers)

    def list_tasks(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: tasks_types.ListTasksV1FilterT | None = None,
        **kwargs,
    ) -> list_tasks_response.ListTasksResponse:
        """Returns a list of tasks. Tasks include scheduled backup and on-demand restore
        related tasks.

        The following table describes the supported task types.

        +-----------------------------------+------------------------------------------+
        |             Task Type             |               Description                |
        +===================================+==========================================+
        | aws_ebs_volume_file_restore       | A restore task for a file within an EBS  |
        |                                   | volume.                                  |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_backup_seeding     | The initial backup task of an EBS Volume |
        |                                   | - future backups are incremental.        |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_incremental_backup | A scheduled incremental backup task for  |
        |                                   | an EBS volume.                           |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_backup_indexing    | A post-processing task that indexes the  |
        |                                   | contents                                 |
        |                                   | of an EBS volume in preparation for      |
        |                                   | file-level indexing and restores.        |
        |                                   | The `aws_ebs_volume_backup_indexing`     |
        |                                   | task cannot be aborted.                  |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_restore            | A restore task for an EBS Volume.        |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mailbox_seeding      | The initial backup task of a mailbox -   |
        |                                   | future backups are incremental.          |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mailbox_backup       | A scheduled incremental backup task for  |
        |                                   | a mailbox.                               |
        +-----------------------------------+------------------------------------------+
        | microsoft365_inventory_sync       | A task that synchronizes Clumio with the |
        |                                   | Microsoft 365 domain by gathering        |
        |                                   | mailbox information and other data, such |
        |                                   | as usage and sizing statistics.          |
        |                                   | The `microsoft365_inventory_sync` task   |
        |                                   | cannot be aborted.                       |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mail_restore         | A restore task for a microsoft365        |
        |                                   | mailbox.                                 |
        +-----------------------------------+------------------------------------------+


        The following table describes the supported task statuses.

        +-------------+----------------------------------------------------------------+
        | Task Status |                          Description                           |
        +=============+================================================================+
        | queued      | A task that is waiting to begin. A task that is in queue can   |
        |             | be aborted at any time.                                        |
        +-------------+----------------------------------------------------------------+
        | in_progress | A task that is currently running. Once the task has            |
        |             | successfully completed,                                        |
        |             | the task status changes to `completed`.                        |
        |             | A task that is in progress can be aborted at any time.         |
        +-------------+----------------------------------------------------------------+
        | completed   | A task that has successfully completed.                        |
        +-------------+----------------------------------------------------------------+
        | failed      | A task that has failed to complete.                            |
        +-------------+----------------------------------------------------------------+
        | aborting    | A task that is in the process of aborting.                     |
        |             | Only tasks that are queued or in progress can be aborted.      |
        |             | Once a task has successfully aborted, the task status changes  |
        |             | to `aborted`.                                                  |
        +-------------+----------------------------------------------------------------+
        | aborted     | A task that has fully aborted.                                 |
        +-------------+----------------------------------------------------------------+

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +----------------------+------------------+------------------------------------+
                |        Field         | Filter Condition |            Description             |
                +======================+==================+====================================+
                | primary_entity.value | $contains        | The name or value given to the     |
                |                      |                  | entity affected by the task.       |
                |                      |                  | For example, filter={"primary_enti |
                |                      |                  | ty.value":{"$contains":"ubuntu-    |
                |                      |                  | bbp-medium-01"}}                   |
                +----------------------+------------------+------------------------------------+
                | primary_entity.id    | $contains        | The unique ID given to the entity  |
                |                      |                  | affected by the task.              |
                |                      |                  | For example, filter={"primary_enti |
                |                      |                  | ty.id":{"eq":"c8011712-9e16-11eb-  |
                |                      |                  | bb8f-0a06889d7896"}}               |
                +----------------------+------------------+------------------------------------+
                | created_timestamp    | $lte, $gte       | The timestamp value of when the    |
                |                      |                  | task was started                   |
                |                      |                  | (cannot exceed the last 6 months)  |
                |                      |                  | in RFC-3999 format.                |
                |                      |                  | For example, filter={"created_time |
                |                      |                  | stamp":{"$lte":                    |
                |                      |                  | "2020-09-13T00:00:00Z"}}           |
                +----------------------+------------------+------------------------------------+
                | type                 | $in              | The task type.                     |
                |                      |                  | Examples of task types include     |
                |                      |                  | "ebs_indexing", and                |
                |                      |                  | "file_restore".                    |
                |                      |                  | Refer to the Task Type table for a |
                |                      |                  | complete list of task types.       |
                |                      |                  | For example, filter={"type":{"$in" |
                |                      |                  | :["ebs_incremental_backup"]}}      |
                +----------------------+------------------+------------------------------------+
                | category             | $in              | The task category.                 |
                |                      |                  | Examples of task categories        |
                |                      |                  | include "backup", "restore", and   |
                |                      |                  | "management".                      |
                |                      |                  | For example, filter={"category":{" |
                |                      |                  | $in":["backup"]}}                  |
                +----------------------+------------------+------------------------------------+
                | genre                | $in              | The task genre.                    |
                |                      |                  | Examples of task types include     |
                |                      |                  | "operational" and                  |
                |                      |                  | "administrative".                  |
                |                      |                  | For example, filter={"genre":{"$in |
                |                      |                  | ":["operational"]}}                |
                +----------------------+------------------+------------------------------------+
                | status               | $in              | The task status.                   |
                |                      |                  | Examples of task statuses include, |
                |                      |                  | "queued", "in_progress", and       |
                |                      |                  | "completed".                       |
                |                      |                  | Refer to the Task Status table for |
                |                      |                  | a complete list of task statuses.  |
                |                      |                  | For example, filter={"status":{"$i |
                |                      |                  | n":["completed"]}}                 |
                +----------------------+------------------+------------------------------------+
                | id                   | $in              | The Clumio-assigned ID of the      |
                |                      |                  | task. Multiple tasks can be        |
                |                      |                  | specified.                         |
                |                      |                  | For example,                       |
                |                      |                  | filter={"id":{"in":["101","114"]}} |
                +----------------------+------------------+------------------------------------+

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return list_tasks_response.ListTasksResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/tasks'

        _query_parameters: dict[str, Any] = {}
        _query_parameters = {
            'limit': limit,
            'start': start,
            'filter': filter.query_str if filter else None,
        }

        resp_instance: list_tasks_response.ListTasksResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'list_tasks for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def read_task(
        self, task_id: str | None = None, **kwargs
    ) -> read_task_response.ReadTaskResponse:
        """Returns a representation of the specified task.

        Args:
            task_id:
                Performs the operation on the task with the specified ID.
        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return read_task_response.ReadTaskResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/tasks/{task_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'task_id': task_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: read_task_response.ReadTaskResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'read_task for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance

    def update_task(
        self,
        task_id: str | None = None,
        body: update_task_v1_request.UpdateTaskV1Request | None = None,
        **kwargs,
    ) -> update_task_response.UpdateTaskResponse:
        """Manages the specified task. Managing a task includes aborting a task that is in
        queue or in progress.

        Args:
            task_id:
                Performs the operation on the task with the specified ID.
            body:

        """

        def get_instance_from_response(resp: requests.Response) -> Any:
            return update_task_response.UpdateTaskResponse.from_response(resp)

        # Prepare query URL
        _url_path = '/tasks/{task_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'task_id': task_id})

        _query_parameters: dict[str, Any] = {}

        resp_instance: update_task_response.UpdateTaskResponse
        # Execute request
        resp: requests.Response
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=body.dict() if body else None,
                raw_response=True,
                **kwargs,
            )
        except requests.exceptions.HTTPError as e:
            resp = e.response

        if not resp.ok:
            error_str = f'update_task for url {urllib.parse.unquote(resp.url)} failed.'
            raise clumio_exception.ClumioException(error_str, resp=resp)

        resp_instance = get_instance_from_response(resp)

        return resp_instance


class TasksV1ControllerPaginator:
    """A Controller to access Endpoints for tasks resource with pagination."""

    def __init__(self, controller: base_controller.BaseController) -> None:
        self.controller = controller

    @retrying.retry(
        retry_on_exception=requests.exceptions.ConnectionError,
        wait_exponential_multiplier=2000,
        stop_max_attempt_number=5,
    )
    def list_tasks(
        self,
        limit: int | None = None,
        start: str | None = None,
        filter: tasks_types.ListTasksV1FilterT | None = None,
        **kwargs,
    ) -> Iterator[list_tasks_response.ListTasksResponse]:
        """Returns a list of tasks. Tasks include scheduled backup and on-demand restore
        related tasks.

        The following table describes the supported task types.

        +-----------------------------------+------------------------------------------+
        |             Task Type             |               Description                |
        +===================================+==========================================+
        | aws_ebs_volume_file_restore       | A restore task for a file within an EBS  |
        |                                   | volume.                                  |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_backup_seeding     | The initial backup task of an EBS Volume |
        |                                   | - future backups are incremental.        |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_incremental_backup | A scheduled incremental backup task for  |
        |                                   | an EBS volume.                           |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_backup_indexing    | A post-processing task that indexes the  |
        |                                   | contents                                 |
        |                                   | of an EBS volume in preparation for      |
        |                                   | file-level indexing and restores.        |
        |                                   | The `aws_ebs_volume_backup_indexing`     |
        |                                   | task cannot be aborted.                  |
        +-----------------------------------+------------------------------------------+
        | aws_ebs_volume_restore            | A restore task for an EBS Volume.        |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mailbox_seeding      | The initial backup task of a mailbox -   |
        |                                   | future backups are incremental.          |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mailbox_backup       | A scheduled incremental backup task for  |
        |                                   | a mailbox.                               |
        +-----------------------------------+------------------------------------------+
        | microsoft365_inventory_sync       | A task that synchronizes Clumio with the |
        |                                   | Microsoft 365 domain by gathering        |
        |                                   | mailbox information and other data, such |
        |                                   | as usage and sizing statistics.          |
        |                                   | The `microsoft365_inventory_sync` task   |
        |                                   | cannot be aborted.                       |
        +-----------------------------------+------------------------------------------+
        | microsoft365_mail_restore         | A restore task for a microsoft365        |
        |                                   | mailbox.                                 |
        +-----------------------------------+------------------------------------------+


        The following table describes the supported task statuses.

        +-------------+----------------------------------------------------------------+
        | Task Status |                          Description                           |
        +=============+================================================================+
        | queued      | A task that is waiting to begin. A task that is in queue can   |
        |             | be aborted at any time.                                        |
        +-------------+----------------------------------------------------------------+
        | in_progress | A task that is currently running. Once the task has            |
        |             | successfully completed,                                        |
        |             | the task status changes to `completed`.                        |
        |             | A task that is in progress can be aborted at any time.         |
        +-------------+----------------------------------------------------------------+
        | completed   | A task that has successfully completed.                        |
        +-------------+----------------------------------------------------------------+
        | failed      | A task that has failed to complete.                            |
        +-------------+----------------------------------------------------------------+
        | aborting    | A task that is in the process of aborting.                     |
        |             | Only tasks that are queued or in progress can be aborted.      |
        |             | Once a task has successfully aborted, the task status changes  |
        |             | to `aborted`.                                                  |
        +-------------+----------------------------------------------------------------+
        | aborted     | A task that has fully aborted.                                 |
        +-------------+----------------------------------------------------------------+

        Args:
            limit:
                Limits the size of the items returned in the response.
            start:
                Sets the page number used to browse the collection.
                Pages are indexed starting from 1 (i.e., `start=1`).
            filter:
                Narrows down the results to only the items that satisfy the filter criteria.
                The following table lists the supported filter fields for this resource and the
                operations
                that can be performed on the field:

                +----------------------+------------------+------------------------------------+
                |        Field         | Filter Condition |            Description             |
                +======================+==================+====================================+
                | primary_entity.value | $contains        | The name or value given to the     |
                |                      |                  | entity affected by the task.       |
                |                      |                  | For example, filter={"primary_enti |
                |                      |                  | ty.value":{"$contains":"ubuntu-    |
                |                      |                  | bbp-medium-01"}}                   |
                +----------------------+------------------+------------------------------------+
                | primary_entity.id    | $contains        | The unique ID given to the entity  |
                |                      |                  | affected by the task.              |
                |                      |                  | For example, filter={"primary_enti |
                |                      |                  | ty.id":{"eq":"c8011712-9e16-11eb-  |
                |                      |                  | bb8f-0a06889d7896"}}               |
                +----------------------+------------------+------------------------------------+
                | created_timestamp    | $lte, $gte       | The timestamp value of when the    |
                |                      |                  | task was started                   |
                |                      |                  | (cannot exceed the last 6 months)  |
                |                      |                  | in RFC-3999 format.                |
                |                      |                  | For example, filter={"created_time |
                |                      |                  | stamp":{"$lte":                    |
                |                      |                  | "2020-09-13T00:00:00Z"}}           |
                +----------------------+------------------+------------------------------------+
                | type                 | $in              | The task type.                     |
                |                      |                  | Examples of task types include     |
                |                      |                  | "ebs_indexing", and                |
                |                      |                  | "file_restore".                    |
                |                      |                  | Refer to the Task Type table for a |
                |                      |                  | complete list of task types.       |
                |                      |                  | For example, filter={"type":{"$in" |
                |                      |                  | :["ebs_incremental_backup"]}}      |
                +----------------------+------------------+------------------------------------+
                | category             | $in              | The task category.                 |
                |                      |                  | Examples of task categories        |
                |                      |                  | include "backup", "restore", and   |
                |                      |                  | "management".                      |
                |                      |                  | For example, filter={"category":{" |
                |                      |                  | $in":["backup"]}}                  |
                +----------------------+------------------+------------------------------------+
                | genre                | $in              | The task genre.                    |
                |                      |                  | Examples of task types include     |
                |                      |                  | "operational" and                  |
                |                      |                  | "administrative".                  |
                |                      |                  | For example, filter={"genre":{"$in |
                |                      |                  | ":["operational"]}}                |
                +----------------------+------------------+------------------------------------+
                | status               | $in              | The task status.                   |
                |                      |                  | Examples of task statuses include, |
                |                      |                  | "queued", "in_progress", and       |
                |                      |                  | "completed".                       |
                |                      |                  | Refer to the Task Status table for |
                |                      |                  | a complete list of task statuses.  |
                |                      |                  | For example, filter={"status":{"$i |
                |                      |                  | n":["completed"]}}                 |
                +----------------------+------------------+------------------------------------+
                | id                   | $in              | The Clumio-assigned ID of the      |
                |                      |                  | task. Multiple tasks can be        |
                |                      |                  | specified.                         |
                |                      |                  | For example,                       |
                |                      |                  | filter={"id":{"in":["101","114"]}} |
                +----------------------+------------------+------------------------------------+

        """
        controller = TasksV1Controller(self.controller)
        while True:
            response = controller.list_tasks(limit=limit, start=start, filter=filter, **kwargs)
            yield response
            next_link = response.Links.Next  # type: ignore
            if not next_link:
                break
            next_link = next_link.Href
            if match := re.search(r'start=([^&]+)', next_link):  # type: ignore
                start = match.group(1)
            else:
                raise clumio_exception.ClumioException(
                    'Next link is malformed. Please contact clumio support.'
                )
