// Copyright (c) 2021 Clumio All Rights Reserved

// Package awsebsvolumes contains methods related to AwsEbsVolumes
package awsebsvolumes

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsEbsVolumesV1 represents a custom type struct
type AwsEbsVolumesV1 struct {
    config config.Config
}

// ListAwsEbsVolumes Returns a list of EBS volumes.
func (a *AwsEbsVolumesV1) ListAwsEbsVolumes(
    limit *int64, 
    start *string, 
    filter *string, 
    embed *string)(
    *models.ListEbsVolumesResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/datasources/aws/ebs-volumes"

    
    header := "application/api.clumio.aws-ebs-volumes=v1+json"
    var result *models.ListEbsVolumesResponse
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
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadAwsEbsVolume Returns a representation of the specified EBS volume.
func (a *AwsEbsVolumesV1) ReadAwsEbsVolume(
    volumeId string, 
    embed *string)(
    *models.ReadEbsVolumeResponse, *apiutils.APIError) {

    pathURL := "/datasources/aws/ebs-volumes/{volume_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "volume_id": volumeId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.aws-ebs-volumes=v1+json"
    var result *models.ReadEbsVolumeResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
