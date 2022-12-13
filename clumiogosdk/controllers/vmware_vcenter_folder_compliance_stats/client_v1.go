// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcenterfoldercompliancestats

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterFolderComplianceStatsV1Client represents a custom type interface
type VmwareVcenterFolderComplianceStatsV1Client interface {
    // ReadVmwareVcenterFolderComplianceStats Returns the compliance statistics of VMs under folders and subfolders of the specified VMware folder.
    ReadVmwareVcenterFolderComplianceStats(
        vcenterId string, 
        folderId string)(
        *models.ReadVMwareFolderStatsResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterFolderComplianceStatsV1 returns VmwareVcenterFolderComplianceStatsV1Client
func NewVmwareVcenterFolderComplianceStatsV1(config config.Config) VmwareVcenterFolderComplianceStatsV1Client {
    client := new(VmwareVcenterFolderComplianceStatsV1)
    client.config = config
    return client
}
