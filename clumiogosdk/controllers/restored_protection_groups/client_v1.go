// Copyright (c) 2021 Clumio All Rights Reserved

package restoredprotectiongroups

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredProtectionGroupsV1Client represents a custom type interface
type RestoredProtectionGroupsV1Client interface {
    // RestoreProtectionGroup Restores the specified protection group backup to the specified target destination.
    RestoreProtectionGroup(
        embed *string, 
        body models.RestoreProtectionGroupV1Request)(
        *models.RestoreProtectionGroupResponse,  *apiutils.APIError)
    
}

// NewRestoredProtectionGroupsV1 returns RestoredProtectionGroupsV1Client
func NewRestoredProtectionGroupsV1(config config.Config) RestoredProtectionGroupsV1Client {
    client := new(RestoredProtectionGroupsV1)
    client.config = config
    return client
}
