// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenterhosts contains methods related to VmwareVcenterHosts
package vmwarevcenterhosts

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterHostsV1 represents a custom type struct
type VmwareVcenterHostsV1 struct {
    config config.Config
}

// ListVmwareVcenterHosts Returns a list of hosts in the specified vCenter server.
func (v *VmwareVcenterHostsV1) ListVmwareVcenterHosts(
    vcenterId string, 
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListHostsResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/hosts"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-hosts=v1+json"
    var result *models.ListHostsResponse
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
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
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


// ReadVmwareVcenterHost Returns a representation of the specified host.
func (v *VmwareVcenterHostsV1) ReadVmwareVcenterHost(
    vcenterId string, 
    hostId string)(
    *models.ReadHostResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/hosts/{host_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "host_id": hostId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-hosts=v1+json"
    var result *models.ReadHostResponse

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
