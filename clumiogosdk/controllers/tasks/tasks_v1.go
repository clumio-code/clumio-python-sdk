// Copyright (c) 2021 Clumio All Rights Reserved

// Package tasks contains methods related to Tasks
package tasks

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// TasksV1 represents a custom type struct
type TasksV1 struct {
    config config.Config
}

// ListTasks Returns a list of tasks. Tasks include scheduled backup and on-demand restore related tasks.
//  
//  The following table describes the supported task types.
//  
//  +-----------------------------------+------------------------------------------+
//  |             Task Type             |               Description                |
//  +===================================+==========================================+
//  | vmware_vm_file_restore            | A restore task for a file within a VM.   |
//  +-----------------------------------+------------------------------------------+
//  | vmware_vm_backup_seeding          | The initial backup task of a VM - future |
//  |                                   | backups are incremental.                 |
//  +-----------------------------------+------------------------------------------+
//  | vmware_vm_incremental_backup      | A scheduled incremental backup task for  |
//  |                                   | a VM.                                    |
//  +-----------------------------------+------------------------------------------+
//  | vmware_vm_backup_indexing         | A post-processing task that indexes the  |
//  |                                   | contents                                 |
//  |                                   | of a VM disk in preparation for file-    |
//  |                                   | level indexing and restores.             |
//  |                                   | The vmware_vm_backup_indexing task       |
//  |                                   | cannot be aborted.                       |
//  +-----------------------------------+------------------------------------------+
//  | vmware_vm_restore                 | A restore task for a VM.                 |
//  +-----------------------------------+------------------------------------------+
//  | aws_ebs_volume_file_restore       | A restore task for a file within an EBS  |
//  |                                   | volume.                                  |
//  +-----------------------------------+------------------------------------------+
//  | aws_ebs_volume_backup_seeding     | The initial backup task of an EBS Volume |
//  |                                   | - future backups are incremental.        |
//  +-----------------------------------+------------------------------------------+
//  | aws_ebs_volume_incremental_backup | A scheduled incremental backup task for  |
//  |                                   | an EBS volume.                           |
//  +-----------------------------------+------------------------------------------+
//  | aws_ebs_volume_backup_indexing    | A post-processing task that indexes the  |
//  |                                   | contents                                 |
//  |                                   | of an EBS volume in preparation for      |
//  |                                   | file-level indexing and restores.        |
//  |                                   | The aws_ebs_volume_backup_indexing task  |
//  |                                   | cannot be aborted.                       |
//  +-----------------------------------+------------------------------------------+
//  | aws_ebs_volume_restore            | A restore task for an EBS Volume.        |
//  +-----------------------------------+------------------------------------------+
//  | microsoft365_mailbox_seeding      | The initial backup task of a mailbox -   |
//  |                                   | future backups are incremental.          |
//  +-----------------------------------+------------------------------------------+
//  | microsoft365_mailbox_backup       | A scheduled incremental backup task for  |
//  |                                   | a mailbox.                               |
//  +-----------------------------------+------------------------------------------+
//  | microsoft365_inventory_sync       | A task that synchronizes Clumio with the |
//  |                                   | Microsoft 365 domain by gathering        |
//  |                                   | mailbox information and other data, such |
//  |                                   | as usage and sizing statistics.          |
//  |                                   | The microsoft365_inventory_sync task     |
//  |                                   | cannot be aborted.                       |
//  +-----------------------------------+------------------------------------------+
//  | microsoft365_mail_restore         | A restore task for a microsoft365        |
//  |                                   | mailbox.                                 |
//  +-----------------------------------+------------------------------------------+
//  
//  
//  The following table describes the supported task statuses.
//  
//  +-------------+----------------------------------------------------------------+
//  | Task Status |                          Description                           |
//  +=============+================================================================+
//  | queued      | A task that is waiting to begin. A task that is in queue can   |
//  |             | be aborted at any time.                                        |
//  +-------------+----------------------------------------------------------------+
//  | in_progress | A task that is currently running. Once the task has            |
//  |             | successfully completed,                                        |
//  |             | the task status changes to completed.                          |
//  |             | A task that is in progress can be aborted at any time.         |
//  +-------------+----------------------------------------------------------------+
//  | completed   | A task that has successfully completed.                        |
//  +-------------+----------------------------------------------------------------+
//  | failed      | A task that has failed to complete.                            |
//  +-------------+----------------------------------------------------------------+
//  | aborting    | A task that is in the process of aborting.                     |
//  |             | Only tasks that are queued or in progress can be aborted.      |
//  |             | Once a task has successfully aborted, the task status changes  |
//  |             | to aborted.                                                    |
//  +-------------+----------------------------------------------------------------+
//  | aborted     | A task that has fully aborted.                                 |
//  +-------------+----------------------------------------------------------------+
//  
func (t *TasksV1) ListTasks(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListTasksResponse, *apiutils.APIError) {

    queryBuilder := t.config.BaseUrl + "/tasks"

    
    header := "application/api.clumio.tasks=v1+json"
    var result *models.ListTasksResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: t.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadTask Returns a representation of the specified task.
func (t *TasksV1) ReadTask(
    taskId string)(
    *models.ReadTaskResponse, *apiutils.APIError) {

    pathURL := "/tasks/{task_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "task_id": taskId,
    }
    queryBuilder := t.config.BaseUrl + pathURL

    
    header := "application/api.clumio.tasks=v1+json"
    var result *models.ReadTaskResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: t.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateTask Manages the specified task. Managing a task includes aborting a task that is in queue or in progress.
func (t *TasksV1) UpdateTask(
    taskId string, 
    body *models.UpdateTaskV1Request)(
    *models.UpdateTaskResponse, *apiutils.APIError) {

    pathURL := "/tasks/{task_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "task_id": taskId,
    }
    queryBuilder := t.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.tasks=v1+json"
    var result *models.UpdateTaskResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: t.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
