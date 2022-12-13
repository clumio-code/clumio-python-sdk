// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenternetworks contains methods related to VmwareVcenterNetworks
package vmwarevcenternetworks

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterNetworksV1 represents a custom type struct
type VmwareVcenterNetworksV1 struct {
    config config.Config
}

// ListVmwareVcenterNetworks Returns a list of networks in the specified vCenter server.
func (v *VmwareVcenterNetworksV1) ListVmwareVcenterNetworks(
    vcenterId string, 
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListVMwareVCenterNetworksResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/networks"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-networks=v1+json"
    var result *models.ListVMwareVCenterNetworksResponse
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


// ReadVmwareVcenterNetwork Returns a representation of the specified network.
func (v *VmwareVcenterNetworksV1) ReadVmwareVcenterNetwork(
    vcenterId string, 
    networkId string)(
    *models.ReadVMwareVCenterNetworkResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/networks/{network_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "network_id": networkId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-networks=v1+json"
    var result *models.ReadVMwareVCenterNetworkResponse

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
