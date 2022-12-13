// Copyright (c) 2021 Clumio All Rights Reserved

package backupawsdynamodbtables

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupAwsDynamodbTablesV1Client represents a custom type interface
type BackupAwsDynamodbTablesV1Client interface {
    // ListBackupAwsDynamodbTables Retrieves a list of DynamoDB table backups.
    ListBackupAwsDynamodbTables(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string)(
        *models.ListDynamoDBTableBackupsResponse,  *apiutils.APIError)
    
    // CreateBackupAwsDynamodbTable Performs an on-demand backup for the specified DynamoDB table.
    CreateBackupAwsDynamodbTable(
        embed *string, 
        body models.CreateBackupAwsDynamodbTableV1Request)(
        *models.OnDemandDynamoDBBackupResponse,  *apiutils.APIError)
    
    // ReadBackupAwsDynamodbTable Returns a representation of the specified DynamoDB table backup.
    ReadBackupAwsDynamodbTable(
        backupId string)(
        *models.ReadDynamoDBTableBackupResponse,  *apiutils.APIError)
    
}

// NewBackupAwsDynamodbTablesV1 returns BackupAwsDynamodbTablesV1Client
func NewBackupAwsDynamodbTablesV1(config config.Config) BackupAwsDynamodbTablesV1Client {
    client := new(BackupAwsDynamodbTablesV1)
    client.config = config
    return client
}
