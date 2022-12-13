// Copyright (c) 2021 Clumio All Rights Reserved

package generalsettings

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// GeneralSettingsV2Client represents a custom type interface
type GeneralSettingsV2Client interface {
    // ReadGeneralSettings Retrieves organization-wide setting details, including password and security settings.
    ReadGeneralSettings()(
        *models.ReadGeneralSettingsResponseV2,  *apiutils.APIError)
    
    // UpdateGeneralSettings Updates organization-wide settings, including password and security settings.
    UpdateGeneralSettings(
        body *models.UpdateGeneralSettingsV2Request)(
        *models.PatchGeneralSettingsResponseV2,  *apiutils.APIError)
    
}

// NewGeneralSettingsV2 returns GeneralSettingsV2Client
func NewGeneralSettingsV2(config config.Config) GeneralSettingsV2Client {
    client := new(GeneralSettingsV2)
    client.config = config
    return client
}
