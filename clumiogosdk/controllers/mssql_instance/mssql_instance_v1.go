// Copyright (c) 2021 Clumio All Rights Reserved

// Package mssqlinstance contains methods related to MssqlInstance
package mssqlinstance

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlInstanceV1 represents a custom type struct
type MssqlInstanceV1 struct {
    config config.Config
}

// ListMssqlInstance Returns a list of Instances
func (m *MssqlInstanceV1) ListMssqlInstance(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListMssqlInstancesResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/datasources/mssql/instances"

    
    header := "application/api.clumio.mssql-instance=v1+json"
    var result *models.ListMssqlInstancesResponse
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
        Config: m.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadMssqlInstance Returns a representation of the specified instance.
func (m *MssqlInstanceV1) ReadMssqlInstance(
    instanceId string)(
    *models.ReadMssqlInstanceResponse, *apiutils.APIError) {

    pathURL := "/datasources/mssql/instances/{instance_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "instance_id": instanceId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.mssql-instance=v1+json"
    var result *models.ReadMssqlInstanceResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
