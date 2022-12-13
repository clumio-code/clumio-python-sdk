// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredprotectiongroups contains methods related to RestoredProtectionGroups
package restoredprotectiongroups

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredProtectionGroupsV1 represents a custom type struct
type RestoredProtectionGroupsV1 struct {
    config config.Config
}

// RestoreProtectionGroup Restores the specified protection group backup to the specified target destination.
func (r *RestoredProtectionGroupsV1) RestoreProtectionGroup(
    embed *string, 
    body models.RestoreProtectionGroupV1Request)(
    *models.RestoreProtectionGroupResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/protection-groups"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-protection-groups=v1+json"
    var result *models.RestoreProtectionGroupResponse
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
