// Copyright (c) 2021 Clumio All Rights Reserved

// Package generalsettings contains methods related to GeneralSettings
package generalsettings

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// GeneralSettingsV2 represents a custom type struct
type GeneralSettingsV2 struct {
    config config.Config
}

// ReadGeneralSettings Retrieves organization-wide setting details, including password and security settings.
func (g *GeneralSettingsV2) ReadGeneralSettings()(
    *models.ReadGeneralSettingsResponseV2, *apiutils.APIError) {

    queryBuilder := g.config.BaseUrl + "/settings/general"

    
    header := "application/api.clumio.general-settings=v2+json"
    var result *models.ReadGeneralSettingsResponseV2

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: g.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateGeneralSettings Updates organization-wide settings, including password and security settings.
func (g *GeneralSettingsV2) UpdateGeneralSettings(
    body *models.UpdateGeneralSettingsV2Request)(
    *models.PatchGeneralSettingsResponseV2, *apiutils.APIError) {

    queryBuilder := g.config.BaseUrl + "/settings/general"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.general-settings=v2+json"
    var result *models.PatchGeneralSettingsResponseV2

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: g.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
