// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredawsrdsresources contains methods related to RestoredAwsRdsResources
package restoredawsrdsresources

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsRdsResourcesV1 represents a custom type struct
type RestoredAwsRdsResourcesV1 struct {
    config config.Config
}

// RestoreAwsRdsResource Restores the specified RDS resource backup or snapshot to the specified target destination.
func (r *RestoredAwsRdsResourcesV1) RestoreAwsRdsResource(
    embed *string, 
    body models.RestoreAwsRdsResourceV1Request)(
    *models.CreateRdsResourceRestoreResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/aws/rds-resources"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-aws-rds-resources=v1+json"
    var result *models.CreateRdsResourceRestoreResponse
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
