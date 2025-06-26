#
# Copyright 2023. Clumio, A Commvault Company.
#

import json
from typing import Optional, Union

from clumioapi import api_helper
from clumioapi import configuration
from clumioapi import sdk_version
from clumioapi.controllers import base_controller
from clumioapi.exceptions import clumio_exception
from clumioapi.models import list_tasks_response
from clumioapi.models import read_task_response
from clumioapi.models import update_task_response
from clumioapi.models import update_task_v1_request
import requests


class TasksV1Controller(base_controller.BaseController):
    """A Controller to access Endpoints for tasks resource."""

    def __init__(self, config: configuration.Configuration) -> None:
        super().__init__(config)
        self.config = config
        self.headers = {
            'accept': 'application/api.clumio.tasks=v1+json',
            'x-clumio-organizationalunit-context': self.config.organizational_unit_context,
            'x-clumio-api-client': 'clumio-python-sdk',
            'x-clumio-sdk-version': f'clumio-python-sdk:{sdk_version}',
        }
        if config.custom_headers != None:
            self.headers.update(config.custom_headers)

    def list_tasks(
        self, limit: int = None, start: str = None, filter: str = None, **kwargs
    ) -> Union[
        list_tasks_response.ListTasksResponse,
        tuple[requests.Response, Optional[list_tasks_response.ListTasksResponse]],
    ]:
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
                Limits the size of the response on each page to the specified number of items.
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

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            list_tasks_response.ListTasksResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/tasks'

        _query_parameters = {}
        _query_parameters = {'limit': limit, 'start': start, 'filter': filter}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing list_tasks.', errors
            )

        if self.config.raw_response:
            return resp, list_tasks_response.ListTasksResponse.from_dictionary(resp.json())
        return list_tasks_response.ListTasksResponse.from_dictionary(resp)

    def read_task(self, task_id: str, **kwargs) -> Union[
        read_task_response.ReadTaskResponse,
        tuple[requests.Response, Optional[read_task_response.ReadTaskResponse]],
    ]:
        """Returns a representation of the specified task.

        Args:
            task_id:
                Performs the operation on the task with the specified ID.
        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            read_task_response.ReadTaskResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/tasks/{task_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'task_id': task_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.get(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing read_task.', errors
            )

        if self.config.raw_response:
            return resp, read_task_response.ReadTaskResponse.from_dictionary(resp.json())
        return read_task_response.ReadTaskResponse.from_dictionary(resp)

    def update_task(
        self, task_id: str, body: update_task_v1_request.UpdateTaskV1Request = None, **kwargs
    ) -> Union[
        update_task_response.UpdateTaskResponse,
        tuple[requests.Response, Optional[update_task_response.UpdateTaskResponse]],
    ]:
        """Manages the specified task. Managing a task includes aborting a task that is in
        queue or in progress.

        Args:
            task_id:
                Performs the operation on the task with the specified ID.
            body:

        Returns:
            requests.Response: Raw Response from the API if config.raw_response is set to True.
            update_task_response.UpdateTaskResponse: Response from the API.
        Raises:
            ClumioException: An error occured while executing the API.
                This exception includes the HTTP response code, an error
                message, and the HTTP body that was received in the request.
        """

        # Prepare query URL
        _url_path = '/tasks/{task_id}'
        _url_path = api_helper.append_url_with_template_parameters(_url_path, {'task_id': task_id})
        _query_parameters = {}

        # Execute request
        try:
            resp = self.client.patch(
                _url_path,
                headers=self.headers,
                params=_query_parameters,
                json=api_helper.to_dictionary(body),
                raw_response=self.config.raw_response,
                **kwargs,
            )
        except requests.exceptions.HTTPError as http_error:
            if self.config.raw_response:
                return http_error.response, None
            errors = self.client.get_error_message(http_error.response)
            raise clumio_exception.ClumioException(
                'Error occurred while executing update_task.', errors
            )

        if self.config.raw_response:
            return resp, update_task_response.UpdateTaskResponse.from_dictionary(resp.json())
        return update_task_response.UpdateTaskResponse.from_dictionary(resp)
