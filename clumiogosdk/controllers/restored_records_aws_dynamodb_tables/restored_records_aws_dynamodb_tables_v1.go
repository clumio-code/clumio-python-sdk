// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredrecordsawsdynamodbtables contains methods related to RestoredRecordsAwsDynamodbTables
package restoredrecordsawsdynamodbtables

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredRecordsAwsDynamodbTablesV1 represents a custom type struct
type RestoredRecordsAwsDynamodbTablesV1 struct {
    config config.Config
}

// RestoreRecordsAwsDynamodbTable Start a DynamoDB backup records retrieval query with the query filters provided in user input. If the query preview flag is set in the input then the result will be returned to the response otherwise the query will run in background and a task id will be returned.
func (r *RestoredRecordsAwsDynamodbTablesV1) RestoreRecordsAwsDynamodbTable(
    embed *string, 
    body *models.RestoreRecordsAwsDynamodbTableV1Request)(
    *models.RestoreRecordsResponseSync, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/aws/dynamodb-tables/records"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-records-aws-dynamodb-tables=v1+json"
    var result *models.RestoreRecordsResponseSync
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
