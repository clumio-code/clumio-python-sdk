// Copyright (c) 2021 Clumio All Rights Reserved

// Package awsrdsresourcerestoredrecords contains methods related to AwsRdsResourceRestoredRecords
package awsrdsresourcerestoredrecords

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsRdsResourceRestoredRecordsV1 represents a custom type struct
type AwsRdsResourceRestoredRecordsV1 struct {
    config config.Config
}

// ListRdsRestoredRecords Returns a list of RDS database restored-records.
func (a *AwsRdsResourceRestoredRecordsV1) ListRdsRestoredRecords(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListRestoredRecordsResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/restores/aws/rds-resources/records"

    
    header := "application/api.clumio.aws-rds-resource-restored-records=v1+json"
    var result *models.ListRestoredRecordsResponse
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


// RestoreRdsRecord Start a database backup query with the query statement provided in user input. If the query preview flag is set in the input then the result will be returned in the response otherwise the query will run in background and a task id will be returned.
func (a *AwsRdsResourceRestoredRecordsV1) RestoreRdsRecord(
    embed *string, 
    body *models.RestoreRdsRecordV1Request)(
    *models.RestoreRecordPreviewResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/restores/aws/rds-resources/records"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.aws-rds-resource-restored-records=v1+json"
    var result *models.RestoreRecordPreviewResponse
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
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
