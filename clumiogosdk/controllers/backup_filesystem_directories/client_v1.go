// Copyright (c) 2021 Clumio All Rights Reserved

package backupfilesystemdirectories

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupFilesystemDirectoriesV1Client represents a custom type interface
type BackupFilesystemDirectoriesV1Client interface {
    // ReadBackupFilesystemDirectory Browse files in the directory with the specified ID.
    ReadBackupFilesystemDirectory(
        backupId string, 
        filesystemId string, 
        directoryId string, 
        limit *int64, 
        start *string)(
        *models.ReadDirectoryResponse,  *apiutils.APIError)
    
}

// NewBackupFilesystemDirectoriesV1 returns BackupFilesystemDirectoriesV1Client
func NewBackupFilesystemDirectoriesV1(config config.Config) BackupFilesystemDirectoriesV1Client {
    client := new(BackupFilesystemDirectoriesV1)
    client.config = config
    return client
}
