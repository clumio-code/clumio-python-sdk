// Copyright (c) 2021 Clumio All Rights Reserved

package restoredawsebsvolumes

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsEbsVolumesV1Client represents a custom type interface
type RestoredAwsEbsVolumesV1Client interface {
    // RestoreAwsEbsVolume Restores the specified source EBS volume backup to the specified target destination. The source EBS volume must be one that was backup up by Clumio.
    RestoreAwsEbsVolume(
        body models.RestoreAwsEbsVolumeV1Request)(
        interface{},  *apiutils.APIError)
    
}

// NewRestoredAwsEbsVolumesV1 returns RestoredAwsEbsVolumesV1Client
func NewRestoredAwsEbsVolumesV1(config config.Config) RestoredAwsEbsVolumesV1Client {
    client := new(RestoredAwsEbsVolumesV1)
    client.config = config
    return client
}
