// Copyright (c) 2021 Clumio All Rights Reserved

// Package managementsubgroups contains methods related to ManagementSubgroups
package managementsubgroups

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// ManagementSubgroupsV1 represents a custom type struct
type ManagementSubgroupsV1 struct {
    config config.Config
}

// ListManagementSubgroups Returns a list of subgroups.
func (m *ManagementSubgroupsV1) ListManagementSubgroups(
    groupId string, 
    limit *int64, 
    start *string)(
    *models.ListSubgroupsResponse, *apiutils.APIError) {

    pathURL := "/management-groups/{group_id}/subgroups"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.management-subgroups=v1+json"
    var result *models.ListSubgroupsResponse
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


// ReadManagementSubgroup Subgroups are used to manage cloud connectors and SQL hosts residing in the same vCenter server.
//  
//  Returns a representation of the specified subgroups.
func (m *ManagementSubgroupsV1) ReadManagementSubgroup(
    subgroupId string, 
    groupId string)(
    *models.ReadSubgroupResponse, *apiutils.APIError) {

    pathURL := "/management-groups/{group_id}/subgroups/{subgroup_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "subgroup_id": subgroupId,
        "group_id": groupId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    
    header := "application/api.clumio.management-subgroups=v1+json"
    var result *models.ReadSubgroupResponse

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


// UpdateManagementSubgroup Update the specified subgroup.
func (m *ManagementSubgroupsV1) UpdateManagementSubgroup(
    subgroupId string, 
    groupId string, 
    body *models.UpdateManagementSubgroupV1Request)(
    *models.UpdateSubgroupResponse, *apiutils.APIError) {

    pathURL := "/management-groups/{group_id}/subgroups/{subgroup_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "subgroup_id": subgroupId,
        "group_id": groupId,
    }
    queryBuilder := m.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.management-subgroups=v1+json"
    var result *models.UpdateSubgroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: m.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}
