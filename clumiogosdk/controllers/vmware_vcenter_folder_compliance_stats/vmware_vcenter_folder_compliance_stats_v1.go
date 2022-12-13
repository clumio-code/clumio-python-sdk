// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenterfoldercompliancestats contains methods related to VmwareVcenterFolderComplianceStats
package vmwarevcenterfoldercompliancestats

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterFolderComplianceStatsV1 represents a custom type struct
type VmwareVcenterFolderComplianceStatsV1 struct {
    config config.Config
}

// ReadVmwareVcenterFolderComplianceStats Returns the compliance statistics of VMs under folders and subfolders of the specified VMware folder.
func (v *VmwareVcenterFolderComplianceStatsV1) ReadVmwareVcenterFolderComplianceStats(
    vcenterId string, 
    folderId string)(
    *models.ReadVMwareFolderStatsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/folders/{folder_id}/stats/compliance"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "folder_id": folderId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-folder-compliance-stats=v1+json"
    var result *models.ReadVMwareFolderStatsResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: v.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
