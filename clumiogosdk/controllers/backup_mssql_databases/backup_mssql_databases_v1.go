// Copyright (c) 2021 Clumio All Rights Reserved

// Package backupmssqldatabases contains methods related to BackupMssqlDatabases
package backupmssqldatabases

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupMssqlDatabasesV1 represents a custom type struct
type BackupMssqlDatabasesV1 struct {
    config config.Config
}

// ListBackupMssqlDatabases Retrieve a list of MSSQL database backups.
func (b *BackupMssqlDatabasesV1) ListBackupMssqlDatabases(
    limit *int64, 
    start *string, 
    sort *string, 
    filter *string, 
    embed *string)(
    *models.ListMssqlDatabaseBackupsResponse, *apiutils.APIError) {

    queryBuilder := b.config.BaseUrl + "/backups/mssql/databases"

    
    header := "application/api.clumio.backup-mssql-databases=v1+json"
    var result *models.ListMssqlDatabaseBackupsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if sort == nil {
        sort = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "sort": *sort,
        "filter": *filter,
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateBackupMssqlDatabase Performs an on-demand backup for the specified MSSQL asset.
func (b *BackupMssqlDatabasesV1) CreateBackupMssqlDatabase(
    embed *string, 
    body models.CreateBackupMssqlDatabaseV1Request)(
    *models.OnDemandMssqlBackupResponse, *apiutils.APIError) {

    queryBuilder := b.config.BaseUrl + "/backups/mssql/databases"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.backup-mssql-databases=v1+json"
    var result *models.OnDemandMssqlBackupResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadBackupMssqlDatabase Returns a representation of the specified MSSQL database backup.
func (b *BackupMssqlDatabasesV1) ReadBackupMssqlDatabase(
    backupId string)(
    *models.ReadMssqlDatabaseBackupResponse, *apiutils.APIError) {

    pathURL := "/backups/mssql/databases/{backup_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "backup_id": backupId,
    }
    queryBuilder := b.config.BaseUrl + pathURL

    
    header := "application/api.clumio.backup-mssql-databases=v1+json"
    var result *models.ReadMssqlDatabaseBackupResponse

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
