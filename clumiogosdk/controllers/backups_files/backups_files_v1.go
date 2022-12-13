// Copyright (c) 2021 Clumio All Rights Reserved

// Package backupsfiles contains methods related to BackupsFiles
package backupsfiles

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// BackupsFilesV1 represents a custom type struct
type BackupsFilesV1 struct {
    config config.Config
}

// ListFiles Retrieve the list of files whose name matches a given regex pattern.
func (b *BackupsFilesV1) ListFiles(
    limit *int64, 
    start *string, 
    filter string)(
    *models.FileSearchResponse, *apiutils.APIError) {

    queryBuilder := b.config.BaseUrl + "/backups/files/search"

    
    header := "application/api.clumio.backups-files=v1+json"
    var result *models.FileSearchResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": filter,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ListFileVersions Retrieve the list of versions of the file.
func (b *BackupsFilesV1) ListFileVersions(
    searchResultId string, 
    limit *int64, 
    start *string)(
    *models.FileListResponse, *apiutils.APIError) {

    pathURL := "/backups/files/search/{search_result_id}/versions"
    //process optional template parameters
    pathParams := map[string]string{
        "search_result_id": searchResultId,
    }
    queryBuilder := b.config.BaseUrl + pathURL

    
    header := "application/api.clumio.backups-files=v1+json"
    var result *models.FileListResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: b.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
