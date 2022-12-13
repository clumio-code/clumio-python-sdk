// Copyright (c) 2021 Clumio All Rights Reserved

package mssqldatabases

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlDatabasesV1Client represents a custom type interface
type MssqlDatabasesV1Client interface {
    // ListMssqlDatabases Returns a list of Databases
    ListMssqlDatabases(
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListMssqlDatabasesResponse,  *apiutils.APIError)
    
    // ReadMssqlDatabases Returns a representation of the specified database.
    ReadMssqlDatabases(
        databaseId string)(
        *models.ReadMssqlDatabaseResponse,  *apiutils.APIError)
    
    // ListMssqlDatabasePitrIntervals Returns restorable times as a list of intervals.
    ListMssqlDatabasePitrIntervals(
        databaseId string, 
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListMssqlDatabasePitrIntervalsResponse,  *apiutils.APIError)
    
}

// NewMssqlDatabasesV1 returns MssqlDatabasesV1Client
func NewMssqlDatabasesV1(config config.Config) MssqlDatabasesV1Client {
    client := new(MssqlDatabasesV1)
    client.config = config
    return client
}
