// Copyright (c) 2021 Clumio All Rights Reserved

package autouserprovisioningsettings

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AutoUserProvisioningSettingsV1Client represents a custom type interface
type AutoUserProvisioningSettingsV1Client interface {
    // ReadAutoUserProvisioningSetting Returns a representation of the auto user provisioning settings.
    ReadAutoUserProvisioningSetting()(
        *models.ReadAutoUserProvisioningSettingResponse,  *apiutils.APIError)
    
    // UpdateAutoUserProvisioningSetting Update the auto user provisioning settings.
    UpdateAutoUserProvisioningSetting(
        body *models.UpdateAutoUserProvisioningSettingV1Request)(
        *models.UpdateAutoUserProvisioningSettingResponse,  *apiutils.APIError)
    
}

// NewAutoUserProvisioningSettingsV1 returns AutoUserProvisioningSettingsV1Client
func NewAutoUserProvisioningSettingsV1(config config.Config) AutoUserProvisioningSettingsV1Client {
    client := new(AutoUserProvisioningSettingsV1)
    client.config = config
    return client
}
