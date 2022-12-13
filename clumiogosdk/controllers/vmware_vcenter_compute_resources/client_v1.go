// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentercomputeresources

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComputeResourcesV1Client represents a custom type interface
type VmwareVcenterComputeResourcesV1Client interface {
    // ListVmwareVcenterComputeResources Returns a list of VMware compute resources in the specified vCenter server.
    //  
    //  The following table lists the supported Clumio protection statuses:
    //  
    //  
    //  +-------------------+-------------------------------------------------------+
    //  | Protection Status |                        Values                         |
    //  +===================+=======================================================+
    //  | protected         | A compute resource that is protected by a policy.     |
    //  +-------------------+-------------------------------------------------------+
    //  | unprotected       | A compute resource that is not protected by a policy. |
    //  +-------------------+-------------------------------------------------------+
    //  
    ListVmwareVcenterComputeResources(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListComputeResourcesResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterComputeResource Returns a representation of the specified VMware compute resource.
    ReadVmwareVcenterComputeResource(
        vcenterId string, 
        computeResourceId string, 
        embed *string)(
        *models.ReadComputeResourceResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterComputeResourcesV1 returns VmwareVcenterComputeResourcesV1Client
func NewVmwareVcenterComputeResourcesV1(config config.Config) VmwareVcenterComputeResourcesV1Client {
    client := new(VmwareVcenterComputeResourcesV1)
    client.config = config
    return client
}
