// Copyright (c) 2021 Clumio All Rights Reserved

package restoredawsrdsresources

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsRdsResourcesV1Client represents a custom type interface
type RestoredAwsRdsResourcesV1Client interface {
    // RestoreAwsRdsResource Restores the specified RDS resource backup or snapshot to the specified target destination.
    RestoreAwsRdsResource(
        embed *string, 
        body models.RestoreAwsRdsResourceV1Request)(
        *models.CreateRdsResourceRestoreResponse,  *apiutils.APIError)
    
}

// NewRestoredAwsRdsResourcesV1 returns RestoredAwsRdsResourcesV1Client
func NewRestoredAwsRdsResourcesV1(config config.Config) RestoredAwsRdsResourcesV1Client {
    client := new(RestoredAwsRdsResourcesV1)
    client.config = config
    return client
}
