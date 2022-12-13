// Copyright (c) 2021 Clumio All Rights Reserved

package restoredawsec2instances

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsEc2InstancesV1Client represents a custom type interface
type RestoredAwsEc2InstancesV1Client interface {
    // RestoreAwsEc2Instance Restores the specified EC2 instance backup to the specified target destination.
    RestoreAwsEc2Instance(
        embed *string, 
        body models.RestoreAwsEc2InstanceV1Request)(
        *models.RestoreEC2Response,  *apiutils.APIError)
    
}

// NewRestoredAwsEc2InstancesV1 returns RestoredAwsEc2InstancesV1Client
func NewRestoredAwsEc2InstancesV1(config config.Config) RestoredAwsEc2InstancesV1Client {
    client := new(RestoredAwsEc2InstancesV1)
    client.config = config
    return client
}
