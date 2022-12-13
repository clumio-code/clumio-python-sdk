// Copyright (c) 2021 Clumio All Rights Reserved

package restoredrecordsawsdynamodbtables

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredRecordsAwsDynamodbTablesV1Client represents a custom type interface
type RestoredRecordsAwsDynamodbTablesV1Client interface {
    // RestoreRecordsAwsDynamodbTable Start a DynamoDB backup records retrieval query with the query filters provided in user input. If the query preview flag is set in the input then the result will be returned to the response otherwise the query will run in background and a task id will be returned.
    RestoreRecordsAwsDynamodbTable(
        embed *string, 
        body *models.RestoreRecordsAwsDynamodbTableV1Request)(
        *models.RestoreRecordsResponseSync,  *apiutils.APIError)
    
}

// NewRestoredRecordsAwsDynamodbTablesV1 returns RestoredRecordsAwsDynamodbTablesV1Client
func NewRestoredRecordsAwsDynamodbTablesV1(config config.Config) RestoredRecordsAwsDynamodbTablesV1Client {
    client := new(RestoredRecordsAwsDynamodbTablesV1)
    client.config = config
    return client
}
