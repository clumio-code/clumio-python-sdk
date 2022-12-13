// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentervms

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterVmsV1Client represents a custom type interface
type VmwareVcenterVmsV1Client interface {
    // ListVmwareVcenterVms Returns a list of VMs in the specified vCenter server.
    ListVmwareVcenterVms(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListVmsResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterVm Returns a representation of the specified VM.
    ReadVmwareVcenterVm(
        vcenterId string, 
        vmId string, 
        embed *string)(
        *models.ReadVmResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterVmsV1 returns VmwareVcenterVmsV1Client
func NewVmwareVcenterVmsV1(config config.Config) VmwareVcenterVmsV1Client {
    client := new(VmwareVcenterVmsV1)
    client.config = config
    return client
}
