// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredmssqldatabases contains methods related to RestoredMssqlDatabases
package restoredmssqldatabases

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredMssqlDatabasesV1 represents a custom type struct
type RestoredMssqlDatabasesV1 struct {
    config config.Config
}

// RestoreMssqlDatabase Creates a restored MSSQL database from a given backup or to a specified point in time.
func (r *RestoredMssqlDatabasesV1) RestoreMssqlDatabase(
    embed *string, 
    body models.RestoreMssqlDatabaseV1Request)(
    *models.CreateMssqlDatabaseRestoreResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/mssql/databases"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-mssql-databases=v1+json"
    var result *models.CreateMssqlDatabaseRestoreResponse
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
