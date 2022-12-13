// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentertagcompliancestats

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterTagComplianceStatsV1Client represents a custom type interface
type VmwareVcenterTagComplianceStatsV1Client interface {
    // ReadVmwareVcenterTagComplianceStats Returns the compliance statistics of the specified tag.
    ReadVmwareVcenterTagComplianceStats(
        vcenterId string, 
        tagId string)(
        *models.ReadVMwareTagStatsResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterTagComplianceStatsV1 returns VmwareVcenterTagComplianceStatsV1Client
func NewVmwareVcenterTagComplianceStatsV1(config config.Config) VmwareVcenterTagComplianceStatsV1Client {
    client := new(VmwareVcenterTagComplianceStatsV1)
    client.config = config
    return client
}
