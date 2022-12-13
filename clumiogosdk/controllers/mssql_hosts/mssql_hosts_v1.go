// Copyright (c) 2021 Clumio All Rights Reserved

// Package mssqlhosts contains methods related to MssqlHosts
package mssqlhosts

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlHostsV1 represents a custom type struct
type MssqlHostsV1 struct {
    config config.Config
}

// ListMssqlHostConnections Returns a list of hosts
func (m *MssqlHostsV1) ListMssqlHostConnections(
    currentCount *int64, 
    filter *string, 
    limit *int64, 
    start *string)(
    *models.ListHcmHostsResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/connections/mssql/hosts"

    
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.ListHcmHostsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if currentCount == nil {
        currentCount = &defaultInt64
    }
    if filter == nil {
        filter = &defaultString
    }
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    
    queryParams := map[string]string{
        "currentCount": fmt.Sprintf("%v", *currentCount),
        "filter": *filter,
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
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


// CreateMssqlHostConnections Create a MSSQL Connection.
func (m *MssqlHostsV1) CreateMssqlHostConnections(
    body *models.CreateMssqlHostConnectionsV1Request)(
    *models.CreateHcmHostResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/connections/mssql/hosts"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.CreateHcmHostResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// DeleteMssqlHostConnections Delete the specified MSSQL host.
func (m *MssqlHostsV1) DeleteMssqlHostConnections(
    embed *string, 
    body *models.DeleteMssqlHostConnectionsV1Request)(
    *models.DeleteHcmHostResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/connections/mssql/hosts"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.DeleteHcmHostResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// MoveMssqlHostConnections Move the specified MSSQL hosts from a source Sub-Group to a destination Sub-Group.
func (m *MssqlHostsV1) MoveMssqlHostConnections(
    embed *string, 
    body *models.MoveMssqlHostConnectionsV1Request)(
    *models.MoveHcmHostsResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/connections/mssql/hosts"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.MoveHcmHostsResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}


// CreateMssqlHostConnectionCredentials Create Edge Connector Credentials for the specified MSSQL host.
func (m *MssqlHostsV1) CreateMssqlHostConnectionCredentials(
    body *models.CreateMssqlHostConnectionCredentialsV1Request)(
    *models.CreateHostECCredentialsResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/connections/mssql/hosts/eccredentials"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.CreateHostECCredentialsResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadMssqlHostConnections Returns a representation of the specified host.
func (m *MssqlHostsV1) ReadMssqlHostConnections(
    hostId string)(
    *models.ReadHcmHostResponse, *apiutils.APIError) {

    pathURL := "/connections/mssql/hosts/{host_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "host_id": hostId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.ReadHcmHostResponse

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


// ListMssqlHosts Returns a list of hosts
func (m *MssqlHostsV1) ListMssqlHosts(
    limit *int64, 
    start *string, 
    filter *string, 
    embed *string)(
    *models.ListMssqlHostsResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/datasources/mssql/hosts"

    
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.ListMssqlHostsResponse
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
        Config: m.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadMssqlHosts Returns a representation of the specified host.
func (m *MssqlHostsV1) ReadMssqlHosts(
    hostId string)(
    *models.ReadMssqlHostResponse, *apiutils.APIError) {

    pathURL := "/datasources/mssql/hosts/{host_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "host_id": hostId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.mssql-hosts=v1+json"
    var result *models.ReadMssqlHostResponse

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
