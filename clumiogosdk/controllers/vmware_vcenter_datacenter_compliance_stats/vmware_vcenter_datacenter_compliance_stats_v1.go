// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenterdatacentercompliancestats contains methods related to VmwareVcenterDatacenterComplianceStats
package vmwarevcenterdatacentercompliancestats

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterDatacenterComplianceStatsV1 represents a custom type struct
type VmwareVcenterDatacenterComplianceStatsV1 struct {
    config config.Config
}

// ReadVmwareVcenterDatacenterComplianceStats Returns a representation of the compliance statistics of the specified data center.
func (v *VmwareVcenterDatacenterComplianceStatsV1) ReadVmwareVcenterDatacenterComplianceStats(
    vcenterId string, 
    datacenterId string)(
    *models.ReadVMwareDatacenterStatsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/datacenters/{datacenter_id}/stats/compliance"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "datacenter_id": datacenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-datacenter-compliance-stats=v1+json"
    var result *models.ReadVMwareDatacenterStatsResponse

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
