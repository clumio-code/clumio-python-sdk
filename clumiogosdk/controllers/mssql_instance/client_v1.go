// Copyright (c) 2021 Clumio All Rights Reserved

package mssqlinstance

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlInstanceV1Client represents a custom type interface
type MssqlInstanceV1Client interface {
    // ListMssqlInstance Returns a list of Instances
    ListMssqlInstance(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListMssqlInstancesResponse,  *apiutils.APIError)
    
    // ReadMssqlInstance Returns a representation of the specified instance.
    ReadMssqlInstance(
        instanceId string)(
        *models.ReadMssqlInstanceResponse,  *apiutils.APIError)
    
}

// NewMssqlInstanceV1 returns MssqlInstanceV1Client
func NewMssqlInstanceV1(config config.Config) MssqlInstanceV1Client {
    client := new(MssqlInstanceV1)
    client.config = config
    return client
}
