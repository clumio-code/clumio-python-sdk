// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredprotectiongroups3assets contains methods related to RestoredProtectionGroupS3Assets
package restoredprotectiongroups3assets

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredProtectionGroupS3AssetsV1 represents a custom type struct
type RestoredProtectionGroupS3AssetsV1 struct {
    config config.Config
}

// RestoreProtectionGroupS3Asset Restores the specified protection group S3 asset backup to the specified target destination.
func (r *RestoredProtectionGroupS3AssetsV1) RestoreProtectionGroupS3Asset(
    embed *string, 
    body models.RestoreProtectionGroupS3AssetV1Request)(
    *models.RestoreProtectionGroupS3AssetResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/protection-groups/s3-assets"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-protection-group-s3-assets=v1+json"
    var result *models.RestoreProtectionGroupS3AssetResponse
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
