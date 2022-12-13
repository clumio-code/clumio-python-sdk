// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcentercomputeresourcecompliancestats contains methods related to VmwareVcenterComputeResourceComplianceStats
package vmwarevcentercomputeresourcecompliancestats

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComputeResourceComplianceStatsV1 represents a custom type struct
type VmwareVcenterComputeResourceComplianceStatsV1 struct {
    config config.Config
}

// ReadVmwareVcenterComputeResourceComplianceStats Returns a representation of the compliance statistics of the specified VMware compute resource.
func (v *VmwareVcenterComputeResourceComplianceStatsV1) ReadVmwareVcenterComputeResourceComplianceStats(
    vcenterId string, 
    computeResourceId string)(
    *models.ReadVMwareComputeResourceStatsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/compute-resources/{compute_resource_id}/stats/compliance"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "compute_resource_id": computeResourceId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-compute-resource-compliance-stats=v1+json"
    var result *models.ReadVMwareComputeResourceStatsResponse

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
