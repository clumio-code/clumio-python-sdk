// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenters contains methods related to VmwareVcenters
package vmwarevcenters

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcentersV1 represents a custom type struct
type VmwareVcentersV1 struct {
    config config.Config
}

// ListVmwareVcenters Returns a list of vCenter servers.
func (v *VmwareVcentersV1) ListVmwareVcenters(
    limit *int64, 
    start *string, 
    embed *string)(
    *models.ListVcentersResponse, *apiutils.APIError) {

    queryBuilder := v.config.BaseUrl + "/datasources/vmware/vcenters"

    
    header := "application/api.clumio.vmware-vcenters=v1+json"
    var result *models.ListVcentersResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: v.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadVmwareVcenter Returns a representation of the specified vCenter server.
func (v *VmwareVcentersV1) ReadVmwareVcenter(
    vcenterId string, 
    embed *string)(
    *models.ReadVcenterResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenters=v1+json"
    var result *models.ReadVcenterResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: v.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
