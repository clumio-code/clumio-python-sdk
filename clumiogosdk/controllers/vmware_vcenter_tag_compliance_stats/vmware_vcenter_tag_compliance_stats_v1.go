// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcentertagcompliancestats contains methods related to VmwareVcenterTagComplianceStats
package vmwarevcentertagcompliancestats

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterTagComplianceStatsV1 represents a custom type struct
type VmwareVcenterTagComplianceStatsV1 struct {
    config config.Config
}

// ReadVmwareVcenterTagComplianceStats Returns the compliance statistics of the specified tag.
func (v *VmwareVcenterTagComplianceStatsV1) ReadVmwareVcenterTagComplianceStats(
    vcenterId string, 
    tagId string)(
    *models.ReadVMwareTagStatsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/tags/{tag_id}/stats/compliance"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "tag_id": tagId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-tag-compliance-stats=v1+json"
    var result *models.ReadVMwareTagStatsResponse

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
