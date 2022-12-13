// Copyright (c) 2021 Clumio All Rights Reserved

// Package mssqldatabases contains methods related to MssqlDatabases
package mssqldatabases

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlDatabasesV1 represents a custom type struct
type MssqlDatabasesV1 struct {
    config config.Config
}

// ListMssqlDatabases Returns a list of Databases
func (m *MssqlDatabasesV1) ListMssqlDatabases(
    limit *int64, 
    start *string, 
    filter *string, 
    embed *string)(
    *models.ListMssqlDatabasesResponse, *apiutils.APIError) {

    queryBuilder := m.config.BaseUrl + "/datasources/mssql/databases"

    
    header := "application/api.clumio.mssql-databases=v1+json"
    var result *models.ListMssqlDatabasesResponse
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


// ReadMssqlDatabases Returns a representation of the specified database.
func (m *MssqlDatabasesV1) ReadMssqlDatabases(
    databaseId string)(
    *models.ReadMssqlDatabaseResponse, *apiutils.APIError) {

    pathURL := "/datasources/mssql/databases/{database_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "database_id": databaseId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.mssql-databases=v1+json"
    var result *models.ReadMssqlDatabaseResponse

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


// ListMssqlDatabasePitrIntervals Returns restorable times as a list of intervals.
func (m *MssqlDatabasesV1) ListMssqlDatabasePitrIntervals(
    databaseId string, 
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListMssqlDatabasePitrIntervalsResponse, *apiutils.APIError) {

    pathURL := "/datasources/mssql/databases/{database_id}/pitr-intervals"
    //process optional template parameters
    pathParams := map[string]string{
        "database_id": databaseId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.mssql-databases=v1+json"
    var result *models.ListMssqlDatabasePitrIntervalsResponse
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
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
