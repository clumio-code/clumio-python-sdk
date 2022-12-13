// Copyright (c) 2021 Clumio All Rights Reserved

package backupmssqldatabases

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupMssqlDatabasesV1Client represents a custom type interface
type BackupMssqlDatabasesV1Client interface {
    // ListBackupMssqlDatabases Retrieve a list of MSSQL database backups.
    ListBackupMssqlDatabases(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string, 
        embed *string)(
        *models.ListMssqlDatabaseBackupsResponse,  *apiutils.APIError)
    
    // CreateBackupMssqlDatabase Performs an on-demand backup for the specified MSSQL asset.
    CreateBackupMssqlDatabase(
        embed *string, 
        body models.CreateBackupMssqlDatabaseV1Request)(
        *models.OnDemandMssqlBackupResponse,  *apiutils.APIError)
    
    // ReadBackupMssqlDatabase Returns a representation of the specified MSSQL database backup.
    ReadBackupMssqlDatabase(
        backupId string)(
        *models.ReadMssqlDatabaseBackupResponse,  *apiutils.APIError)
    
}

// NewBackupMssqlDatabasesV1 returns BackupMssqlDatabasesV1Client
func NewBackupMssqlDatabasesV1(config config.Config) BackupMssqlDatabasesV1Client {
    client := new(BackupMssqlDatabasesV1)
    client.config = config
    return client
}
