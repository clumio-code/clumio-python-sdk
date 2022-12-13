// Copyright (c) 2021 Clumio All Rights Reserved

// Package awsenvironments contains methods related to AwsEnvironments
package awsenvironments

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsEnvironmentsV1 represents a custom type struct
type AwsEnvironmentsV1 struct {
    config config.Config
}

// ListAwsEnvironments Returns a list of AWS environments.
func (a *AwsEnvironmentsV1) ListAwsEnvironments(
    limit *int64, 
    start *string, 
    filter *string, 
    embed *string)(
    *models.ListAWSEnvironmentsResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/datasources/aws/environments"

    
    header := "application/api.clumio.aws-environments=v1+json"
    var result *models.ListAWSEnvironmentsResponse
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
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadAwsEnvironment Returns a representation of the specified AWS environment.
func (a *AwsEnvironmentsV1) ReadAwsEnvironment(
    environmentId string, 
    embed *string)(
    *models.ReadAWSEnvironmentResponse, *apiutils.APIError) {

    pathURL := "/datasources/aws/environments/{environment_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "environment_id": environmentId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.aws-environments=v1+json"
    var result *models.ReadAWSEnvironmentResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
