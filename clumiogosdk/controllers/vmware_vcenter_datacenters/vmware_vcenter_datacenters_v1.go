// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenterdatacenters contains methods related to VmwareVcenterDatacenters
package vmwarevcenterdatacenters

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterDatacentersV1 represents a custom type struct
type VmwareVcenterDatacentersV1 struct {
    config config.Config
}

// ListVmwareVcenterDatacenters Returns a list of VMware data centers in the specified vCenter server.
func (v *VmwareVcenterDatacentersV1) ListVmwareVcenterDatacenters(
    vcenterId string, 
    limit *int64, 
    start *string, 
    filter *string, 
    Embed *string)(
    *models.ListDatacentersResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/datacenters"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-datacenters=v1+json"
    var result *models.ListDatacentersResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    if Embed == nil {
        Embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
        "Embed": *Embed,
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


// ReadVmwareVcenterDatacenter Returns a representation of the specified VMware data center within the specified vCenter server.
func (v *VmwareVcenterDatacentersV1) ReadVmwareVcenterDatacenter(
    vcenterId string, 
    datacenterId string, 
    embed *string)(
    *models.ReadDatacenterResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/datacenters/{datacenter_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "datacenter_id": datacenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-datacenters=v1+json"
    var result *models.ReadDatacenterResponse
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
