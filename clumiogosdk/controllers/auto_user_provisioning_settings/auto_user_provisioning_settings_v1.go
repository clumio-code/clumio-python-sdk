// Copyright (c) 2021 Clumio All Rights Reserved

// Package autouserprovisioningsettings contains methods related to AutoUserProvisioningSettings
package autouserprovisioningsettings

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AutoUserProvisioningSettingsV1 represents a custom type struct
type AutoUserProvisioningSettingsV1 struct {
    config config.Config
}

// ReadAutoUserProvisioningSetting Returns a representation of the auto user provisioning settings.
func (a *AutoUserProvisioningSettingsV1) ReadAutoUserProvisioningSetting()(
    *models.ReadAutoUserProvisioningSettingResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/settings/auto-user-provisioning"

    
    header := "application/api.clumio.auto-user-provisioning-settings=v1+json"
    var result *models.ReadAutoUserProvisioningSettingResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateAutoUserProvisioningSetting Update the auto user provisioning settings.
func (a *AutoUserProvisioningSettingsV1) UpdateAutoUserProvisioningSetting(
    body *models.UpdateAutoUserProvisioningSettingV1Request)(
    *models.UpdateAutoUserProvisioningSettingResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/settings/auto-user-provisioning"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.auto-user-provisioning-settings=v1+json"
    var result *models.UpdateAutoUserProvisioningSettingResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}
