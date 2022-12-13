// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredawsdynamodbtables contains methods related to RestoredAwsDynamodbTables
package restoredawsdynamodbtables

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsDynamodbTablesV1 represents a custom type struct
type RestoredAwsDynamodbTablesV1 struct {
    config config.Config
}

// RestoreAwsDynamodbTable Restores the specified DynamoDB table backup to the specified target destination.
func (r *RestoredAwsDynamodbTablesV1) RestoreAwsDynamodbTable(
    embed *string, 
    body models.RestoreAwsDynamodbTableV1Request)(
    *models.RestoreDynamoDBTableResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/aws/dynamodb-tables"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-aws-dynamodb-tables=v1+json"
    var result *models.RestoreDynamoDBTableResponse
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
