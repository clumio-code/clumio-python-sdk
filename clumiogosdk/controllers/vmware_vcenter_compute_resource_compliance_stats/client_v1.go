// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentercomputeresourcecompliancestats

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComputeResourceComplianceStatsV1Client represents a custom type interface
type VmwareVcenterComputeResourceComplianceStatsV1Client interface {
    // ReadVmwareVcenterComputeResourceComplianceStats Returns a representation of the compliance statistics of the specified VMware compute resource.
    ReadVmwareVcenterComputeResourceComplianceStats(
        vcenterId string, 
        computeResourceId string)(
        *models.ReadVMwareComputeResourceStatsResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterComputeResourceComplianceStatsV1 returns VmwareVcenterComputeResourceComplianceStatsV1Client
func NewVmwareVcenterComputeResourceComplianceStatsV1(config config.Config) VmwareVcenterComputeResourceComplianceStatsV1Client {
    client := new(VmwareVcenterComputeResourceComplianceStatsV1)
    client.config = config
    return client
}
