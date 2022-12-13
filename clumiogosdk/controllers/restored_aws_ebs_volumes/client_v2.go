// Copyright (c) 2021 Clumio All Rights Reserved

package restoredawsebsvolumes

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsEbsVolumesV2Client represents a custom type interface
type RestoredAwsEbsVolumesV2Client interface {
    // RestoreAwsEbsVolume Restores the specified source EBS volume backup to the specified target destination. The source EBS volume must be one that was backup up by Clumio.
    RestoreAwsEbsVolume(
        embed *string, 
        body models.RestoreAwsEbsVolumeV2Request)(
        *models.RestoreEBSResponse,  *apiutils.APIError)
    
}

// NewRestoredAwsEbsVolumesV2 returns RestoredAwsEbsVolumesV2Client
func NewRestoredAwsEbsVolumesV2(config config.Config) RestoredAwsEbsVolumesV2Client {
    client := new(RestoredAwsEbsVolumesV2)
    client.config = config
    return client
}
