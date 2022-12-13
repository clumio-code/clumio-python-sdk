// Copyright (c) 2021 Clumio All Rights Reserved

// Package protectiongroups contains methods related to ProtectionGroups
package protectiongroups

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// ProtectionGroupsV1 represents a custom type struct
type ProtectionGroupsV1 struct {
    config config.Config
}

// ListProtectionGroups Returns a list of protection groups.
func (p *ProtectionGroupsV1) ListProtectionGroups(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListProtectionGroupsResponse, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/datasources/protection-groups"

    
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.ListProtectionGroupsResponse
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
        Config: p.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadProtectionGroup Returns a representation of the specified protection group.
func (p *ProtectionGroupsV1) ReadProtectionGroup(
    groupId string)(
    *models.ReadProtectionGroupResponse, *apiutils.APIError) {

    pathURL := "/datasources/protection-groups/{group_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.ReadProtectionGroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateProtectionGroup Creates a new protection group by specifying object filters. Appearance in
//  datasources/protection-groups read/listing is asynchronous and may take a few
//  seconds to minutes at most. As a result, the protection group won't be protectable
//  via /policies/assignments until it appears in the /datasources/protection-groups
//  endpoint. Additionally, to create a protection group in the context of another Organizational
//  Unit, refer to the Getting Started
//  documentation.
func (p *ProtectionGroupsV1) CreateProtectionGroup(
    body models.CreateProtectionGroupV1Request)(
    *models.CreateProtectionGroupResponse, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/protection-groups"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.CreateProtectionGroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// UpdateProtectionGroup Updates a protection group by modifying object filters. Appearance in
//  datasources/protection-groups read/listing is asynchronous and may take a few
//  seconds to minutes at most. Must be in the same OU context as the creator of this
//  protection group.
func (p *ProtectionGroupsV1) UpdateProtectionGroup(
    groupId string, 
    body *models.UpdateProtectionGroupV1Request)(
    *models.UpdateProtectionGroupResponse, *apiutils.APIError) {

    pathURL := "/protection-groups/{group_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.UpdateProtectionGroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}


// DeleteProtectionGroup Marks a protection group as deleted by taking the protection group ID. Appearance
//  in /datasources/protection-groups read/listing is asynchronous and may take a few
//  seconds to minutes at most. Must be in the same OU context as the creator of this
//  protection group.
func (p *ProtectionGroupsV1) DeleteProtectionGroup(
    groupId string)(
    interface{}, *apiutils.APIError) {

    pathURL := "/protection-groups/{group_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    
    header := "application/api.clumio.protection-groups=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// AddBucketProtectionGroup Adds a bucket to protection group and creates a child protection group S3 asset.
//  Appearance in /datasources/protection-groups/s3-assets read/listing is asynchronous
//  and may take a few seconds to minutes at most. Must be in the same OU context as
//  the creator of this protection group. Bucket ID in body can be found in
//  datasources/aws/s3.
func (p *ProtectionGroupsV1) AddBucketProtectionGroup(
    groupId string, 
    body models.AddBucketProtectionGroupV1Request)(
    *models.AddBucketToProtectionGroupResponse, *apiutils.APIError) {

    pathURL := "/protection-groups/{group_id}/buckets"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.AddBucketToProtectionGroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// DeleteBucketProtectionGroup Deletes a bucket from a protection group and the child protection group S3 asset.
//  Appearance in /datasources/protection-groups/s3-assets read/listing is asynchronous
//  and may take a few seconds to minutes at most. Must be in the same OU context as
//  the creator of this protection group. Bucket ID in path can be found in
//  datasources/aws/s3.
func (p *ProtectionGroupsV1) DeleteBucketProtectionGroup(
    groupId string, 
    bucketId string)(
    *models.DeleteBucketFromProtectionGroupResponse, *apiutils.APIError) {

    pathURL := "/protection-groups/{group_id}/buckets/{bucket_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "group_id": groupId,
        "bucket_id": bucketId,
    }
    queryBuilder := p.config.BaseUrl + pathURL

    
    header := "application/api.clumio.protection-groups=v1+json"
    var result *models.DeleteBucketFromProtectionGroupResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}
