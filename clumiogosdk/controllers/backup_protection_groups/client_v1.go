// Copyright (c) 2021 Clumio All Rights Reserved

package backupprotectiongroups

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupProtectionGroupsV1Client represents a custom type interface
type BackupProtectionGroupsV1Client interface {
    // ListBackupProtectionGroups Retrieves a list of protection group backups.
    ListBackupProtectionGroups(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string)(
        *models.ListProtectionGroupBackupsResponse,  *apiutils.APIError)
    
    // ListBackupProtectionGroupS3Assets Retrieves a list of protection group S3 asset backups.
    ListBackupProtectionGroupS3Assets(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string)(
        *models.ListProtectionGroupS3AssetBackupsResponse,  *apiutils.APIError)
    
    // ReadBackupProtectionGroupS3Asset Returns a representation of the specified protection group S3 asset backup.
    ReadBackupProtectionGroupS3Asset(
        backupId string)(
        *models.ReadProtectionGroupS3AssetBackupResponse,  *apiutils.APIError)
    
    // ReadBackupProtectionGroup Returns a representation of the specified protection group backup.
    ReadBackupProtectionGroup(
        backupId string)(
        *models.ReadProtectionGroupBackupResponse,  *apiutils.APIError)
    
}

// NewBackupProtectionGroupsV1 returns BackupProtectionGroupsV1Client
func NewBackupProtectionGroupsV1(config config.Config) BackupProtectionGroupsV1Client {
    client := new(BackupProtectionGroupsV1)
    client.config = config
    return client
}
