// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredawsebsvolumes contains methods related to RestoredAwsEbsVolumes
package restoredawsebsvolumes

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsEbsVolumesV2 represents a custom type struct
type RestoredAwsEbsVolumesV2 struct {
    config config.Config
}

// RestoreAwsEbsVolume Restores the specified source EBS volume backup to the specified target destination. The source EBS volume must be one that was backup up by Clumio.
func (r *RestoredAwsEbsVolumesV2) RestoreAwsEbsVolume(
    embed *string, 
    body models.RestoreAwsEbsVolumeV2Request)(
    *models.RestoreEBSResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/aws/ebs-volumes"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-aws-ebs-volumes=v2+json"
    var result *models.RestoreEBSResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
