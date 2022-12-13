// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcentercomputeresources contains methods related to VmwareVcenterComputeResources
package vmwarevcentercomputeresources

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterComputeResourcesV1 represents a custom type struct
type VmwareVcenterComputeResourcesV1 struct {
    config config.Config
}

// ListVmwareVcenterComputeResources Returns a list of VMware compute resources in the specified vCenter server.
//  
//  The following table lists the supported Clumio protection statuses:
//  
//  
//  +-------------------+-------------------------------------------------------+
//  | Protection Status |                        Values                         |
//  +===================+=======================================================+
//  | protected         | A compute resource that is protected by a policy.     |
//  +-------------------+-------------------------------------------------------+
//  | unprotected       | A compute resource that is not protected by a policy. |
//  +-------------------+-------------------------------------------------------+
//  
func (v *VmwareVcenterComputeResourcesV1) ListVmwareVcenterComputeResources(
    vcenterId string, 
    limit *int64, 
    start *string, 
    filter *string, 
    embed *string)(
    *models.ListComputeResourcesResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/compute-resources"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-compute-resources=v1+json"
    var result *models.ListComputeResourcesResponse
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
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
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


// ReadVmwareVcenterComputeResource Returns a representation of the specified VMware compute resource.
func (v *VmwareVcenterComputeResourcesV1) ReadVmwareVcenterComputeResource(
    vcenterId string, 
    computeResourceId string, 
    embed *string)(
    *models.ReadComputeResourceResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/compute-resources/{compute_resource_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "compute_resource_id": computeResourceId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-compute-resources=v1+json"
    var result *models.ReadComputeResourceResponse
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
