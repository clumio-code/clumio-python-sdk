// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcenternetworks

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterNetworksV1Client represents a custom type interface
type VmwareVcenterNetworksV1Client interface {
    // ListVmwareVcenterNetworks Returns a list of networks in the specified vCenter server.
    ListVmwareVcenterNetworks(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListVMwareVCenterNetworksResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterNetwork Returns a representation of the specified network.
    ReadVmwareVcenterNetwork(
        vcenterId string, 
        networkId string)(
        *models.ReadVMwareVCenterNetworkResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterNetworksV1 returns VmwareVcenterNetworksV1Client
func NewVmwareVcenterNetworksV1(config config.Config) VmwareVcenterNetworksV1Client {
    client := new(VmwareVcenterNetworksV1)
    client.config = config
    return client
}
