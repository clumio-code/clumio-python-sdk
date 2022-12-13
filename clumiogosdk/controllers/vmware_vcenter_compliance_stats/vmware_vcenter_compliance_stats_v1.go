// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcentercompliancestats contains methods related to VmwareVcenterComplianceStats
package vmwarevcentercompliancestats

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComplianceStatsV1 represents a custom type struct
type VmwareVcenterComplianceStatsV1 struct {
    config config.Config
}

// ReadVmwareVcenterComplianceStats Returns a representation of the compliance statistics of VMs in the specified vCenter server.
func (v *VmwareVcenterComplianceStatsV1) ReadVmwareVcenterComplianceStats(
    vcenterId string)(
    *models.ReadVMwareVCenterProtectionStatsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/stats/compliance"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-compliance-stats=v1+json"
    var result *models.ReadVMwareVCenterProtectionStatsResponse

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
