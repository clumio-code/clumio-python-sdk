// Copyright (c) 2021 Clumio All Rights Reserved

package restoredmssqldatabases

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredMssqlDatabasesV1Client represents a custom type interface
type RestoredMssqlDatabasesV1Client interface {
    // RestoreMssqlDatabase Creates a restored MSSQL database from a given backup or to a specified point in time.
    RestoreMssqlDatabase(
        embed *string, 
        body models.RestoreMssqlDatabaseV1Request)(
        *models.CreateMssqlDatabaseRestoreResponse,  *apiutils.APIError)
    
}

// NewRestoredMssqlDatabasesV1 returns RestoredMssqlDatabasesV1Client
func NewRestoredMssqlDatabasesV1(config config.Config) RestoredMssqlDatabasesV1Client {
    client := new(RestoredMssqlDatabasesV1)
    client.config = config
    return client
}
