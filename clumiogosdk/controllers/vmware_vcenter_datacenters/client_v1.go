// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcenterdatacenters

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterDatacentersV1Client represents a custom type interface
type VmwareVcenterDatacentersV1Client interface {
    // ListVmwareVcenterDatacenters Returns a list of VMware data centers in the specified vCenter server.
    ListVmwareVcenterDatacenters(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string, 
        Embed *string)(
        *models.ListDatacentersResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterDatacenter Returns a representation of the specified VMware data center within the specified vCenter server.
    ReadVmwareVcenterDatacenter(
        vcenterId string, 
        datacenterId string, 
        embed *string)(
        *models.ReadDatacenterResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterDatacentersV1 returns VmwareVcenterDatacentersV1Client
func NewVmwareVcenterDatacentersV1(config config.Config) VmwareVcenterDatacentersV1Client {
    client := new(VmwareVcenterDatacentersV1)
    client.config = config
    return client
}
