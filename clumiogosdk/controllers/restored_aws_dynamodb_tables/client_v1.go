// Copyright (c) 2021 Clumio All Rights Reserved

package restoredawsdynamodbtables

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsDynamodbTablesV1Client represents a custom type interface
type RestoredAwsDynamodbTablesV1Client interface {
    // RestoreAwsDynamodbTable Restores the specified DynamoDB table backup to the specified target destination.
    RestoreAwsDynamodbTable(
        embed *string, 
        body models.RestoreAwsDynamodbTableV1Request)(
        *models.RestoreDynamoDBTableResponse,  *apiutils.APIError)
    
}

// NewRestoredAwsDynamodbTablesV1 returns RestoredAwsDynamodbTablesV1Client
func NewRestoredAwsDynamodbTablesV1(config config.Config) RestoredAwsDynamodbTablesV1Client {
    client := new(RestoredAwsDynamodbTablesV1)
    client.config = config
    return client
}
