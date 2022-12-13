// Copyright (c) 2021 Clumio All Rights Reserved

// Package backupawsebsvolumes contains methods related to BackupAwsEbsVolumes
package backupawsebsvolumes

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupAwsEbsVolumesV1 represents a custom type struct
type BackupAwsEbsVolumesV1 struct {
    config config.Config
}

// ListBackupAwsEbsVolumes Returns a list of EBS volumes that have been backed up by Clumio. EBS volume backups can be restored through the [POST /restores/aws/ebs-volumes](#operation/restore-aws-ebs-volume) endpoint.
func (b *BackupAwsEbsVolumesV1) ListBackupAwsEbsVolumes(
    limit *int64, 
    start *string, 
    sort *string, 
    filter *string)(
    *models.ListEBSBackupsResponseV1, *apiutils.APIError) {

    queryBuilder := b.config.BaseUrl + "/backups/aws/ebs-volumes"

    
    header := "application/api.clumio.backup-aws-ebs-volumes=v1+json"
    var result *models.ListEBSBackupsResponseV1
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
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "sort": *sort,
        "filter": *filter,
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


// CreateBackupAwsEbsVolume Performs an on-demand backup for the specified EBS volume.
func (b *BackupAwsEbsVolumesV1) CreateBackupAwsEbsVolume(
    body models.CreateBackupAwsEbsVolumeV1Request)(
    interface{}, *apiutils.APIError) {

    queryBuilder := b.config.BaseUrl + "/backups/aws/ebs-volumes"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.backup-aws-ebs-volumes=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadBackupAwsEbsVolume Returns a representation of the specified EBS volume backup.
func (b *BackupAwsEbsVolumesV1) ReadBackupAwsEbsVolume(
    backupId string)(
    *models.ReadEBSBackupResponseV1, *apiutils.APIError) {

    pathURL := "/backups/aws/ebs-volumes/{backup_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "backup_id": backupId,
    }
    queryBuilder := b.config.BaseUrl + pathURL

    
    header := "application/api.clumio.backup-aws-ebs-volumes=v1+json"
    var result *models.ReadEBSBackupResponseV1

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
