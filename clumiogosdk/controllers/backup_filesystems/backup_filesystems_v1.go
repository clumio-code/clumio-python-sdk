// Copyright (c) 2021 Clumio All Rights Reserved

// Package backupfilesystems contains methods related to BackupFilesystems
package backupfilesystems

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupFilesystemsV1 represents a custom type struct
type BackupFilesystemsV1 struct {
    config config.Config
}

// ListBackupFilesystems Returns a list of filesystems.
func (b *BackupFilesystemsV1) ListBackupFilesystems(
    backupId string, 
    limit *int64, 
    start *string)(
    *models.ListFileSystemsResponse, *apiutils.APIError) {

    pathURL := "/backups/{backup_id}/filesystems"
    //process optional template parameters
    pathParams := map[string]string{
        "backup_id": backupId,
    }
    queryBuilder := b.config.BaseUrl + pathURL

    
    header := "application/api.clumio.backup-filesystems=v1+json"
    var result *models.ListFileSystemsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadFilesystem Returns a representation of the specified filesystem.
func (b *BackupFilesystemsV1) ReadFilesystem(
    filesystemId string, 
    backupId string)(
    *models.ReadFileSystemResponse, *apiutils.APIError) {

    pathURL := "/backups/{backup_id}/filesystems/{filesystem_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "filesystem_id": filesystemId,
        "backup_id": backupId,
    }
    queryBuilder := b.config.BaseUrl + pathURL

    
    header := "application/api.clumio.backup-filesystems=v1+json"
    var result *models.ReadFileSystemResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
