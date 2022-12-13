// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcenterhosts

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterHostsV1Client represents a custom type interface
type VmwareVcenterHostsV1Client interface {
    // ListVmwareVcenterHosts Returns a list of hosts in the specified vCenter server.
    ListVmwareVcenterHosts(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListHostsResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterHost Returns a representation of the specified host.
    ReadVmwareVcenterHost(
        vcenterId string, 
        hostId string)(
        *models.ReadHostResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterHostsV1 returns VmwareVcenterHostsV1Client
func NewVmwareVcenterHostsV1(config config.Config) VmwareVcenterHostsV1Client {
    client := new(VmwareVcenterHostsV1)
    client.config = config
    return client
}
