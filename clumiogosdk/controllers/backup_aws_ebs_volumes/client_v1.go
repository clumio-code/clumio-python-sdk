// Copyright (c) 2021 Clumio All Rights Reserved

package backupawsebsvolumes

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupAwsEbsVolumesV1Client represents a custom type interface
type BackupAwsEbsVolumesV1Client interface {
    // ListBackupAwsEbsVolumes Returns a list of EBS volumes that have been backed up by Clumio. EBS volume backups can be restored through the [POST /restores/aws/ebs-volumes](#operation/restore-aws-ebs-volume) endpoint.
    ListBackupAwsEbsVolumes(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string)(
        *models.ListEBSBackupsResponseV1,  *apiutils.APIError)
    
    // CreateBackupAwsEbsVolume Performs an on-demand backup for the specified EBS volume.
    CreateBackupAwsEbsVolume(
        body models.CreateBackupAwsEbsVolumeV1Request)(
        interface{},  *apiutils.APIError)
    
    // ReadBackupAwsEbsVolume Returns a representation of the specified EBS volume backup.
    ReadBackupAwsEbsVolume(
        backupId string)(
        *models.ReadEBSBackupResponseV1,  *apiutils.APIError)
    
}

// NewBackupAwsEbsVolumesV1 returns BackupAwsEbsVolumesV1Client
func NewBackupAwsEbsVolumesV1(config config.Config) BackupAwsEbsVolumesV1Client {
    client := new(BackupAwsEbsVolumesV1)
    client.config = config
    return client
}
