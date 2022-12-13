// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentercompliancestats

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComplianceStatsV1Client represents a custom type interface
type VmwareVcenterComplianceStatsV1Client interface {
    // ReadVmwareVcenterComplianceStats Returns a representation of the compliance statistics of VMs in the specified vCenter server.
    ReadVmwareVcenterComplianceStats(
        vcenterId string)(
        *models.ReadVMwareVCenterProtectionStatsResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterComplianceStatsV1 returns VmwareVcenterComplianceStatsV1Client
func NewVmwareVcenterComplianceStatsV1(config config.Config) VmwareVcenterComplianceStatsV1Client {
    client := new(VmwareVcenterComplianceStatsV1)
    client.config = config
    return client
}
