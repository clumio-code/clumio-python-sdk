// Copyright (c) 2021 Clumio All Rights Reserved

// Package vmwarevcenterdatastores contains methods related to VmwareVcenterDatastores
package vmwarevcenterdatastores

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterDatastoresV1 represents a custom type struct
type VmwareVcenterDatastoresV1 struct {
    config config.Config
}

// ListVmwareVcenterDatastores Returns a list of datastores in the specified vCenter server.
//  
//  
//  Supported Datastore Types
//  Clumio supports the following VMware datastore types:
//  
//  Network File System (nfs)
//  vSAN (virtual_storage_area_network)
//  vSphere Virtual Machine File System (vmfs)
//  Virtual Volumes (virtual_volume)
//  
func (v *VmwareVcenterDatastoresV1) ListVmwareVcenterDatastores(
    vcenterId string, 
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListVMwareDatastoresResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/datastores"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-datastores=v1+json"
    var result *models.ListVMwareDatastoresResponse
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


// ReadVmwareVcenterDatastore Returns a representation of the specified datastore.
func (v *VmwareVcenterDatastoresV1) ReadVmwareVcenterDatastore(
    vcenterId string, 
    datastoreId string)(
    *models.ReadVMwareDatastoreResponse, *apiutils.APIError) {

    pathURL := "/datasources/vmware/vcenters/{vcenter_id}/datastores/{datastore_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "vcenter_id": vcenterId,
        "datastore_id": datastoreId,
    }
    queryBuilder := v.config.BaseUrl + pathURL

    
    header := "application/api.clumio.vmware-vcenter-datastores=v1+json"
    var result *models.ReadVMwareDatastoreResponse

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
