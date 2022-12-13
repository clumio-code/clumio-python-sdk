// Copyright (c) 2021 Clumio All Rights Reserved

// Package awsconnections contains methods related to AwsConnections
package awsconnections

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsConnectionsV1 represents a custom type struct
type AwsConnectionsV1 struct {
    config config.Config
}

// ListAwsConnections Returns a list of AWS Connections
func (a *AwsConnectionsV1) ListAwsConnections(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListAWSConnectionsResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/connections/aws"

    
    header := "application/api.clumio.aws-connections=v1+json"
    var result *models.ListAWSConnectionsResponse
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
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateAwsConnection Initiate a new AWS connection.
func (a *AwsConnectionsV1) CreateAwsConnection(
    body *models.CreateAwsConnectionV1Request)(
    *models.CreateAWSConnectionResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/connections/aws"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.aws-connections=v1+json"
    var result *models.CreateAWSConnectionResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadAwsConnection Returns a representation of the specified AWS connection.
func (a *AwsConnectionsV1) ReadAwsConnection(
    connectionId string)(
    *models.ReadAWSConnectionResponse, *apiutils.APIError) {

    pathURL := "/connections/aws/{connection_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "connection_id": connectionId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.aws-connections=v1+json"
    var result *models.ReadAWSConnectionResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// DeleteAwsConnection Delete the specified AWS connection.
func (a *AwsConnectionsV1) DeleteAwsConnection(
    connectionId string)(
    interface{}, *apiutils.APIError) {

    pathURL := "/connections/aws/{connection_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "connection_id": connectionId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.aws-connections=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// UpdateAwsConnection Returns a new template url for the specified configuration.
func (a *AwsConnectionsV1) UpdateAwsConnection(
    connectionId string, 
    body models.UpdateAwsConnectionV1Request)(
    *models.UpdateAWSConnectionResponse, *apiutils.APIError) {

    pathURL := "/connections/aws/{connection_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "connection_id": connectionId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.aws-connections=v1+json"
    var result *models.UpdateAWSConnectionResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
